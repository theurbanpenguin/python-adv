class Planet:
    def __init__(self, name, size, distance_from_sun):
        self.name = name
        self.size = size
        self.distance_from_sun = distance_from_sun

    def formatted_size(self):
        return "{:,.0f}".format(self.size)

    def formatted_distance(self):
        return "{:,.0f}".format(self.distance_from_sun)

    def __str__(self):
        return f"{self.name} - Size: {self.formatted_size()} km, Distance from the Sun: {self.formatted_distance()} km"

# Create instances of the Planet class for each planet
planets = [
    Planet("Mercury", 4880, 57900000),
    Planet("Venus", 12104, 108200000),
    Planet("Earth", 12742, 149600000),
    Planet("Mars", 6779, 227900000),
    Planet("Jupiter", 139822, 778300000),
    Planet("Saturn", 116464, 1420000000),
    Planet("Uranus", 50724, 2870000000),
    Planet("Neptune", 49244, 4500000000),
]

# Function to list planets alphabetically by name
def list_planets_alphabetically():
    sorted_planets = sorted(planets, key=lambda planet: planet.name)
    for planet in sorted_planets:
        print(planet.name)

# Function to list planets by size (ascending order)
def list_planets_by_size():
    sorted_planets = sorted(planets, key=lambda planet: planet.size)
    for planet in sorted_planets:
        print(planet.name)

# Function to list planets by distance from the Sun (ascending order)
def list_planets_by_distance():
    sorted_planets = sorted(planets, key=lambda planet: planet.distance_from_sun)
    for planet in sorted_planets:
        print(planet.name)

# Call the functions to display the sorted lists
print("Planets Alphabetically:")
list_planets_alphabetically()
print("\nPlanets by Size:")
list_planets_by_size()
print("\nPlanets by Distance from the Sun:")
list_planets_by_distance()
