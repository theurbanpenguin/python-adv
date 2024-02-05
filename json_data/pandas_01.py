import pandas as pd
df = pd.read_csv('01_pop.tsv', sep='\t')
# print(df)
# print(type(df))
# print(df.shape)
# print(df.dtypes)
# print(df.info())
country_df = df['country']
print(country_df.head())
# print(df.country)
print(df.iloc[0])