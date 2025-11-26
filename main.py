import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# age
# taille
# poids
# revenu_estime_mois
# historique_credits
# risque_personnel
# score_credit
# loyer_mensuel
# montant_pret


df = pd.read_csv("data.csv")

print("Fichier brut : ",  len(df.index))

# # Boxplot pour détecter les outliers dans les revenus
# sns.boxplot(x=df["score_credit"])
# plt.show()

# Supprimer les doublons (absents)
df = df.drop_duplicates()
print("Suppression doublons : ",  len(df.index))


print("Total des valeurs manquantes par colonne")
print(df.isnull().sum())

# Ajouter une colonne pour stocker le total des valeurs manquantes de chaque ligne
df["manquants"] = df.isnull().sum(axis=1)

df = df[df['manquants'] < 2]

print("Conservation des lignes ayant moins de 2 colonnes vides : ",  len(df.index))

# Filtrer les outliers (par exemple, couper les revenus à plus de 3 fois l'écart interquartile)
Q1 = df["revenu_estime_mois"].quantile(0.25)
Q3 = df["revenu_estime_mois"].quantile(0.75)
IQR = Q3 - Q1
df = df[(df["revenu_estime_mois"] >= (Q1 - 1.5 * IQR)) & (df["revenu_estime_mois"] <= (Q3 + 1.5 * IQR))]

print("Elimination des outliers de revenus mensuels : ",  len(df.index))

# Filtrer les outliers (par exemple, couper les socre crédit à plus de 3 fois l'écart interquartile)
Q1 = df["score_credit"].quantile(0.25)
Q3 = df["score_credit"].quantile(0.75)
IQR = Q3 - Q1
df = df[(df["score_credit"] >= (Q1 - 1.5 * IQR)) & (df["score_credit"] <= (Q3 + 1.5 * IQR))]

print("Elimination des outliers de score de crédit : ",  len(df.index))

print("Total des valeurs manquantes par colonne après filtrage")
print(df.isnull().sum())

# Remplacer les valeurs manquantes par la moyenne de la colonne
df["loyer_mensuel"].fillna(df["loyer_mensuel"].mean(), inplace=True)
df["score_credit"].fillna(df["score_credit"].mean(), inplace=True)
df["historique_credits"].fillna(df["historique_credits"].mean(), inplace=True)

df = df.dropna()

print("Elimination des lignes vides (ne doit rien changer) : ",  len(df.index))

df.to_csv("data_cleaned.csv")
