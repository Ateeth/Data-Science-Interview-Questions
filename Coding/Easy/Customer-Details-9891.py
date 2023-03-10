#Question Link : https://platform.stratascratch.com/coding/9891-customer-details?code_type=2

# Import your libraries
import pandas as pd


#Merge the customers and orders table based on id in customers table and cust_id in order table
merged = pd.merge(customers, orders, left_on = 'id', right_on = 'cust_id', how = 'left')

result = merged[['first_name' , 'last_name' , 'city' , 'order_details']].sort_values(['first_name' , 'order_details'] , ascending = True)

result
