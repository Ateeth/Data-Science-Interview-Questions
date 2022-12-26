# Question-Link : https://platform.stratascratch.com/coding/10156-number-of-units-per-nationality?tabname=question

# Import your libraries
import pandas as pd

airbnb_hosts = airbnb_hosts.drop_duplicates()

airbnb_hosts_merged = airbnb_hosts.merge(airbnb_units , how = 'left')
airbnb_hosts_under30 = airbnb_hosts_merged[airbnb_hosts_merged['age'] < 30]


airbnb_hosts_apartment = airbnb_hosts_under30[airbnb_hosts_under30['unit_type'] == 'Apartment']


airbnb_hosts_apartment['count'] = 1
filtered_df = airbnb_hosts_apartment.groupby('nationality').sum().reset_index()

result = filtered_df[['nationality' , 'count']].sort_values('count' , ascending = False)
