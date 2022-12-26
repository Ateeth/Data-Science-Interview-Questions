# Question Link : https://platform.stratascratch.com/coding/9814-counting-instances-in-text?code_type=2

# Import your libraries
import pandas as pd
import re

gfs = google_file_store

#The below lines of code fetch out instances of rows which have bulls / bears in their content

# bull_words = gfs[gfs['contents'].str.contains(r'\bbull\b' , flags = re.I)]

# bear_words = gfs[gfs['contents'].str.contains(r'\bbear\b' , flags = re.I)] 

#The below code will create a count of how many times bull and bear occur in each row context column

#regex is used and \b is applied to beginning and end of bull and bear we are searching for as it is basically the word bounday so it specifically looks for bull , bear and not words like bullish are considered. Also the word r is used before search string to make it consider as raw text

#In the end take the sum of the columns of bull and bear and display


gfs['bull'] = gfs['contents'].apply(lambda text : len(re.findall(r'\bbull\b' , text)))

gfs['bear'] = gfs['contents'].apply(lambda text : len(re.findall(r'\bbear\b' , text)))

gfs[['bull' , 'bear']].sum().reset_index()
