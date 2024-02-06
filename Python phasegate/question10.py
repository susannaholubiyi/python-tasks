def convert_from_celcius_to_fahrenheit(temperature_in_celcius):

	temperature_in_fahrenheit = ( ( temperature_in_celcius * (9/5) ) + 32 )
	
	return temperature_in_fahrenheit
	
temperature_in_celcius = float(input("Enter the temperature in celcius to convert it to fahrenheit: "))

print(convert_from_celcius_to_fahrenheit(temperature_in_celcius))
