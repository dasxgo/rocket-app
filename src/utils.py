import pandas as pd
import numpy as np
import load

df = load.df

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

def clean_data(df4, columns):
    for col in columns:
        df4.drop(df4[(df4[col] == 0) | (df4[col] < 0)].index, inplace=True)

if __name__ == '__main__':
    print(df.head(5))

    well_planned = 5000
    df = production_values(df, well_planned)
    print(df.head())
    
    # Save the DataFrame to a CSV file
    route = '/home/dasxgo/dev/rocket-app/reports/02-plan.csv'
    df.to_csv(route, index=False)  
    print(f'DataFrame save in {route}')




