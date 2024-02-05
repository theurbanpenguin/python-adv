class CustomIndexList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        if index < 1 or index > len(self.data):
            raise IndexError("Index out of range")
        return self.data[index - 1]
if __name__ == '__main__':
     planets = CustomIndexList([
        {"name": "Mercury", "size": 4880, "distance_from_sun": 57900000},
        {"name": "Venus", "size": 12104, "distance_from_sun": 108200000},
        {"name": "Earth", "size": 12742, "distance_from_sun": 149600000},
        {"name": "Mars", "size": 6779, "distance_from_sun": 227900000},
        {"name": "Jupiter", "size": 139822, "distance_from_sun": 778300000},
        {"name": "Saturn", "size": 116464, "distance_from_sun": 1420000000},
        {"name": "Uranus", "size": 50724, "distance_from_sun": 2870000000},
        {"name": "Neptune", "size": 49244, "distance_from_sun": 4500000000},
     ])
     print(planets[1])