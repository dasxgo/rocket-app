import pandas as pd
import numpy as np
import utils

def main():

    # Read CSV file
    df4 = pd.read_csv('/home/dasxgo/dev/rocket-app/reports/02-plan.csv')
    print(df4.head(5))
    print('-' * 160)

    # Display information about the DataFrame
    print(df4.info())

    # Check data for errors
    error_column = 'OIL_BBL'
    total_errors = df4[(df4[error_column] == 0) | (df4[error_column] < 0)].shape[0]
    print(f'Total errors in {error_column}: {total_errors}')
    print('-' * 160)

    # clean the data
    production_columns = ["OIL_BBL", "GAS_MCF", "WATER_BBL"]
    utils.clean_data(df4, production_columns)

    # Check after cleaning
    data_okay_column = 'OIL_BBL'
    total_errors_cleaned = df4[(df4[data_okay_column] == 0) | (df4[data_okay_column] < 0)].shape[0]
    print(f'Total errors in {data_okay_column} after cleaning: {total_errors_cleaned}')
    print('-' * 160)

    # Show first clean records
    print(df4.head())

    # Save the DataFrame to a CSV file
    route = '/home/dasxgo/dev/rocket-app/reports/03-clean.csv'
    df4.to_csv(route, index=False)
    print(f'DataFrame saved in {route}')
    print('-' * 160)

    # Read CSV file
    df5 = pd.read_csv('/home/dasxgo/dev/rocket-app/reports/03-clean.csv')
    print(df5.head(5))
    print('=' * 160)
    
    # Change column target - Options: OIL_BBL / GAS_MCF / WATER_BBL

    target = 'OIL_BBL'

    def reservoir(df5, reservoir):
        reservoir = df5[df5['RESERVOIR'] == reservoir]
        return reservoir[['WellName', 'TotalProdMonths', target]]
    
    # funtion for the reservoir
    df_lss = reservoir(df5, "LSS")
    print(df_lss.head())
    print('=' * 160)

    df_wsb = reservoir(df5, "WCB")
    print(df_wsb.head())
    print('=' * 160)
    
    df_wca = reservoir(df5, "WCA")
    print(df_wca.head())
    print('=' * 160)

    # Save the DataFrame to a CSV file
    route = '/home/dasxgo/dev/rocket-app/reports/04-lss.csv'
    df_lss.to_csv(route, index=False)
    print(f'DataFrame lss saved in {route}')
    print('-' * 160)

    route = '/home/dasxgo/dev/rocket-app/reports/05-wsb.csv'
    df_wsb.to_csv(route, index=False)
    print(f'DataFrame wsb saved in {route}')
    print('-' * 160)

    route = '/home/dasxgo/dev/rocket-app/reports/06-wca.csv'
    df_wca.to_csv(route, index=False)
    print(f'DataFrame wca saved in {route}')

if __name__ == '__main__':
    main()

