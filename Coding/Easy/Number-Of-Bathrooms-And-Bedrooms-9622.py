# Question_link = https://platform.stratascratch.com/coding/9622-number-of-bathrooms-and-bedrooms?tabname=question 

# Import your libraries
import pandas as pd

# Start writing code
airbnb_key_details = airbnb_search_details[['city' , 'property_type' , 'bathrooms' , 'bedrooms']]

airbnb_averages = airbnb_key_details.groupby(['city' , 'property_type']).mean().reset_index()

airbnb_averages
