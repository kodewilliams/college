def GetMilesToKilometers(num_miles):
    '''
    This function should return the miles converted to kilometers. Replace the
    line below with the correct code.
    '''
    return num_miles * 1.61


def GetPoundsToKilograms(num_pounds):
    '''
    This function should the miles converted to kilometers. Replace the line
    below with the correct code.
    '''
    return num_pounds * 0.45


def GetFahrenheitToCelsius(temp_fahrenheit):
    '''
    This function should the fahrenheit temperature converted to celsius.
    Replace the line below with the correct code.
    '''
    return (temp_fahrenheit - 32) * (5/9)


# You don't need to change anything below this line.
num_miles = float(input("Enter distance (in miles): "))
num_pounds = float(input("Enter weight (in pounds): "))
temp_fahrenheit = float(input("Enter temperature (in fahrenheit): "))

num_kilometers = GetMilesToKilometers(num_miles)
num_kilograms = GetPoundsToKilograms(num_pounds)
temp_celsius = GetFahrenheitToCelsius(temp_fahrenheit)
print('That\'s', num_kilometers, 'kilometers,', num_kilograms,
      'kilograms, and', temp_celsius,
      'celsius. Now you sound like you\'re from London!')
