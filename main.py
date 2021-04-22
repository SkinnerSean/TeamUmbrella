import pandas as pd 

read_file = pd.read_excel('C_stock_hydro_race_data.xlsx')
read_file.to_csv('data.csv')
df = pd.read_csv('data.csv')

def normalize(x):
    return x * (10**(-3))

df['RPM [rpm]'] = df[df['RPM [rpm]'] != '0,000']
df['Head Temp [°F]'] = df['Head Temp [°F]'].apply(normalize)
df['RPM [rpm]'] = df['RPM [rpm]'].apply(normalize)
df['GPS_Speed [mph]'] = df['GPS_Speed [mph]'].apply(normalize)
df['Prop Slip [% Slip]'] = df['Prop Slip [% Slip]'].apply(normalize)

print(df)