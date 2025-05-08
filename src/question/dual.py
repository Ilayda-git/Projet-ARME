from scipy.optimize import linprog
import numpy as np

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
            print("Solution optimale trouvée pour le dual.")
            print("Bénéfice total:", -result.fun)
            print("Prix unitaires:", result.x)
            return result.x, -result.fun
        else:
            print("Pas de solution optimale pour le dual.")
            return None, None
