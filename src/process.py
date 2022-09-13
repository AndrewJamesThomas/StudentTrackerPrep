import pandas as pd
FILE_NAME = "Quick Query 20220913-121846.csv"

# load data
path = "data/raw/" + FILE_NAME
df = pd.read_csv(path)

# order column appropriately
cols = ['first_name', 'middle_name', 'last_name', 'suffix', 'birthdate', 'start_search_date', 'application_id']
df = df[cols]

# correctly format all fields
df["middle_name"] = df["middle_name"].str[:1]
df["birthdate"] = pd.to_datetime(df["birthdate"]).dt.strftime("%Y%m%d")
df["start_search_date"] = pd.to_datetime(df["start_search_date"]).dt.strftime("%Y%m%d")

