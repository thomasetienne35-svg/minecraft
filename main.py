"""Instancie 100 000 villageois virtuels et exporte le nombre de réinitialisations en CSV."""

import pandas as pd

from src.villageois import Villageois
from src.villageois import enchantements

nombre_villageois = 100000
nombre_reinitialisation = []

for i in range(100000):
    nouveau_villageois = Villageois(enchantements)
    while nouveau_villageois.echange != ("Raccommodage", 1):
        nouveau_villageois.new_trade()
    nombre_reinitialisation.append(nouveau_villageois.reinitialisation)

df = pd.DataFrame({"tentatives": nombre_reinitialisation})

df.to_csv("resultats_minecraft.csv", index=False)