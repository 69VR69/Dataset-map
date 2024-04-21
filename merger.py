import pandas as pd

# Lecture de "election-dataset.csv"
df = pd.read_csv("./election_dataset.csv", sep=";", dtype=str)

# Lecture de "./output/IREF_to_CSV.csv"
df2 = pd.read_csv("./output/IREF_to_CSV.csv", sep=";", dtype=str)

indexDf = 0
indexDf2 = 0

# Merge des deux dataframes sur la colonne index 0
df = pd.merge(
    df, df2, left_on=df.columns[indexDf], right_on=df2.columns[indexDf2], how="inner"
)

# Load the "communes-departement-region.csv"
df3 = pd.read_csv("./communes-departement-region.csv", sep=";", dtype=str, encoding="utf-8")
df3 = df3.iloc[:, 0].str.split(',', expand=True)

print(df3.columns)

# Selecting columns at indices 11, 6, and 7
selected_columns = df3.columns[[11, 5, 6]]

# Dropping columns not in the selected columns
df3 = df3[selected_columns]

# renaming columns
df3.columns = ["Code du departement", "Latitude", "Longitude"]

# transform the column "Code du departement" to always have 2 digits
df3.iloc[:, 0] = df3.iloc[:, 0].apply(lambda x: x.zfill(2))

# remove duplicates of the column "Code du departement"
df3 = df3.drop_duplicates(subset="Code du departement")
df

# log df3 head
print(df3.head())

df = pd.merge(
    df, df3, left_on=df.columns[indexDf], right_on=df3.columns[0], how="inner"
)

# Sauvegarde du dataframe dans "merged.csv"
df.to_csv("merged.csv", sep=";", index=False)
