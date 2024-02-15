import random
from meals import weekly_meals
# Function to shuffle meals for each day
def shuffle_meals(weekly_meals):
    for day_meals in weekly_meals:
        meals = list(day_meals.values())
        random.shuffle(meals)
        day_meals["breakfast"], day_meals["lunch"], day_meals["dinner"] = meals
    return weekly_meals
# List of day names
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Print the shuffled meals for each day of the week with day names
for day_name, day_meals in zip(days_of_week, weekly_meals):
    print(f"{day_name}:")
    print("Breakfast:", day_meals["breakfast"])
    print("Lunch:", day_meals["lunch"])
    print("Dinner:", day_meals["dinner"])
    print()
