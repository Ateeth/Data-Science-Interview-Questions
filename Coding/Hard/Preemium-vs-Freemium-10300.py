# Question-Link : https://platform.stratascratch.com/coding/10300-premium-vs-freemium?tabname=question&code_type=2

# Import your libraries
import pandas as pd

# Merge all dataframes
df_user = ms_user_dimension.merge(ms_acc_dimension , how = 'right')
df_all = df_user.merge(ms_download_facts , how = 'right')

# Create new columns for downlaods of paid customers and non paying customers
df_all['paid'] = df_all['downloads']
df_all['unpaid'] = df_all['downloads']

#If non paying customer make downlaods in paid column for that row as 0
df_all.loc[df_all['paying_customer'] == 'no' , 'paid'] = 0

#If paying customer make downlaods in unpaid column for that row as 0
df_all.loc[df_all['paying_customer'] == 'yes' , 'unpaid'] = 0

daily_values = df_all.groupby('date').sum().reset_index()[['date' , 'paid' , 'unpaid']]

result = daily_values[daily_values['unpaid'] > daily_values['paid']].sort_values('date' , ascending = True)

result
