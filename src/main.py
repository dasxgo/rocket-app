import pandas as pd
import numpy as np
import utils

def main():
    # Read CSV file
    data = pd.read_csv('/home/dasxgo/dev/rocket-app/reports/02-plan.csv')
    print(data.head(5))
    print('-' * 160)

    # Display information about the DataFrame
    print(data.info())

    # Check data for errors
    error_column = 'OIL_BBL'
    total_errors = data[(data[error_column] == 0) | (data[error_column] < 0)].shape[0]
    print(f'Total errors in {error_column}: {total_errors}')
    print('-' * 160)

    # clean the data
    production_columns = ["OIL_BBL", "GAS_MCF", "WATER_BBL"]
    utils.clean_data(data, production_columns)

    # Check after cleaning
    data_okay_column = 'OIL_BBL'
    total_errors_cleaned = data[(data[data_okay_column] == 0) | (data[data_okay_column] < 0)].shape[0]
    print(f'Total errors in {data_okay_column} after cleaning: {total_errors_cleaned}')
    print('-' * 160)

    # Show first clean records
    print(data.head())

    # Save the DataFrame to a CSV file
    route = '/home/dasxgo/dev/rocket-app/reports/03-clean.csv'
    data.to_csv(route, index=False)
    print(f'DataFrame saved in {route}')
    print('-' * 160)
    
    # Change column target - Options: OIL_BBL / GAS_MCF / WATER_BBL

    target = 'OIL_BBL'

    def reservoir(data, reservoir):
        reservoir = data[data['RESERVOIR'] == reservoir]
        return reservoir[['WellName', 'TotalProdMonths', target]]
    
    # funtion for the reservoir
    df_lss = reservoir(data, "LSS")
    print(df_lss.head())
    print('=' * 160)

    df_wsb = reservoir(data, "WCB")
    print(df_wsb.head())
    print('=' * 160)
    
    df_wca = reservoir(data, "WCA")
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

