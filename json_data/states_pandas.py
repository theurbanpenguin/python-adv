import json
import pandas as pd
json_file = "states_data.json"
with open(json_file, 'r') as file:
    data = json.load(file)
df = pd.DataFrame(data)
print(df.head())
high_population_states = df[df['Population'] > 5000000]
print(high_population_states)
df_sorted = df.sort_values(by='Population', ascending=True)
print(df_sorted)
total_population = df['Population'].sum()
print("Total Population:", total_population)
state_with_highest_population = df[df['Population'] == df['Population'].max()]
print(state_with_highest_population)

