import pandas as pd

df = pd.read_csv("bestsellers.csv")

# head gets the first 5 rows of the spreadsheet
#print(df.head)

# columns gets the names of every column in the spread sheet
# print(df.columns)

# shape gets the shape of the spreadsheet or size ex: (500,10)
# print(df.shape)

# describe Gets the summary statistics for each column
# print(df.describe())