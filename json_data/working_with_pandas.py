# Module for pandas SOLID demo

import pandas as pd


class DataProcessor:
    @staticmethod
    def create_dataframe(tsv_file):
        return pd.read_csv(tsv_file, sep='\t')


class DataAnalyzer:
    @staticmethod
    def sort_by_mean_life_expectancy(continent_lifeexp_mean):
        return continent_lifeexp_mean.sort_values(ascending=False)

    @staticmethod
    def print_reports(df, year=None):
        if year:
            df = df.loc[df['year'] == year]
        continent_lifeexp_mean = df.groupby('continent')['lifeExp'].mean()
        sorted_continent_lifeexp = DataAnalyzer.sort_by_mean_life_expectancy(continent_lifeexp_mean)
        print("Mean life expectancy by continent:")
        print(sorted_continent_lifeexp)
