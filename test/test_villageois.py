"""Tests unitaires pour la classe Villageois."""

from src.villageois import Villageois
from unittest.mock import patch


test_enchantements = {"Raccommodage": 1, "Tranchant": 5}


def test_initialisation_villageois():
    """Vérifie qu'un villageois naît avec les bonnes valeurs par défaut."""
    v = Villageois(test_enchantements)

    assert v.job == "libraire"
    assert v.reinitialisation == 0
    assert v.echange is None


def test_new_trade_incremente_compteur():
    """Vérifie que la méthode new_trade ajoute bien 1 à reinitialisation."""
    v = Villageois(test_enchantements)
    v.new_trade()

    assert v.reinitialisation == 1


@patch("src.villageois.random.choice")
def test_new_trade_donne_bibliotheque(mock_choice):
    """Vérifie le chemin où le villageois vend une bibliothèque."""
    mock_choice.return_value = "bibliothèque"

    v = Villageois(test_enchantements)
    v.new_trade()

    assert v.echange == "bibliothèque"


@patch("src.villageois.random.randint")
@patch("src.villageois.random.choice")
def test_new_trade_donne_livre(mock_choice, mock_randint):
    """Vérifie le chemin où le villageois vend un livre enchanté."""
    mock_choice.side_effect = ["livre enchanté", "Raccommodage"]

    mock_randint.return_value = 1

    v = Villageois(test_enchantements)
    v.new_trade()

    assert v.echange == ("Raccommodage", 1)
