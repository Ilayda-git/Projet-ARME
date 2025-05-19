from scipy.optimize import linprog
import numpy as np

class PrimalProblem:
    def __init__(self, costs, constraints, requirements):
        """
        Initialise le problème primal avec les coûts, les contraintes et les besoins.
        """
        self.costs = costs
        self.constraints = [[-c for c in row] for row in constraints]
        self.requirements = [-r for r in requirements]

    def solve(self):
        """
        Résout le problème d'optimisation linéaire.
        """
        result = linprog(c=self.costs, A_ub=self.constraints, b_ub=self.requirements, method='highs')
        if result.success:
            return result.x, result.fun
        else:
            print("Pas de solution optimale.")
            return None, None
        


class DualProblem:
    def __init__(self, costs, constraints, requirements):
        """
        Initialise le problème dual avec les coûts, les contraintes et les besoins.
        """
        self.costs = [-r for r in requirements]
        self.constraints = np.transpose(constraints)
        self.requirements = costs

    def solve(self):
        """
        Résout le problème dual pour maximiser le bénéfice.
        """
        result = linprog(c=self.costs, A_ub=self.constraints, b_ub=self.requirements, method='highs')
        if result.success:
            return result.x, -result.fun
        else:
            print("Pas de solution optimale pour le dual.")
            return None, None