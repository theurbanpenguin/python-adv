names: list = ["Vera", "Chuck","Sam", "Rob", "Joe", "Dave", "Jill"]
salaries: list = [2000, 1800, 2100, 1200, 2100, 950]

count = len(names)
print(count)

for c in range(count):
    print(f'{names[c]}: {salaries[c]}')