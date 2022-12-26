# Question Link : https://platform.stratascratch.com/coding/9782-customer-revenue-in-march?code_type=2

# Import your libraries
import pandas as pd

# Filter March 2019 , Groupby CustomerID , Sum

#Create new column for year and month
orders['order_year'] = orders['order_date'].dt.year
orders['order_month'] = orders['order_date'].dt.month

# Fetch orders made in march 2019
orders_march_2019 = orders[(orders['order_month'] == 3) & (orders['order_year'] == 2019)]

# Fetch the important columns needed
order_march_2019_key_details = orders_march_2019[['cust_id','total_order_cost']]

#Find total order cost of each customer by grouping by cust_id
result = order_march_2019_key_details.groupby(['cust_id'])['total_order_cost'].sum().reset_index()

result
