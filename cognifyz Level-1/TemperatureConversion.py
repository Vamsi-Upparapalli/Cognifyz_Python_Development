def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fanrenheit - 32) * 5/9


celsius_temperature = 30
converted_to_fahrenheit = celsius_to_fahrenheit(celsius_temperature)
print(f"{celsius_temperature} celsius is equal to {converted_to_fahrenheit:.2f} fahrenheit")

fahrenheit_temperature = 86
converted_to_celsius = fahrenheit_to_celsius(fahrenheit_temperature)
print(f"{fahrenheit_temperature} fahrenheit is equal to {converted_to_celsius:.2f} celsius")ḍ