# https://students.masaischool.com/assignments/38650/problems/31771/134453

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Example usage
celsius_temperature = 25
fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
print(f"{celsius_temperature} degrees Celsius is equal to {fahrenheit_temperature} degrees Fahrenheit.")

fahrenheit_temperature = 77
celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)
print(f"{fahrenheit_temperature} degrees Fahrenheit is equal to {celsius_temperature} degrees Celsius.")
