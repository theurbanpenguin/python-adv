from meals import weekly_meals

for day in weekly_meals:
    print(f"{day['breakfast']} : {day['lunch']} : {day['dinner']}")