import pandas as pd
import numpy as np

if __name__ == '__main__':
    
    field = 'IDARADO2'

    # WCA file

    df1 = pd.read_csv('/home/dasxgo/dev/rocket/data/WCA_2.csv')
    data_major = 'OIL'
    data_reservoir = 'WCA'
    df1.insert(0, 'FIELD', field) 
    df1.insert(1, 'MAJOR', data_major)
    df1.insert(2, 'RESERVOIR', data_reservoir)
    print(df1.head())
    print('='*64)

    # WCB file

    df2 = pd.read_csv('/home/dasxgo/dev/rocket/data/WCB_2.csv')
    data_major = 'OIL'
    data_reservoir = 'WCB'
    df2.insert(0, 'FIELD', field) 
    df2.insert(1, 'MAJOR', data_major)
    df2.insert(2, 'RESERVOIR', data_reservoir)
    print(df2.head())
    print('='*64)


    # LSS file

    df3 = pd.read_csv('/home/dasxgo/dev/rocket/data/LSS_2.csv')
    data_major = 'OIL'
    data_reservoir = 'LSS'
    df3.insert(0, 'FIELD', field) 
    df3.insert(1, 'MAJOR', data_major)
    df3.insert(2, 'RESERVOIR', data_reservoir)
    print(df3.head())
    print('='*64)
    
    # DataFrame
    
    df = pd.concat([df1,df2,df3], ignore_index=True)
    df['ProducingMonth'] = pd.to_datetime(df['ProducingMonth'])
    print(df.head())

    # Save the DataFrame to a CSV file

    route = '/home/dasxgo/dev/rocket/data/df.csv'
    df.to_csv(route, index=False)  
    print(f'DataFrame save in {route}')









