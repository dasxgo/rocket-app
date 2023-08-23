import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_oil_average_curve(data1, data2 , x, y):
    plt.figure(figsize=(14,8))
    plt.yscale('log')
    plt.title("Oil - average curve")
    plt.xlabel("TotalProdMonths")
    plt.ylabel("OIL_BBL")
    plt.grid(visible=True, which='major', axis='both')
    
    sns.lineplot(data=data1, x=x, y=y, hue="WellName", palette='Greys', 
    estimator=None, n_boot=1000, lw=0.8, orient='x', sort=True, legend=None, ci='deprecated', ax=None)
    sns.lineplot(data=data2, x=x, y=y, hue=None, palette='Greys', color='C0', 
    estimator=None, n_boot=1000, lw=0.8, orient='x', sort=True, legend=None, ci='deprecated', ax=None)

    plt.legend(loc='center', bbox_to_anchor=(1.12,0.5))
    plt.show()

if __name__ == '__main__':
    # Read CSV file
    df = pd.read_csv('/home/dasxgo/dev/rocket/out/04-lss.csv')
    print(df.head(5))
    print('=' * 160)
    
    # Transform data
    max_value = df.groupby('WellName')['OIL_BBL'].max().reset_index()
    avg_max_value = np.int64(max_value['OIL_BBL'].mean())  # Calculate the average of the maximum values
    df.loc[df["TotalProdMonths"] <= 1, 'OIL_BBL'] = avg_max_value   # Assign the average to values ​​less than or equal to 1
    df = df[df['OIL_BBL'] <= avg_max_value ]  # Filter values ​​greater than average
    df_mean = df.groupby('TotalProdMonths').mean().reset_index()

    # Funtion data
    data1 = df
    data2 = df_mean
    x = 'TotalProdMonths'
    y = "OIL_BBL"
    plot_oil_average_curve(data1, data2, x, y)

