#Question_Link : https://platform.stratascratch.com/coding/10164-total-adwords-earnings?tabname=question&code_type=2

# Import your libraries
import pandas as pd

google_key_details = google_adwords_earnings[['business_type' , 'adwords_earnings']]

business_earnings = google_key_details.groupby('business_type').sum().reset_index()

business_earnings




