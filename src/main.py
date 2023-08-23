import pandas as pd
import numpy as np
import utils

# Read CSV file
df = pd.read_csv('/home/dasxgo/dev/rocket/out/02-plan.csv')
print(df.head(5))
print('-' * 160)

# Display information about the DataFrame
print(df.info())

# Check data for errors
error_column = 'OIL_BBL'
total_errors = df[(df[error_column] == 0) | (df[error_column] < 0)].shape[0]
print(f'Total errors in {error_column}: {total_errors}')
print('-' * 160)

# clean the data
production_columns = ["OIL_BBL", "GAS_MCF", "WATER_BBL"]
utils.clean_data(df, production_columns)

# Check after cleaning
data_okay_column = 'OIL_BBL'
total_errors_cleaned = df[(df[data_okay_column] == 0) | (df[data_okay_column] < 0)].shape[0]
print(f'Total errors in {data_okay_column} after cleaning: {total_errors_cleaned}')

print('-' * 160)

# Show first clean records
print(df.head())

# Save the DataFrame to a CSV file
route = '/home/dasxgo/dev/rocket/reports/03-clean.csv'
df.to_csv(route, index=False)
print(f'DataFrame saved in {route}')
print('-' * 160)

def main():
    # Read CSV file
    df2 = pd.read_csv('/home/dasxgo/dev/rocket/out/03-clean.csv')
    print(df2.head(5))
    print('=' * 160)
    
    # Change column target - Options: OIL_BBL / GAS_MCF / WATER_BBL

    target = 'OIL_BBL'

    def reservoir(df2, reservoir):
        reservoir = df2[df2['RESERVOIR'] == reservoir]
        return reservoir[['WellName', 'TotalProdMonths', target]]
    
    # funtion for the reservoir
    df_lss = reservoir(df2, "LSS")
    print(df_lss.head())
    print('=' * 160)

    df_wsb = reservoir(df2, "WCB")
    print(df_wsb.head())
    print('=' * 160)
    
    df_wca = reservoir(df2, "WCA")
    print(df_wca.head())
    print('=' * 160)

    # Save the DataFrame to a CSV file
    route = '/home/dasxgo/dev/rocket/out/04-lss.csv'
    df_lss.to_csv(route, index=False)
    print(f'DataFrame lss saved in {route}')

    route = '/home/dasxgo/dev/rocket/out/05-wsb.csv'
    df_wsb.to_csv(route, index=False)
    print(f'DataFrame wsb saved in {route}')

    route = '/home/dasxgo/dev/rocket/out/06-wca.csv'
    df_wca.to_csv(route, index=False)
    print(f'DataFrame wca saved in {route}')

if __name__ == '__main__':
    main()

