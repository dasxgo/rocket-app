import pandas as pd
import numpy as np

def clean_data(df, columns):
    for col in columns:
        df.drop(df[(df[col] == 0) | (df[col] < 0)].index, inplace=True)


def production_values(df, well_planned):
    production_columns = ['LiquidsProd_BBL', 'GasProd_MCF', 'WaterProd_BBL']
    production_data = {}

    for column in production_columns:
        data = df[column] * (well_planned / df['LateralLength_FT']) * (30.4 / df['ProducingDays'])
        production_data[column] = data

    df[['OIL_BBL', 'GAS_MCF', 'WATER_BBL']] = pd.DataFrame(production_data)

    # Convert columns to int64
    for column in production_columns:
        df[column] = df[column].astype(np.int64)

    return df

if __name__ == '__main__':
    df = pd.read_csv('/home/dasxgo/dev/rocket/out/01-df.csv')
    print(df.head(5))

    well_planned = 5000
    df = production_values(df, well_planned)
    print(df.head())

# Save the DataFrame to a CSV file
    route = '/home/dasxgo/dev/rocket/out/02-plan.csv'
    df.to_csv(route, index=False)  
    print(f'DataFrame save in {route}')




