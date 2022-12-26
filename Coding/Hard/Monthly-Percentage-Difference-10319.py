#Question_link : https://platform.stratascratch.com/coding/10319-monthly-percentage-difference?tabname=question&code_type=2

# Import your libraries
import pandas as pd

# Start writing code
#All year is same in the table
# Create month column , group by month , sum revenue
sf_transactions['month'] = sf_transactions['created_at'].dt.month
dates_formatted = sf_transactions['created_at'].dt.strftime('%Y-%m')
sf_transactions['date'] = dates_formatted

monthly_revenue = sf_transactions.groupby(['date']).sum().reset_index()[['date' , 'value']].sort_values('date')


#Take difference in monthly revenue
monthly_revenue['value_difference'] = monthly_revenue['value'].diff()

#Create a column for last month diff which can find via month revenue - value difference

monthly_revenue['last_month_revenue'] = monthly_revenue['value'] - monthly_revenue['value_difference']

monthly_revenue['percentage_change'] = (monthly_revenue['value_difference'] / monthly_revenue['last_month_revenue']) * 100

# results = monthly_revenues_sorted[['date_formatted' , 'percentage_change']]
monthly_revenue['percentage_change'] = monthly_revenue['percentage_change'].round(2)

result = monthly_revenue[['date' , 'percentage_change']]

result
