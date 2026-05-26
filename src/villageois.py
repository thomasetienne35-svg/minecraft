"""Module contenant la classe Villageois et la mécanique de tirage aléatoire des enchantements."""

import random

enchantements = {
    "Affilage": 3,
    "Affinité aquatique": 1,
    "Agilité aquatique": 3, 
    "Apnée": 3,
    "Appât": 3,
    "Aura de feu": 2,
    "Butin": 3,
    "Canalisation": 1,
    "Chance de la mer": 3,
    "Charge rapide": 3,
    "Châtiment": 5,
    "Chute amortie": 4,
    "Efficacité": 5,
    "Empalement": 5,
    "Épines": 3,
    "Fendage": 3,
    "Flamme": 1,
    "Fléau des arthropodes": 5,
    "Fortune": 3,
    "Frappe": 2,
    "Impulsion": 3,
    "Infinité": 1,
    "Loyauté": 3,
    "Malédiction de disparition": 1,
    "Malédiction du lien éternel": 1,
    "Perforation": 4,
    "Protection": 4	,
    "Protection contre le feu": 4,
    "Protection contre les explosions": 4,
    "Protection contre les projectiles": 4,
    "Puissance": 5,
    "Raccommodage": 1, #c'est l'enchantement qui nous intéresse
    "Recul": 2,
    "Semelles givrantes": 2,
    "Solidité": 3,
    "Tir multiple": 1,
    "Toucher de soie": 1,
    "Tranchant": 5
}

class Villageois:
    """Création d'un villageois libraire."""
    def __init__(self, enchantements: dict) -> None:
        """Initialise un nouveau villageois libraire.

        Parameters
        ----------
        enchantements : dict
            Un dictionnaire contenant les noms des enchantements en clés et leur niveau maximal en valeurs.
        """
        self.job: str = "libraire"
        self.echange: str | tuple[str, int] | None = None
        self.reinitialisation: int = 0
        self.enchantements: dict[str, int] = enchantements
    
    def new_trade(self) -> None:
        """Simulation d'un nouvel échange proposer par un villageois libraire."""
        self.reinitialisation = self.reinitialisation + 1
        
        sell = ["bibliothèque", "livre enchanté"]
        if random.choice(sell) == "bibliothèque":
            self.echange = "bibliothèque"
        else:
            ench_choisi = random.choice(list(self.enchantements.keys()))
            niveau_ench = random.randint(1, self.enchantements[ench_choisi])
            self.echange = (ench_choisi, niveau_ench)