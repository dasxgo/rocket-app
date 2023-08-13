import pandas as pd
import numpy as np

if __name__ == '__main__':
    # Read CSV file
    df = pd.read_csv('/home/dasxgo/dev/rocket/out/03-clean.csv')
    print(df.head(5))
    print('=' * 160)
    
    # Change column target - Options: OIL_BBL / GAS_MCF / WATER_BBL

    target = 'OIL_BBL'

    def reservoir(df, reservoir):
        reservoir = df[df['RESERVOIR'] == reservoir]
        return reservoir[['WellName', 'TotalProdMonths', target]]
    
    # funtion for the reservoir
    df_lss = reservoir(df, "LSS")
    print(df_lss.head())
    print('=' * 160)

    df_wsb = reservoir(df, "WCB")
    print(df_wsb.head())
    print('=' * 160)
    
    df_wca = reservoir(df, "WCA")
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

