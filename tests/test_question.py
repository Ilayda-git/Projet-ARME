import sys
import os
import pytest

# Ajouter le chemin vers les modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../optimisation_militaire')))

from primal import PrimalProblem
from dual import DualProblem

@pytest.fixture
def problem_data():
    """Fixture pour les données du problème"""
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

def test_primal(problem_data):
    """Test du problème primal"""
    costs, constraints, requirements = problem_data
    primal = PrimalProblem(costs, constraints, requirements)
    lots, cost = primal.solve()

    assert lots is not None, "La solution des lots ne doit pas être nulle."
    assert cost >= 0, "Le coût total doit être positif."
    assert len(lots) == len(costs), "Le nombre de lots doit correspondre au nombre de coûts."
    print("Test primal réussi.")

def test_dual(problem_data):
    """Test du problème dual"""
    costs, constraints, requirements = problem_data
    dual = DualProblem(costs, constraints, requirements)
    prices, profit = dual.solve()

    assert prices is not None, "Les prix unitaires ne doivent pas être nuls."
    assert profit >= 0, "Le profit doit être positif."
    assert len(prices) == len(requirements), "Le nombre de prix doit correspondre au nombre d'armements."
    print("Test dual réussi.")



def test_import_modules():
    assert PrimalProblem is not None
    assert DualProblem is not None
