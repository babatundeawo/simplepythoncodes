temp_value = float(input("Enter value of the temperature: "))
temp_unit = str(input("Select Celsius to Fahrenheit (A) or Fahrenheit to Celsius (B): "))

if temp_unit.upper() == "A":
    fahrenheit = (temp_value * 9/5) + 32
    print("The temperature in Fahrenheit is ", fahrenheit)
elif temp_unit.upper() == "B":
    celsius = (temp_value - 32) * 5/9
    print("The temperature in Celsius is ", celsius)
else:
    print("The unit entered is invalid.")
