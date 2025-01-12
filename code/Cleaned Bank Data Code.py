import pandas as pd
import numpy as np

#import ["bank_marketing.csv"] file
#Making DataFrame
bm = pd.read_csv("bank_marketing.csv")

#[Client.csv]
client = bm[["client_id", "age", "job", "marital", "education", "credit_default", "mortgage"]]

#cleaning_client
client["education"] = client["education"].str.replace('.','_')
client["education"] = client["education"].replace("unknown",np.nan)
client["job"] = client["education"].str.replace('.','_')

for col in ["credit_default", "mortgage"]:
    client[col] = client[col].map({'yes' : 1,'no' : 0, 'unknown': 0}).astype(bool)
    
#[Campaign.csv]
campaign = bm[["client_id", "number_contacts", "contact_duration", "previous_campaign_contacts", "previous_outcome", "campaign_outcome", "month", "day"]]


#Cleaning_campaign : choose options ;} ; giving same result

#Option: 1
for col in ["campaign_outcome","previous_outcome"]:
    campaign[col] = campaign[col].map({'yes' : 1,'no' : 0, 'success' : 1, 'failure': 0, 'nonexistent': 0}).astype(bool)
    
#Option: 2 
#campaign["campaign_outcome"] = campaign["campaign_outcome"].map({"yes" : 1,"no": 0}).astype(bool)
#campaign["previous_outcome"] = campaign["previous_outcome"].map({"success" : 1,"failure": 0,"nonexistent": 0}).astype(bool)

#creating new column
campaign["year"] = "2022"
campaign["day"] = campaign["day"].astype(str)
campaign["last_contact_date"] = campaign["year"] + '-' + campaign["month"] + '-' + campaign["day"]
campaign["last_contact_date"] = pd.to_datetime(campaign["last_contact_date"], format = "%Y-%b-%d" )

#deleting columns
for col in ["year" , "month" , "day"]:
    campaign.drop(columns = col, inplace = True)

#[Economics.csv]
economics = bm[["client_id", "cons_price_idx", "euribor_three_months"]]


#Saving data
client.to_csv("client.csv", index = False)
campaign.to_csv("campaign.csv", index = False)
economics.to_csv("economics.csv", index = False)
