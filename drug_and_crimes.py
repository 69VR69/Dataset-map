import pandas as pd

# CSV
CSV_FILE_NAME = "./input/donnee-dep-data.gouv-2022-geographie2023-produit-le2023-07-17.csv"

def get_data_from_csv(csv):
    # Read in the data from the csv file
    data = pd.read_csv(
        csv, 
        delimiter=";"
        )
    return data

def get_column(data, column_name):
    # Get the column from the data
    column = data[column_name]
    return column

def get_unique_values(column):
    # Get the unique values from the column
    unique_values = column.unique()
    return unique_values

def get_columns(data):
    # Get the columns from the data
    columns = data.columns
    return columns

def get_rows(data, rows):
    # Get the rows from the data
    rows = data[rows]
    return rows



data = get_data_from_csv(CSV_FILE_NAME)

classe_column = get_column(data, "classe")
classe_values = get_unique_values(classe_column)

columns = get_columns(data)

unite_column = get_column(data, "unité.de.compte")
unite_values = get_unique_values(unite_column)

filtered_data = get_rows(data, ["classe", "Code.département", "faits", "POP"])

drugs = filtered_data[filtered_data["classe"] == "Trafic de stupéfiants"]


# XLSX TO CSV

XLSX_FILE_NAME = "./input/IREF_SECUR21-F11.xlsx"
RELEVENT_FIGURE = "Figure 3b"
TRANCHE_NAMES = ["0", "1", "2", "3", "4", "5"]

def get_data_from_xlsx(xlsx):
    # Read in the data from the xlsx file
    data = pd.read_excel(
        xlsx, 
        sheet_name="Figure 3b"
        )
    return data

def map_tranche(x):
    match (x):
        case "0":
            return TRANCHE_NAMES[0]
        case "(0 ; 0,9]":
            return TRANCHE_NAMES[1]
        case "(0,9 ; 1,6]":
            return TRANCHE_NAMES[2]
        case "(1,6 ; 2,7]":
            return TRANCHE_NAMES[3]
        case "(2,7 ; 4,6]":
            return TRANCHE_NAMES[4]
        case "> 4,6":
            return TRANCHE_NAMES[5]
    raise Exception("Unexpected value : " + x)



data = get_data_from_xlsx(XLSX_FILE_NAME)
selected_data = data.iloc[4:34970, 0:3]
column_names = selected_data.columns
selected_data.rename(columns={
    column_names[0]: "Code Postal", 
    column_names[1]: "Ville",
    column_names[2]: "Tranche pour 1000 habitants"
    }, 
    inplace=True)

# Tranform Code Postal to Code département
selected_data["Code Postal"] = selected_data["Code Postal"].apply(lambda x: x[:2])
selected_data.rename(columns={"Code Postal": "Code du departement"}, inplace=True)

tranches = get_unique_values(get_column(selected_data, "Tranche pour 1000 habitants"))

selected_data["Tranche pour 1000 habitants"] = selected_data["Tranche pour 1000 habitants"].apply(lambda x: map_tranche(x))

selected_data.to_csv("./output/IREF_to_CSV.csv", index=False, sep=";")