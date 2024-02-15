import random
from meals import weekly_meals
# Function to shuffle meals for each day
def shuffle_meals(weekly_meals):
    for day_meals in weekly_meals:
        meals = list(day_meals.values())
        random.shuffle(meals)
        day_meals["breakfast"], day_meals["lunch"], day_meals["dinner"] = meals
    return weekly_meals

# Print the shuffled meals for each day of the week
for i, day_meals in enumerate(weekly_meals, start=1):
    print(f"Day {i}:")
    print("Breakfast:", day_meals["breakfast"])
    print("Lunch:", day_meals["lunch"])
    print("Dinner:", day_meals["dinner"])
    print()
