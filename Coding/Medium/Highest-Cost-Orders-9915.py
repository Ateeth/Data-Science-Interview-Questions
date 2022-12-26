# Question_link : https://platform.stratascratch.com/coding/9915-highest-cost-orders?via=keith&code_type=2

# Import your libraries
import pandas as pd

# First rename the cust_id column of customers
df = orders.merge(customers , left_on = 'cust_id' , right_on = 'id')
df['order_date'] = df['order_date'].dt.strftime("%Y-%m-%d")

total_df = df.groupby(['cust_id' , 'order_date' , 'first_name']).sum().reset_index()

filtered_df = total_df[(total_df['order_date'] >= '2019-02-01') & (total_df['order_date'] <= '2019-05-01')]

result = filtered_df.sort_values('total_order_cost' , ascending = False)[['first_name' , 'order_date' , 'total_order_cost']].head(1)

result
