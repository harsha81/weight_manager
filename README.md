Calorie Tracking Program
This Python program helps track your daily calorie intake by allowing you to log food items and their respective calories. It calculates your BMI (Body Mass Index), suggests daily calorie ranges for maintenance, weight loss, and weight gain, and allows you to log food consumption for the day.

Features
BMI Calculation: The program calculates your BMI based on your weight and height, and provides an interpretation (Underweight, Normal weight, Overweight, or Obesity).
Calorie Needs: It estimates your daily calorie needs for maintaining weight, losing weight, or gaining weight based on the Mifflin-St Jeor Equation.
Food Search: The program uses a web scraper to search for food items and retrieve their calorie information from FatSecret.
Food Logging: You can log food items consumed during the day with their quantity, and the program will calculate the total calories for the day.
CSV Logging: All data is saved in a CSV file named after the user's name, and it stores each entry with the date, food name, calories, quantity, and total calories.
Daily Total: At the end of the day, the total calories consumed are logged.
Requirements
Python 3.x: Ensure Python 3 is installed.
Libraries:
requests: For making HTTP requests to fetch food data.
beautifulsoup4: For parsing HTML and extracting food calorie information.
csv: To store food logs in CSV format.
os: To handle file operations.
datetime: To log the current date.
You can install the required libraries using pip:

bash
Copy
Edit
pip install requests beautifulsoup4
Usage
Run the Program:

To start the program, run the script in your terminal or Python IDE:
bash
Copy
Edit
python calorie_tracking.py
Input Information:

Enter your name, weight (in kg), and height (in cm).
The program will display your BMI and your calorie needs.
Log Food Items:

After displaying your BMI, enter the name of a food item.
The program will search for matching foods and show a list of options with calorie information.
Select a food item by entering its corresponding number.
Enter the quantity of the selected food item to calculate the total calories.
Exit the Program:

To finish logging for the day, type exit when prompted for a food item.
CSV Log:

All data will be saved in a CSV file named YourName_food_log.csv (e.g., John_Doe_food_log.csv).
Example Output
plaintext
Copy
Edit
Enter your name: John Doe
Enter your weight (in kg): 70
Enter your height (in cm): 175

Your BMI: 22.86 (Normal weight)
Calories to maintain weight: 2505 kcal/day
Calories for weight loss: 2005 kcal/day
Calories for weight gain: 3005 kcal/day

Enter Food Item: Apple
Found 3 items for 'Apple':
1. Apple, raw - 52 kcal
2. Apple, baked - 95 kcal
3. Apple, sliced - 40 kcal
Select a food item by number (1-3): 1
Enter quantity of Apple, raw (e.g., 1, 2, 3, ...): 2
Apple, raw: 52 kcal x 2 = 104 kcal
Total Calories So Far: 104 kcal

Enter Food Item: exit

Total Calories Consumed Today: 104 kcal
File Structure
The program generates a CSV file for each user, where the logs are stored. For example:

mathematica
Copy
Edit
John_Doe_food_log.csv
  - Date, Food Name, Calories, Quantity, Total Calories
  - 2025-01-28, Apple, raw, 52, 104
  - 2025-01-28, Total Calories for the Day, , , 104
