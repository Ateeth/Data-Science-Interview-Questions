# Question Link : https://platform.stratascratch.com/coding/10064-highest-energy-consumption?tabname=question

# Import your libraries
import pandas as pd

df = pd.concat([fb_eu_energy, fb_asia_energy, fb_na_energy])

df_filtered = df.groupby('date').sum().reset_index()

result = df_filtered[df_filtered['consumption'] == df_filtered['consumption'].max()]
