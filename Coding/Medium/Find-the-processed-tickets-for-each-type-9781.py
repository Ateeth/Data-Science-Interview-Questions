# Question-Link : https://platform.stratascratch.com/coding/9781-find-the-rate-of-processed-tickets-for-each-type

# Import your libraries
import pandas as pd


# To count number of occurences of each type
facebook_complaints['count'] = 1

# Convert boolean to int
facebook_complaints['processed'] = facebook_complaints['processed'].astype(int)

#To find total count and number of processed tickets of each type
filtered_df = facebook_complaints.groupby('type').sum().reset_index()

# Create processed_rate column
filtered_df['processed_rate'] = filtered_df['processed'] / filtered_df['count']

result = filtered_df[['type' , 'processed_rate']]

result

