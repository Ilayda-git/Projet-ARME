"""
    Fichier de tests unitaires pour valider les classes PrimalProblem et DualProblem
    définies dans le module 'Resolution/question.py'.

    Ce fichier utilise la bibliothèque 'pytest' pour exécuter automatiquement une
    série de vérifications (problème primal et problème dual).
"""




import sys
import os
import pytest
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../Resolution')))

from question import PrimalProblem
from question import DualProblem

@pytest.fixture
def donnees_probleme():
    """
    Donne les données du problème d'optimisation pour les tests.

    Retourne :
        tuple: (coûts, contraintes, besoins)
    """
    couts = [10_000_000, 12_000_000, 15_000_000]
    contraintes = [
        [500, 300, 800],
        [1000, 2000, 1500],
        [10, 20, 15],
        [100, 80, 15],
        [80, 120, 200]
        ]
    
    besoins = [100_000, 200_000, 100, 400, 400]
    return couts, contraintes, besoins


def test_cout_total_primal(donnees_probleme):
    """
    Vérifie que le coût obtenu est positif ou nul.
    """
    couts, contraintes, besoins = donnees_probleme
    primal = PrimalProblem(couts, contraintes, besoins)
    _,cout_total = primal.solve()
    
    assert cout_total >= 0, "Le coût total doit être positif."


def test_longueur_solution_duale(donnees_probleme):
    """
    Vérifie que le vecteur de prix du dual correspond au nombre d'armements.
    """
    couts, contraintes, besoins = donnees_probleme
    dual = DualProblem(couts, contraintes, besoins)
    prix, _ = dual.solve()

    assert prix is not None
    assert len(prix) == len(besoins), "Dimension incorrecte des prix du dual."


def test_egalite_dualite(donnees_probleme):
    """
    Vérifie que le coût du primal est égal au bénéfice du dual (dualité forte).
    """
    couts, contraintes, besoins = donnees_probleme
    primal = PrimalProblem(couts, contraintes, besoins)
    dual = DualProblem(couts, contraintes, besoins)

    _, cout_total = primal.solve()
    _, benefice_total = dual.solve()

    assert pytest.approx(cout_total, rel=1e-5) == benefice_total, "Écart de dualité non nul."


def test_import_modules():
    """
    Vérifie que les classes PrimalProblem et DualProblem sont bien importées.
    """
    assert PrimalProblem is not None
    assert DualProblem is not None