#Question_Link : https://platform.stratascratch.com/coding/10164-total-adwords-earnings?tabname=question&code_type=2

# Import your libraries
import pandas as pd

total_for_business = google_adwords_earnings.groupby(['business_type']).mean()

total_earnings= total_for_business['adwords_earnings'].tolist()

unique_business = google_adwords_earnings['business_type'].unique().tolist()



result = pd.DataFrame(
    {'business_type': unique_business,
     'adwords_earnings': total_earnings
    })

result


