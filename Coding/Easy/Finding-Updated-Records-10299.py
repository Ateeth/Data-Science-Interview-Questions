# Question Link : https://platform.stratascratch.com/coding/10299-finding-updated-records?tabname=question


# Import your libraries
import pandas as pd

# Start writing code
sorted_salaries = ms_employee_salary.sort_values(['salary'] , ascending = False)

current_salaries = sorted_salaries.drop_duplicates(['id'])

result = current_salaries.sort_values(['id'])

result
