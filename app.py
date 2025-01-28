import requests
from bs4 import BeautifulSoup
import re
import csv
import os
import datetime

# Function to calculate BMI and suggest calorie ranges
def calculate_bmi_and_calories(weight, height):
    # Convert height from cm to meters
    height_m = height / 100
    # Calculate BMI
    bmi = weight / (height_m ** 2)
    bmi_status = ""

    if bmi < 18.5:
        bmi_status = "Underweight"
    elif 18.5 <= bmi < 24.9:
        bmi_status = "Normal weight"
    elif 25 <= bmi < 29.9:
        bmi_status = "Overweight"
    else:
        bmi_status = "Obesity"

    # Calculate calorie needs using Mifflin-St Jeor Equation (approximation)
    bmr = 10 * weight + 6.25 * height - 5 * 25 + 5  # Assuming age 25 for now
    maintenance_calories = bmr * 1.55  # Moderate activity level
    weight_loss_calories = maintenance_calories - 500
    weight_gain_calories = maintenance_calories + 500

    return {
        "bmi": round(bmi, 2),
        "bmi_status": bmi_status,
        "maintenance_calories": round(maintenance_calories),
        "weight_loss_calories": round(weight_loss_calories),
        "weight_gain_calories": round(weight_gain_calories),
    }

# Function to search for food and extract calorie information
def get_food_calories(food_item):
    url = "https://www.fatsecret.com/calories-nutrition/search?q=" + food_item
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    food_items = soup.find_all('a', {'class': 'prominent'})

    result = []
    if food_items:
        for item in food_items:
            food_name = item.get_text(strip=True)
            calorie_info = item.find_next('div', {'class': 'smallText greyText greyLink'})
            if calorie_info:
                match = re.search(r'Calories:\s*(\d+)', calorie_info.get_text())
                if match:
                    calories = int(match.group(1))
                    result.append((food_name, calories))
    return result

# Function to save the selected food and its calorie count to a CSV file
def save_food_data(food_name, calories, quantity, total_calories, date, name):
    filename = f"{name.replace(' ', '_')}_food_log.csv"
    file_exists = os.path.exists(filename)
    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date", "Food Name", "Calories", "Quantity", "Total Calories"])
        total_food_calories = calories * quantity
        total_calories += total_food_calories
        writer.writerow([date, food_name, calories, quantity, total_food_calories])
    return total_calories

# Function to log the total calories consumed for the day
def log_daily_total(date, total_calories, name):
    filename = f"{name.replace(' ', '_')}_food_log.csv"
    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, "Total Calories for the Day", "", "", total_calories])

# Main program to track and sum calories
def track_calories():
    name = input("Enter your name: ").strip()
    filename = f"{name.replace(' ', '_')}_food_log.csv"
    total_calories = 0

    # Get user weight and height for BMI calculation
    weight = float(input("Enter your weight (in kg): "))
    height = float(input("Enter your height (in cm): "))

    bmi_data = calculate_bmi_and_calories(weight, height)
    print(f"\nYour BMI: {bmi_data['bmi']} ({bmi_data['bmi_status']})")
    print(f"Calories to maintain weight: {bmi_data['maintenance_calories']} kcal/day")
    print(f"Calories for weight loss: {bmi_data['weight_loss_calories']} kcal/day")
    print(f"Calories for weight gain: {bmi_data['weight_gain_calories']} kcal/day\n")

    date = datetime.date.today().strftime("%Y-%m-%d")
    while True:
        print("Press Ctrl+C to Exit or type 'exit' to finish.")
        food_item = input("Enter Food Item: ").strip()
        if food_item.lower() == "exit":
            break
        food_list = get_food_calories(food_item)
        if food_list:
            print(f"\nFound {len(food_list)} items for '{food_item}':")
            for i, (food_name, calories) in enumerate(food_list, 1):
                print(f"{i}. {food_name} - {calories} kcal")
            while True:
                try:
                    selection = int(input(f"Select a food item by number (1-{len(food_list)}): "))
                    if 1 <= selection <= len(food_list):
                        selected_food = food_list[selection - 1]
                        food_name, calories = selected_food
                        break
                    else:
                        print("Invalid selection. Please select a valid number.")
                except ValueError:
                    print("Please enter a valid number.")
            while True:
                try:
                    quantity = int(input(f"Enter quantity of {food_name} (e.g., 1, 2, 3, ...): "))
                    if quantity > 0:
                        break
                    else:
                        print("Quantity must be positive.")
                except ValueError:
                    print("Please enter a valid number for quantity.")
            total_calories = save_food_data(food_name, calories, quantity, total_calories, date, name)
            print(f"{food_name}: {calories} kcal x {quantity} = {calories * quantity} kcal")
            print(f"Total Calories So Far: {total_calories} kcal\n")
        else:
            print(f"No results found for '{food_item}'.")
    log_daily_total(date, total_calories, name)
    print(f"\nTotal Calories Consumed Today: {total_calories} kcal")

# Run the program
if __name__ == "__main__":
    track_calories()
