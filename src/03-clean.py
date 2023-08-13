import pandas as pd
import numpy as np

def clean_data(df, columns):
    for col in columns:
        df.drop(df[(df[col] == 0) | (df[col] < 0)].index, inplace=True)

if __name__ == '__main__':
    # Read CSV file
    df = pd.read_csv('/home/dasxgo/dev/rocket/out/02-plan.csv')
    print(df.head(5))
    print('=' * 160)

    # Display information about the DataFrame
    print(df.info())
    print('=' * 160)

    # Check data for errors
    error_column = 'OIL_BBL'
    total_errors = df[(df[error_column] == 0) | (df[error_column] < 0)].shape[0]
    print(f'Total errors in {error_column}: {total_errors}')

    print('=' * 160)

    # clean the data
    production_columns = ["OIL_BBL", "GAS_MCF", "WATER_BBL"]
    clean_data(df, production_columns)

    # Check after cleaning
    data_okay_column = 'OIL_BBL'
    total_errors_cleaned = df[(df[data_okay_column] == 0) | (df[data_okay_column] < 0)].shape[0]
    print(f'Total errors in {data_okay_column} after cleaning: {total_errors_cleaned}')

    print('=' * 160)

    # Show first clean records
    print(df.head())

    # Save the DataFrame to a CSV file
    route = '/home/dasxgo/dev/rocket/out/03-clean.csv'
    df.to_csv(route, index=False)
    print(f'DataFrame saved in {route}')