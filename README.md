# Simulateur d'Enchantement Minecraft

---

## Objectif du projet
Dans le jeu vidéo Minecraft, l'enchantement **"Raccommodage" (ou Mending en anglais)** est très pratique pour réparer des outils. L'obtention de ce dernier via un villageois libraire (un personnage virtuel vendant des livres enchantés) est soumise à une double contrainte aléatoire. Il y a une chance sur deux qu'il vende le bon objet (un livre enchanté) puis une chance sur 38 d'avoir l'enchantement Raccommodage sur ce livre. Tous les événements sont indépendants. 
Dans le jeu, il est possible de réinitialiser indéfiniment les objets vendus par le villageois en cassant sa station de travail (un pupitre) puis en la reposant. On cherche donc a savoir combien de de réinitialisation on doit faire avant d'avoir l'enchantement voulu. On va compter le nombre de réinitialisation qu'il faut pour un grand nombre de villageois.

Ce projet vise à modéliser mathématiquement ce système en programmation orientée objet (Python) et à réaliser une simulation (100 000 itérations) pour déterminer le nombre précis de réinitialisations nécessaires pour obtenir cet enchantement avec un **seuil de confiance de 95%**.

---

## Version de Python

- **Python :** Version **3.13.9** 

---

##  Architecture du projet
Le projet combine l'ingénierie logicielle (Python) et l'analyse statistique (R).

* **`src/villageois.py`** : Contient la classe `Villageois` modélisant l'état et le comportement stochastique du PNJ selon les règles du wiki officiel.
* **`tests/test_villageois.py`** : Contient les tests unitaires (via `pytest`) garantissant le bon fonctionnement de la classe avec une couverture de 100%.
* **`main.py`** : Script principal orchestrant la simulation sur 100 000 agents et exportant les données brutes au format CSV.
* **`requirements.txt`** : Liste des dépendances Python pour garantir la reproductibilité du projet.

##  Installation 

Pour faire fonctionner ce projet sur votre machine locale, veuillez suivre les étapes ci-dessous. Elles incluent la création d'un environnement virtuel afin d'isoler les dépendances du projet. Ces commandes sont à exécuter dans le terminal.

```bash
# 1. Cloner le dépôt 
git clone https://github.com/thomasetienne35-svg/minecraft.git

# 2. Entrer le nom du dossier du projet
cd minecraft

# 3. Créer et activer l'environnement virtuel (nommé.venv):
python3 -m venv .venv

# 4. Activer l'environnement virtuel
# - Si vous êtes sur Windows, utilisez la commande suivante à la place : .venv\Scripts\activate
source .venv/bin/activate

# 5. Installer les dépendances du projet
pip install -r requirements.txt

# 6. Exécuter la simulation :
python main.py

#Un fichier resultats_minecraft.csv sera automatiquement généré à la racine.
```

---

##  Tests

Ce projet utilise `pytest` pour les tests unitaires et garantit une **couverture de code de 100%**. 

Pour exécuter l'ensemble des tests et afficher le rapport de couverture, assurez-vous d'être dans votre environnement virtuel et lancez la commande suivante depuis la racine du projet :

```bash
python -m pytest --cov=src
```

---

## Qualité du code : Linter et Formatter

Ce projet respecte les conventions de style de code **Google**. 

Pour garantir la qualité, la propreté et l'uniformité du code, nous utilisons l'outil tout-en-un **Ruff**, qui agit à la fois comme linter et comme formatter. 

Assurez-vous d'être dans votre environnement virtuel, puis exécutez les commandes suivantes depuis la racine du projet :

**1. Pour vérifier le code (Linter) :**
```bash
python -m ruff check .
```

**2. Pour formater le code automatiquement (Formatter) :**
```bash
python -m ruff format .
```