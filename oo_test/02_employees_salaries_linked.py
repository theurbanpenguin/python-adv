names =["Vera", "Chuck", "Samantha", "Roberto", "Joe", "Dave", "Tina"]
salaries = [2000, 1800, 1800, 2100, 200, 2200, 2300]

count = len(names)
for c in range(count):
    print(f"{names[c]}: £{salaries[c]}")