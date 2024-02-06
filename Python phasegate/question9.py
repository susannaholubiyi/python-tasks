def area_of_a_circle(radius):
	pi = 22/7
	area_of_circle = ( (pi * radius) ** 2)
	
	return area_of_circle
	
radius = float(input('Enter a radius to find the area of the circle: ') )

print(f"{area_of_a_circle(radius):.2f}")
