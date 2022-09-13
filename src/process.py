import pandas as pd
FILE_NAME = "Quick Query 20220913-121846.csv"

# load data
path = "data/raw/" + FILE_NAME
df = pd.read_csv(path)

# order column appropriately
cols = ['first_name', 'middle_name', 'last_name', 'suffix', 'birthdate', 'application_id']

# change data types
