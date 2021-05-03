import pandas as pd 
import numpy as np

class EngineProfile:
    def __init__(self,loc,file): # name is set in users
        self.location = loc
        self.stats = self.key_stats(file)
        print('fuck you')

    def process_file(self,excel_file):
        read_file = pd.read_excel(excel_file)
        read_file.to_csv('../resources/data.csv')
        df = pd.read_csv('../resources/data.csv', index_col=1)
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        def normalize(x):
            if isinstance(x,str):
                x = 0
            return x * (10**(-3))
        df['Head Temp [°F]'] = df['Head Temp [°F]'].apply(normalize)
        df['RPM [rpm]'] = df['RPM [rpm]'].apply(normalize)
        df['GPS_Speed [mph]'] = df['GPS_Speed [mph]'].apply(normalize)
        df['Prop Slip [% Slip]'] = df['Prop Slip [% Slip]'].apply(normalize)
        return df

    def key_stats(self,file):
        max_entry = {}
        df = self.process_file(file)
        df = df.loc[df['GPS_Speed [mph]'] == df['GPS_Speed [mph]'].max()]
        max_entry['time_min'] = int(df['Time (s)'])
        max_entry['head_temp'] = float(df['Head Temp [°F]'])
        max_entry['rpm'] = float(df['RPM [rpm]'])
        max_entry['speed_mph'] = float(df['GPS_Speed [mph]'])
        max_entry['pro_slip'] = float(df['Prop Slip [% Slip]'])
        return max_entry

