#Question - Link : https://platform.stratascratch.com/coding/10061-popularity-of-hack?code_type=2

# Import your libraries
import pandas as pd

df_merged = facebook_employees.join(facebook_hack_survey , lsuffix = 'id' , rsuffix = 'employee_id')

df_merged.groupby(['location'])['popularity'].mean().reset_index()
