# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Celsius to Kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273.15

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Function to convert Fahrenheit to Kelvin
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

# Function to convert Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Function to convert Kelvin to Fahrenheit
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Main Program

# Prompting the user to input the temperature value
temperature = float(input("Enter the temperature value: "))
# Prompting the user to input the unit of measurement
unit = input("Enter the unit of measurement (Celsius, Fahrenheit, or Kelvin): ").lower()
# Depending on the unit of measurement provided by the user, convert the temperature to the other two units
if unit == 'celsius':
    fahrenheit = celsius_to_fahrenheit(temperature)
    kelvin = celsius_to_kelvin(temperature)
    print(f"{temperature} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit and {kelvin:.2f} Kelvin.")
elif unit == 'fahrenheit':
    celsius = fahrenheit_to_celsius(temperature)
    kelvin = fahrenheit_to_kelvin(temperature)
    print(f"{temperature} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius and {kelvin:.2f} Kelvin.")
elif unit == 'kelvin':
    celsius = kelvin_to_celsius(temperature)
    fahrenheit = kelvin_to_fahrenheit(temperature)
    print(f"{temperature} Kelvin is equal to {celsius:.2f} degrees Celsius and {fahrenheit:.2f} Fahrenheit.")
else:
    print("Invalid unit of measurement. Please enter Celsius, Fahrenheit, or Kelvin.")