"""
    Script principal pour la résolution du problème d’optimisation militaire de base.

    Ce fichier exécute trois étapes :
    1. Résolution du problème primal (minimisation du coût pour le client)
    2. Résolution du problème dual (maximisation du bénéfice pour le fournisseur)
    3. Étude de sensibilité sur le prix du Lot 1 (variation de coût/bénéfice)

    Utilise :
    - question.PrimalProblem et question.DualProblem
    - graphique.plot_3d_graph et plot_sensitivity_graph

    Affiche les résultats sous forme de tableaux et graphiques.
"""




import sys
import os
from prettytable import PrettyTable


sys.path.append(os.path.dirname(__file__))

from question import PrimalProblem, DualProblem
from graphique import plot_3d_graph, plot_sensitivity_graph


def display_primal_results(lots, costs, cost_total):

    """
    Affiche la solution optimale du problème primal (minimisation des coûts d’achat).

    Args:
        lots (list[float]): Quantité de chaque lot achetée
        costs (list[float]): Coûts unitaires de chaque lot
        cost_total (float): Coût total de la solution optimale

    Sortie console :
        ==================================================
                    1.  PROBLEME PRIMAL
        ==================================================

        +-------+----------+---------------+-----------------+
        |  Lot  | Quantité | Coût unitaire |    Coût total   |
        +-------+----------+---------------+-----------------+
        | Lot 1 |   0.0    |  10 000 000   |       0.0       |
        | Lot 2 |   8.7    |  12 000 000   |  104347826.09   |
        | Lot 3 |  121.74  |  15 000 000   | 1826086956.52   |
        +-------+----------+---------------+-----------------+
        -> Le dépense totale minimale est de 1930.43 millions de dollars.
    """

    print("\nVoici la solution optimale du problème de minimisation de la dépense du pays PATIBULAIRE:")
    table = PrettyTable()
    table.field_names = ["Lot", "Quantité", "Coût unitaire", "Coût total"]

    for i, (lot, cost) in enumerate(zip(lots, costs), 1):
        total_cost = lot * cost
        table.add_row([f"Lot {i}", round(lot, 4), cost* 1000000, round(total_cost* 1000000, 4)])

    print(table)
    print(f"-> Le dépense totale minimale pour satisfaire la demande du pays PATIBULAIRE est de {round(cost_total, 4)} millions de dollars.")



def display_dual_results(prices, profit):

    """
    Affiche la solution optimale du problème dual (maximisation du bénéfice).

    Args:
        prices (list[float]): Prix unitaires optimaux pour chaque type d’armement
        profit (float): Bénéfice total maximal obtenu

    Sortie console :
        ==================================================
                        2.  PROBLEME DUAL                   
        ==================================================

        +-----------------+----------------+-----------------+
        | Type d'armement | Prix unitaire  |    Bénéfice     |
        +-----------------+----------------+-----------------+
        |      fusils     |  10434.78261   | 1 043 478 260.87|
        |     grenades    |   4434.78261   |  886 956 521.74 |
        |      chars      |      0.0       |        0        |
        |  mitrailleuses  |      0.0       |        0        |
        |    bazookas     |      0.0       |        0        |
        +-----------------+----------------+-----------------+
        -> Le bénéfice total maximal est de 1 930 434 782.61 dollars.
    """

    print("\nVoici la solution optimale du problème de maximisation du bénéfice de DETAILIN :")
    table = PrettyTable()
    table.field_names = ["Type d'armement", "Prix unitaire ", "Bénéfice "]
    armes = ["fusils", "Grenades", "Chars", "Mitrailleuses", "bazookas"]

    for arme, price in zip(armes, prices):
        benefit = price * 100000 if arme == "fusils" else price * 200000 if arme == "Grenades" else 0
        table.add_row([arme, round(price * 1000000, 5), round(benefit * 1000000, 4)])

    print(table)
    print(f"-> Le bénéfice total maximal pour DETAILIN est de {round(profit , 4)} millions de dollars.")



def display_sensitivity_results(price, cost_total, lots, profit, prices):

    """
    Affiche les résultats intermédiaires de l’étude de sensibilité pour une valeur donnée du prix du Lot 1.

    Args:
        price (float): Nouveau prix du Lot 1 testé
        cost_total (float): Coût total du primal avec ce prix
        lots (list[float]): Quantités de lots achetés pour cette simulation
        profit (float): Bénéfice total du dual pour cette simulation
        prices (list[float]): Prix unitaires calculés dans la solution duale
    """
    
    table = PrettyTable()
    table.field_names = ["Prix du Lot 1 (M$)", "Coût total ", "Lots achetés", "Bénéfice total ", "Prix unitaires"]
    lots_str = ", ".join([f"{round(lot, 2)}" for lot in lots])
    prices_str = ", ".join([f"{round(price, 5)}" for price in prices])
    table.add_row([price, round(cost_total, 4), lots_str, round(profit, 4), prices_str])
    print(table)



def study_price_variation():

    """
    Effectue une étude de sensibilité sur le prix du Lot 1.

    Pour chaque prix du Lot 1 dans un intervalle [1, 29] :
    - Résout le problème primal pour obtenir le coût total
    - Résout le problème dual pour obtenir le bénéfice
    - Affiche les résultats dans un tableau
    - Trace un graphique de l'évolution du coût et du bénéfice

    sortie console :
        ============================================================
                3.  ÉTUDE DE LA SENSIBILITÉ DU PRIX DU LOT 1
        ============================================================

        +--------------------+--------------------+------------------+-------------------+-----------------------------------------+
        | Prix du Lot 1 (M$) |     Coût total     |   Lots achetés   |   Bénéfice total  |        Prix unitaires                   |
        +--------------------+--------------------+------------------+-------------------+-----------------------------------------+
        |         1          |    200 000 000.0   | 200.0, 0.0, 0.0  |  200 000 000.0    |      2000.0, 0.0, 0.0, 0.0, 0.0         |
        |         2          |    400 000 000.0   | 200.0, 0.0, 0.0  |  400 000 000.0    |      4000.0, 0.0, 0.0, 0.0, 0.0         |
        |         3          |    600 000 000.0   | 200.0, 0.0, 0.0  |  600 000 000.0    |      6000.0, 0.0, 0.0, 0.0, 0.0         |
        |         ...        |       ...          |       ...        |      ...          |             ...                         |
        |         29         | 1 930 434 782.6087 | 0.0, 8.7, 121.74 | 1 930 434 782.6087| 10434.78261, 4434.78261, 0.0, 0.0, 0.0  |
        +--------------------+--------------------+------------------+-------------------+-----------------------------------------+
    """

    price_range = list(range(1, 30)) 
    costs = [10, 12, 15]
    constraints = [
        [500, 300, 800],   
        [1000, 2000, 1500],
        [10, 20, 15],      
        [100, 80, 15],     
        [80, 120, 200]]
    requirements = [100000, 200000, 100, 400, 400]

    cost_totals = []
    profit_totals = []


    table = PrettyTable()
    table.field_names = ["Prix du Lot 1 (M$)", "Coût total ", "Lots achetés", "Bénéfice total ", "Prix unitaires"]

    for price in price_range:
        costs[0] = price
        
        primal = PrimalProblem(costs, constraints, requirements)
        lots, cost_total = primal.solve()
        cost_totals.append(cost_total)

        dual = DualProblem(costs, constraints, requirements)
        prices, profit = dual.solve()
        profit_totals.append(profit * 1000000)  


        lots_str = ", ".join([f"{round(lot, 2)}" for lot in lots])
        prices_str = ", ".join([f"{round(price * 1000000, 5)}" for price in prices])
        table.add_row([price, round(cost_total* 1000000, 4), lots_str, round(profit * 1000000, 4), prices_str])

    print(table)
    plot_sensitivity_graph(price_range, cost_totals, profit_totals)



def main():

    """
    Point d’entrée du script de résolution du problème initial.

    Étapes :
    - Résolution du problème primal (minimisation des coûts pour le client).
    - Résolution du problème dual (maximisation des bénéfices pour le fournisseur).
    - Affichage des résultats sous forme de tableaux PrettyTable.
    - Étude de sensibilité sur le prix du Lot 1.

    Exécution typique :
        (base) NomDeUtilisateur Projet-ARME % cd Resolution
        (base) NomDeUtilisateur Resolution % uv run app.py
    """
    
    # Données du problème
    costs = [10, 12, 15]
    constraints = [
        [500, 300, 800],   
        [1000, 2000, 1500], 
        [10, 20, 15],      
        [100, 80, 15],     
        [80, 120, 200]   
    ]
    requirements = [100000, 200000, 100, 400, 400]

    print("\n" + "="*50)
    print("                  1.  PROBLEME PRIMAL")
    print(50* "=" + "\n")

    primal = PrimalProblem(costs, constraints, requirements)
    lots, cost_total = primal.solve()
    display_primal_results(lots, costs, cost_total)
    plot_3d_graph(constraints, requirements, lots)

    print("\n" + "="*50)
    print("                 2.  PROBLEME DUAL")
    print(50* "=" + "\n")


    dual = DualProblem(costs, constraints, requirements)
    prices, profit = dual.solve()
    display_dual_results(prices, profit)


    print("\n" + "="*60)
    print("        3.  ÉTUDE DE LA SENSIBILITÉ DU PRIX DU LOT 1")
    print(60* "=" + "\n")
    
    study_price_variation()

if __name__ == "__main__":
    main()