import sys
import os
import pytest
import numpy as np

# Ajouter le chemin vers le dossier src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from optimisation_militaire.generalisation import GeneralizedPrimalProblem, GeneralizedDualProblem

@pytest.fixture
def simple_problem():
    """Fixture d'un problème simple de test"""
    costs = [10, 12, 15]
    constraints = [
        [100, 200, 150],   # Fusils
        [50, 60, 55],      # Grenades
        [20, 30, 25]       # Chars
    ]
    requirements = [4000, 2500, 900]
    return costs, constraints, requirements

def test_generalized_primal_solution(simple_problem):
    """Test que le problème primal généralisé retourne une solution valide"""
    costs, constraints, requirements = simple_problem
    primal = GeneralizedPrimalProblem(costs, constraints, requirements)
    solution, cost = primal.solve()

    assert solution is not None, "La solution doit exister"
    assert len(solution) == len(costs), "La taille de la solution doit correspondre au nombre de lots"
    assert cost >= 0, "Le coût doit être positif"
    print(f"Solution primal OK : coût = {cost}")

def test_generalized_dual_solution(simple_problem):
    """Test que le problème dual généralisé retourne une solution valide"""
    costs, constraints, requirements = simple_problem
    dual = GeneralizedDualProblem(costs, constraints, requirements)
    prices, profit = dual.solve()

    assert prices is not None, "La solution duale doit exister"
    assert len(prices) == len(requirements), "Nombre de prix = nombre de contraintes"
    assert profit >= 0, "Le profit doit être positif"
    print(f"Solution duale OK : profit = {profit}")

def test_strong_duality(simple_problem):
    """Vérifie que le coût primal = profit dual (dualité forte)"""
    costs, constraints, requirements = simple_problem
    primal = GeneralizedPrimalProblem(costs, constraints, requirements)
    lots, cost = primal.solve()

    dual = GeneralizedDualProblem(costs, constraints, requirements)
    prices, profit = dual.solve()

    assert abs(cost - profit) < 1e-4, f"Dualité violée : coût={cost}, profit={profit}"
    print("Dualité forte vérifiée")

def test_random_problem():
    """Génère un problème aléatoire et vérifie qu'une solution est trouvée"""
    np.random.seed(42)
    n_lots = 5
    m_constraints = 3
    costs = np.random.randint(5, 20, size=n_lots).tolist()
    constraints = [np.random.randint(20, 100, size=n_lots).tolist() for _ in range(m_constraints)]
    requirements = [int(sum(row) * 0.6) for row in constraints]

    primal = GeneralizedPrimalProblem(costs, constraints, requirements)
    lots, cost = primal.solve()
    assert lots is not None, "Problème aléatoire - primal doit donner une solution"

    dual = GeneralizedDualProblem(costs, constraints, requirements)
    prices, profit = dual.solve()
    assert prices is not None, "Problème aléatoire - dual doit donner une solution"

    assert abs(cost - profit) < 1e-4, "Dualité forte non respectée"
    print("Test aléatoire OK avec dualité forte")
