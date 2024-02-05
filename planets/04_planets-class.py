class Planet:
    def __init__(self, name, size, distance_from_sun):
        self.name = name
        self.size = size
        self.distance_from_sun = distance_from_sun

    def formatted_size(self):
        return "{:,.0f}".format(self.size)

    def formatted_distance(self):
        return "{:,.0f}".format(self.distance_from_sun)

    def __getitem__(self, index):
        if index < 1 or index > len(self.data):
            raise IndexError("Index out of range")
        return self.data[index - 1]

    def __str__(self):
        return (f"{self.name} - Size: {self.formatted_size()} km, "
                f"Distance from the Sun: {self.formatted_distance()} km")

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
for planet in planets:
    print(planet)