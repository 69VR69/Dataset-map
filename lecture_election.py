import pandas as pd
import numpy as np

# Lecture de "resultats-par-niveau-burvot-t1-france-entiere.txt"

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df = pd.read_csv(
    "resultats-par-niveau-burvot-t1-france-entiere.txt",
    encoding="ANSI",
    delimiter=";",
    dtype=str)

renaming = {
    "Voix": "Arthaud",
    "Voix 1": "Roussel",
    "Voix 2": "Macron",
    "Voix 3": "Lassalle",
    "Voix 4": "Le Pen",
    "Voix 5": "Zemmour",
    "Voix 6": "Mélanchon",
    "Voix 7": "Hidalgo",
    "Voix 8": "Jadot",
    "Voix 9": "Pécresse",
    "Voix 10": "Poutou",
    "Voix 11": "Dupont-Aignan"
}

df.rename(columns = renaming, inplace=True)

keep_columns = ['Code du département',
                'Inscrits',
                'Abstentions',
                'Votants',
                'Blancs',
                'Nuls',
                'Exprimés',
                'Arthaud',
                'Roussel',
                'Macron',
                'Lassalle',
                'Le Pen',
                'Zemmour',
                'Mélanchon',
                'Hidalgo',
                'Jadot',
                'Pécresse',
                'Poutou',
                'Dupont-Aignan']

df = df[keep_columns]

aaa = {'Code du département': str,
       'Inscrits': int,
        'Abstentions': int,
        'Votants': int,
        'Blancs': int,
        'Nuls': int,
        'Exprimés': int,
        'Arthaud': int,
        'Roussel': int,
        'Macron': int,
        'Lassalle': int,
        'Le Pen': int,
        'Zemmour': int,
        'Mélanchon': int,
        'Hidalgo': int,
        'Jadot': int,
        'Pécresse': int,
        'Poutou': int,
        'Dupont-Aignan': int}

df = df.astype(aaa)
df = df.groupby("Code du département")[list(df)[1:]].sum().reset_index()

df.rename(columns={"Code du département": "Code du departement"}, inplace=True)

df.to_csv("election_dataset.csv", sep=";", index=False)


# keep_columns = ['Code du département',
#                 'Libellé du département',
#                 'Code de la circonscription',
#                 'Libellé de la circonscription',
#                 'Code de la commune',
#                 'Libellé de la commune',
#                 'Code du b.vote',
#                 'Inscrits',
#                 'Abstentions',
#                 'Arthaud',
#                 'Roussel',
#                 'Macron',
#                 'Lassalle',
#                 'Le Pen',
#                 'Zemmour',
#                 'Mélanchon',
#                 'Hidalgo',
#                 'Jadot',
#                 'Pécresse',
#                 'Poutou',
#                 'Dupont-Aignan']
