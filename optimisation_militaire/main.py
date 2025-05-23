import sys
import os
from prettytable import PrettyTable


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'optimisation_militaire/')))

from question import PrimalProblem
from question import DualProblem
from graphique import plot_3d_graph, plot_sensitivity_graph

def display_primal_results(lots, costs, cost_total):
    print("\nVoici la solution optimale du problème de minimisation de la dépense du pays PATIBULAIRE:")
    table = PrettyTable()
    table.field_names = ["Lot", "Quantité", "Coût unitaire (M$)", "Coût total (M$)"]
    
    for i, (lot, cost) in enumerate(zip(lots, costs), 1):
        total_cost = lot * cost
        table.add_row([f"Lot {i}", round(lot, 4), cost, round(total_cost, 4)])
    
    print(table)
    print(f"Le dépense totale minimale pour satisfaire la demande du pays PATIBULAIRE est de {round(cost_total, 4)} millions de dollars.")

def display_dual_results(prices, profit):
    print("\nVoici la solution optimale du problème de maximisation du bénéfice de DETAILIN :")
    table = PrettyTable()
    table.field_names = ["Type d'armement", "Prix unitaire (M$)", "Bénéfice (M$)"]
    armes = ["fusils", "Grenades", "Chars", "Mitrailleuses", "bazookas"]
    
    for arme, price in zip(armes, prices):
        benefit = price * 100000 if arme == "fusils" else price * 200000 if arme == "Grenades" else 0
        table.add_row([arme, round(price * 1000000, 5), round(benefit * 100, 4)])
    
    print(table)
    print(f"Le bénéfice total maximal pour DETAILIN est de {round(profit * 1000000, 4)} dollars.")

def display_sensitivity_results(price, cost_total, lots, profit, prices):
    table = PrettyTable()
    table.field_names = ["Prix du Lot 1 (M$)", "Coût total (M$)", "Lots achetés", "Bénéfice total (M$)", "Prix unitaires"]
    lots_str = ", ".join([f"{round(lot, 2)}" for lot in lots])
    prices_str = ", ".join([f"{round(price, 5)}" for price in prices])
    table.add_row([price, round(cost_total, 4), lots_str, round(profit, 4), prices_str])
    print(table)

def study_price_variation():

    price_range = list(range(1, 30)) 
    costs = [10, 12, 15]
    constraints = [
        [500, 300, 800],   
        [1000, 2000, 1500],
        [10, 20, 15],      
        [100, 80, 15],     
        [80, 120, 200]     
    ]
    requirements = [100000, 200000, 100, 400, 400]

    cost_totals = []
    profit_totals = []


    table = PrettyTable()
    table.field_names = ["Prix du Lot 1 (M$)", "Coût total (M$)", "Lots achetés", "Bénéfice total (M$)", "Prix unitaires"]

    for price in price_range:
        costs[0] = price
        
        primal = PrimalProblem(costs, constraints, requirements)
        lots, cost_total = primal.solve()
        cost_totals.append(cost_total)

        dual = DualProblem(costs, constraints, requirements)
        prices, profit = dual.solve()
        profit_totals.append(profit * 1000000)  


        lots_str = ", ".join([f"{round(lot, 2)}" for lot in lots])
        prices_str = ", ".join([f"{round(price, 5)}" for price in prices])
        table.add_row([price, round(cost_total, 4), lots_str, round(profit * 1000000, 4), prices_str])

    print(table)

    plot_sensitivity_graph(price_range, cost_totals, profit_totals)


def main():
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


    print("\n=== Problème Primal ===")
    primal = PrimalProblem(costs, constraints, requirements)
    lots, cost_total = primal.solve()
    display_primal_results(lots, costs, cost_total)
    plot_3d_graph(constraints, requirements, lots)


    print("\n=== Problème Dual ===")
    dual = DualProblem(costs, constraints, requirements)
    prices, profit = dual.solve()
    display_dual_results(prices, profit)


    print("\n=== Étude de sensibilité du prix du Lot 1 ===")
    study_price_variation()

if __name__ == "__main__":
    main()