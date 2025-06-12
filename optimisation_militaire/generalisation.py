"""
Ce module contient deux classes principales :
- GeneralizedPrimalProblem  : résolution du problème primal (minimisation des coûts),
- GeneralizedDualProblem  : résolution du problème dual (maximisation des bénéfices).

Ces classes utilisent la bibliothèque 'scipy.optimize.linprog' pour résoudre les
programmes linéaires de manière générique, quel que soit le nombre de lots ou de types d’armement.
"""




from scipy.optimize import linprog
import numpy as np

class GeneralizedPrimalProblem:

    """
    Représente le problème primal : comment satisfaire les besoins en armement
    avec un coût total minimal.

    args :
    - costs (list of float)         : coûts unitaires de chaque lot
    - constraints (list of list)    : matrice des quantités de chaque armement par lot
    - requirements (list of float)  : quantités minimales à atteindre pour chaque armement
    """
    
    def __init__(self, costs, constraints, requirements):
        """
        Initialise le problème primal.
        Les contraintes sont inversées pour être compatibles avec 'linprog'
        """
        self.costs = costs
        self.constraints = [[-c for c in row] for row in constraints]
        self.requirements = [-r for r in requirements]

    def solve(self):
        """
        Résout le problème de minimisation des coûts via 'scipy.optimize.

        Retour :
        - tuple (lots, coût_total)
        - lots : quantités optimales à acheter pour chaque lot
        - coût_total : dépense minimale obtenue
        """
        result = linprog(c=self.costs, A_ub=self.constraints, b_ub=self.requirements, method='highs')
        if result.success:
            return result.x, result.fun
        else:
            print("Aucune solution optimale trouvée")
            return None, None


class GeneralizedDualProblem:

    """
    Représente le problème dual : comment fixer les prix unitaires des armements
    pour que les lots ne dépassent pas leur prix d’origine, tout en maximisant le bénéfice.

    args :
    - costs (list of float)         : coûts unitaires des lots (b_ub dans le dual)
    - constraints (list of list)    : matrice des quantités de chaque armement par lot
    - requirements (list of float)  : quantités minimales requises (deviennent c dans le dual)
    """
    
    def __init__(self, costs, constraints, requirements):
        """
        Initialise le problème dual. Transpose la matrice des contraintes pour être
        compatible avec la formulation du dual.
        """
        self.costs = [-r for r in requirements]

        A_dual = np.transpose(constraints)
        self.constraints = [[v for v in row] for row in A_dual] 
        self.requirements = costs 

    def solve(self):
        """
        Résout le problème de maximisation du bénéfice avec 'scipy.optimize'.

        Retour :
        - tuple (prices, profit)
        - prices : prix unitaires optimaux des armements
        - profit : bénéfice total maximal réalisable
        """
        result = linprog(c=self.costs, A_ub=self.constraints, b_ub=self.requirements, method='highs')
        if result.success:
            return result.x, -result.fun 
        else:
            print("Aucune solution optimale trouvée")
            return None, None
