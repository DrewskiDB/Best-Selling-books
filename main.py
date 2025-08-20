import pandas as pd

#df = pd.read_csv("bestsellers.csv")

# head gets the first 5 rows of the spreadsheet
# print(df.head)

# shape gets the shape of the spreadsheet or size ex: (500,10)
# print(df.shape)

# columns gets the names of every column in the spread sheet
# print(df.columns)

# describe Gets the summary statistics for each column
# print(df.describe())

def df_into_dict(csv):
    df = pd.read_csv(csv)
    df_sections = df.drop_duplicates(subset= ['Name', "Author"], keep= 'first')
    #for i in df_sections_dict:
    #    print(i)

    df_sections.rename(columns= {"Name": "Title", "Year":"Publication Year", "User Rating": "Rating"},inplace= True)
    df_dict = df_sections.to_dict(orient= "records")

    for row in df_dict:
        print(row)

