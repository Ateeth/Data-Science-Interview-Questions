# Question_Link : import pandas as pd
import numpy as np


# Find on each date each user latest entry time
page_load_df = facebook_web_log[facebook_web_log['action'] == 'page_load']
page_load_df['day'] = page_load_df['timestamp'].dt.date
page_load_df['entry_time'] = page_load_df['timestamp'].dt.time
page_load_filtered = page_load_df.groupby(['user_id', 'day']).max().reset_index()


# Find on each date each user earliest exit time
page_exit_df = facebook_web_log[facebook_web_log['action'] == 'page_exit']
page_exit_df['day'] = page_exit_df['timestamp'].dt.date
page_exit_df['exit_time'] = page_exit_df['timestamp'].dt.time
page_exit_filtered = page_exit_df.groupby(['user_id', 'day']).min().reset_index()

# Merge the dataframes based on user_id and date
merged_df = pd.merge(page_load_filtered , page_exit_filtered , how = 'inner' , on = ['user_id' , 'day'])

# Find difference in timestamps
merged_df['difference'] = (merged_df['timestamp_y'] - merged_df['timestamp_x']) / pd.Timedelta(seconds=1)


result = merged_df[['user_id' , 'difference']]

# Find mean of difference
final_result = result.groupby('user_id').mean().reset_index()


import pandas as pd
import numpy as np


# Find on each date each user latest entry time
page_load_df = facebook_web_log[facebook_web_log['action'] == 'page_load']
page_load_df['day'] = page_load_df['timestamp'].dt.date
page_load_df['entry_time'] = page_load_df['timestamp'].dt.time
page_load_filtered = page_load_df.groupby(['user_id', 'day']).max().reset_index()


# Find on each date each user earliest exit time
page_exit_df = facebook_web_log[facebook_web_log['action'] == 'page_exit']
page_exit_df['day'] = page_exit_df['timestamp'].dt.date
page_exit_df['exit_time'] = page_exit_df['timestamp'].dt.time
page_exit_filtered = page_exit_df.groupby(['user_id', 'day']).min().reset_index()

# Merge the dataframes based on user_id and date
merged_df = pd.merge(page_load_filtered , page_exit_filtered , how = 'inner' , on = ['user_id' , 'day'])

# Find difference in timestamps
merged_df['difference'] = (merged_df['timestamp_y'] - merged_df['timestamp_x']) / pd.Timedelta(seconds=1)


result = merged_df[['user_id' , 'difference']]

# Find mean of difference
final_result = result.groupby('user_id').mean().reset_index()
