planets = (
    ("Mercury", 4880, 57900000),
    ("Venus", 12104, 108200000),
    ("Earth", 12742, 149600000),
    ("Mars", 6779, 227900000),
    ("Jupiter", 139822, 778300000),
    ("Saturn", 116464, 1420000000),
    ("Uranus", 50724, 2870000000),
    ("Neptune", 49244, 4500000000)
)
''' Print all planets '''
print(planets)

''' Print the second planet 
    [0] is the first planet, [1] is the second planet'''
print(planets[1])

''' Now print the distance from the sun of the 4th planet, planet[3]'''
print(planets[3][2])

''' Now format the distance as 1000s'''
distance = planets[3][2]
formatted_distance = "{:,}".format(distance)
print(formatted_distance)
