import pandas as pd 

class EngineProfile:
    def __init__(self,name,loc,file):
        self.name = name
        self.location = loc
        self.df = self.process_file(file)
        self.stats = self.key_stats()

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

    def key_stats(self):
        return self.df.loc[self.df['GPS_Speed [mph]'] == self.df['GPS_Speed [mph]'].max()]
