import random
from meals import weekly_meals
# Function to shuffle meals for each day
def shuffle_meals(weekly_meals):
    for day_meals in weekly_meals:
        meals = list(day_meals.values())
        random.shuffle(meals)
        day_meals["breakfast"], day_meals["lunch"], day_meals["dinner"] = meals
    return weekly_meals

# Shuffle the meals for each day
weekly_meals = shuffle_meals(weekly_meals)

for day in weekly_meals:
    print(f"{day['breakfast']} : {day['lunch']} : {day['dinner']}")