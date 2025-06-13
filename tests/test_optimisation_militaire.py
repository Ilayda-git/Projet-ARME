"""
    Fichier de tests unitaires pour vérifier la généralisation du problème 
    d’optimisation linéaire à un nombre arbitraire de lots et de types d’armement.

    Ce module teste les fonctionnalités des classes définies dans 'Data/generalisation.py',
    notamment la résolution de problèmes d’optimisation avec des dimensions variables.

    Fichiers associés :
    - 'Data/generalisation_data.json' : contient des jeux de données de test (format JSON)
"""




import sys
import os
import json
import pytest
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../Optimisation_militaire')))

from generalisation import GeneralizedPrimalProblem, GeneralizedDualProblem


@pytest.fixture
def jeu_donnees():
    costs = [10, 12, 15]
    constraints = [
        [500, 300, 800],
        [1000, 2000, 1500],
        [10, 20, 15],
        [100, 80, 15],
        [80, 120, 200]
    ]
    requirements = [100000, 200000, 100, 400, 400]
    return costs, constraints, requirements


def test_resolution_primal(jeu_donnees):
    couts, contraintes, besoins = jeu_donnees
    primal = GeneralizedPrimalProblem(couts, contraintes, besoins)
    lots, cout_total = primal.solve()

    assert lots is not None
    assert cout_total > 0
    assert len(lots) == len(couts)


def test_resolution_dual(jeu_donnees):
    couts, contraintes, besoins = jeu_donnees
    dual = GeneralizedDualProblem(couts, contraintes, besoins)
    prix, profit = dual.solve()

    assert prix is not None
    assert profit > 0
    assert len(prix) == len(besoins)


def test_dualite_primal_dual(jeu_donnees):
    couts, contraintes, besoins = jeu_donnees

    primal = GeneralizedPrimalProblem(couts, contraintes, besoins)
    _, cout_total = primal.solve()

    dual = GeneralizedDualProblem(couts, contraintes, besoins)
    _, profit = dual.solve()

    assert round(cout_total, 2) == round(profit, 2), "Écart entre primal et dual"


def test_probleme_vide():
    primal = GeneralizedPrimalProblem([], [], [])
    lots, cost = primal.solve()
    assert lots is None or cost is None


def test_format_json():
    chemin = os.path.abspath(os.path.join(os.path.dirname(__file__), "../Data/generalisation_data.json"))
    assert os.path.exists(chemin), f"Fichier non trouvé : {chemin}"

    with open(chemin) as f:
        data = json.load(f)
        assert "costs" in data
        assert "constraints" in data
        assert "requirements" in data