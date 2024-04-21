# Preprocess de "resultats-par-niveau-burvot-t1-france-entiere.txt"

with open("resultats-par-niveau-burvot-t1-france-entiere.txt", encoding="ANSI") as f:
    lines = f.readlines()

# N°Panneau;Sexe;Nom;Prénom;Voix;% Voix/Ins;% Voix/Exp
template = "N°Panneau {};Sexe {};Nom {};Prénom {};Voix {};% Voix/Ins {};% Voix/Exp {};"
ajout = ""
for i in range(1, 12+1):
    ajout += template.format(i, i, i, i, i, i, i)

if lines[0][-1] == "\n":
    lines[0] = lines[0][:-1] # Retirer l'ancienne fin de ligne
lines[0] += ";" + ajout + "\n" # ajouter les noms de colonne manquant

with open("resultats-par-niveau-burvot-t1-france-entiere.txt", "w", encoding="ANSI") as f:
    f.writelines(lines)