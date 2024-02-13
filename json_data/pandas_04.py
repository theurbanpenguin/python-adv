import working_with_pandas

# Example usage:
tsv_file = "02_pop.tsv"

df = working_with_pandas.DataProcessor.create_dataframe(tsv_file)

# Generating report for all data
working_with_pandas.DataAnalyzer.print_reports(df)

# Generating report for a specific year
working_with_pandas.DataAnalyzer.print_reports(df, year=1962)
