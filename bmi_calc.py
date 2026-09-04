#This is a BMI calc I am making just to practice
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in ft: "))
height_m = height * 0.3048  # Convert height from feet to meters
BMI = weight / (height_m * height_m)  # Calculate BMI using the formula: weight (kg) / (height (m))^2
print("Your BMI is: ", BMI)