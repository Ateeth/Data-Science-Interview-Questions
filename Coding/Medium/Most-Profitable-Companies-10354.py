# Question link : https://platform.stratascratch.com/coding/10354-most-profitable-companies?code_type=2

# Import your libraries
import pandas as pd

df = forbes_global_2010_2014[['company' , 'profits']]

results = df.sort_values('profits' , ascending = False).head(3)

results
