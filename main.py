import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Vérifie si la variable existe
if "DISPLAY" in os.environ:
    print(f"Succès ! Variable DISPLAY détectée : {os.environ['DISPLAY']}")
else:
    print("Erreur : La variable DISPLAY est introuvable.")
    
df = pd.read_csv('data.csv')

df = df.dropna()


sns.histplot(df['age'])

plt.show()

