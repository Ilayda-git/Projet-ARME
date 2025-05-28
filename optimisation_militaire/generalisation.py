from scipy.optimize import linprog
import numpy as np

class GeneralizedPrimalProblem:
    def __init__(self, costs, constraints, requirements):
        self.costs = costs
        self.constraints = [[-c for c in row] for row in constraints]
        self.requirements = [-r for r in requirements]

    def solve(self):
        result = linprog(c=self.costs, A_ub=self.constraints, b_ub=self.requirements, method='highs')
        if result.success:
            return result.x, result.fun
        else:
            print("Aucune solution optimale trouvée (primal).")
            return None, None

class GeneralizedDualProblem:
    def __init__(self, costs, constraints, requirements):
        # Maximiser requirements^T * y ⇔ Minimiser -requirements^T * y
        self.costs = [-r for r in requirements]

        # Transpose et corrige les signes : A_dual = A_primal^T
        A_dual = np.transpose(constraints)
        self.constraints = [[v for v in row] for row in A_dual]  # Optionnel: explicite la conversion liste
        self.requirements = costs  # c_primal → borne supérieure des contraintes du dual

    def solve(self):
        result = linprog(c=self.costs, A_ub=self.constraints, b_ub=self.requirements, method='highs')
        if result.success:
            return result.x, -result.fun  # Remet le max
        else:
            print("Aucune solution optimale trouvée (dual).")
            return None, None


