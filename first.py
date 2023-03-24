# Convert Celsius to Fahrenheit
def C2F(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Convert Fahrenheit to Celsius
def F2C(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Test the functions
celsius = 30
fahrenheit = 86

print(f"{celsius} Celsius is equal to {C2F(celsius):.2f} Fahrenheit.")
print(f"{fahrenheit} Fahrenheit is equal to {F2C(fahrenheit):.2f} Celsius.")
