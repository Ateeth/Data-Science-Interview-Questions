# Question_Link = https://platform.stratascratch.com/coding/10353-workers-with-the-highest-salaries?code_type=2

# Import your libraries
import pandas as pd

df_merge = worker.merge(title, left_on='worker_id', right_on='worker_ref_id')

df_max_salary = df_merge[df_merge['salary'] == df_merge['salary'].max()]

result = df_max_salary['worker_title']
