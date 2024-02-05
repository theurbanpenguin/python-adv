import pandas as pd

# Assuming you have the data in a TSV file (tab-separated values)
tsv_file = "02_pop.tsv"

# Read the TSV file into a DataFrame
df = pd.read_csv(tsv_file, sep='\t')

# Group by the "continent" column and calculate the mean of "lifeExp"
continent_lifeexp_mean = df.groupby('continent')['lifeExp'].mean()
sorted_continent_lifeexp = continent_lifeexp_mean.sort_values(ascending=False)
# Display the result
print(sorted_continent_lifeexp)
# Filter the data for the year 1952
df_1952 = df.loc[df['year'] == 1952]

# Group by the "continent" column and calculate the mean of "lifeExp"
continent_lifeexp_mean = df_1952.groupby('continent')['lifeExp'].mean()

# Sort the result by mean life expectancy in descending order
sorted_continent_lifeexp = continent_lifeexp_mean.sort_values(ascending=False)

# Display the sorted result
print(sorted_continent_lifeexp)
