#Question Link = https://platform.stratascratch.com/coding/10322-finding-user-purchases?tabname=question

import pandas as pd
import numpy as np
import datetime

#sort values accoring to user_id and created_at
amazon_key_details = amazon_transactions.sort_values(['user_id','created_at'])

amazon_key_details['diff'] = amazon_key_details.groupby('user_id')['created_at'].diff()

result = amazon_key_details[amazon_key_details['diff'] <= pd.Timedelta(days=7)]['user_id'].unique()

result

