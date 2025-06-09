import os
import json
from generalisation import GeneralizedPrimalProblem, GeneralizedDualProblem
from graphique import plot_generalized_sensitivity
from prettytable import PrettyTable


def load_data(filename):
    path = os.path.join(os.path.dirname(__file__), '..', 'Data', filename)
    with open(path, 'r') as f:
        return json.load(f)


def display_lot_table(constraints, costs, armes):
    
    print("Ces marchands proposent différents types de lots.")
    table = PrettyTable()
    n_lots = len(costs)
    headers = ["Type d'armement"] + [f"Lot {i+1}" for i in range(n_lots)]
    table.field_names = headers

    for i, arme in enumerate(armes):
        row = [arme] + [constraints[i][j] for j in range(n_lots)]
        table.add_row(row)

    table.add_row(["Coûts des lots"] + [f"{c}" for c in costs])
    print(table)



def display_primal_solution(lots, costs):
    print("\n" + "=" * 110)
    print("                  QUESTION 1 : Quelle est la solution optimale pour le Client (minimiser les coûts)")
    print(110* "=" + "\n")

    table = PrettyTable()
    table.field_names = ["Lot", "Quantité", "Coût unitaire ", "Coût total "]

    total_cost = 0
    for i, (qte, cost) in enumerate(zip(lots, costs), 1):
        cost_total = qte * cost
        total_cost += cost_total
        table.add_row([f"Lot {i}", round(qte, 2), cost, round(cost_total, 2)])

    print(table)
    print(f"→ Coût total minimal (client) : {round(total_cost, 2)}")




def display_dual_solution(prices, requirements, armes):
    print("\n" + "=" * 110)
    print("                  QUESTION 2 : Quelle est la solution optimale pour le Fournisseur (maximiser les bénéfices)")
    print(110* "=" + "\n")

    table = PrettyTable()
    table.field_names = ["Type d'armement", "Prix unitaire", "Bénéfice "]

    total_profit = 0
    for arme, price, req in zip(armes, prices, requirements):
        profit = price * req
        total_profit += profit 
        table.add_row([arme, round(price , 5), round(profit, 5)])

    print(table)
    print(f"→ Bénéfice total maximal (Fournisseur) : {round(total_profit, 2)} ")
    return total_profit




def display_comparative_table(lots, costs, prices, armes, requirements):
    print("\n" + "=" * 110)
    print("                  QUESTION 3 : COMPARAISON PRIMAL / DUAL")
    print(110* "=" + "\n")

    table = PrettyTable()
    table.field_names = ["Lot", "Quantité", "Coût unitaire", "Coût total",
                        "Prix unitaire", "Bénéfice "]

    total_cost = 0
    total_benefit = 0

    for i, (lot, cost, price, req) in enumerate(zip(lots, costs, prices, requirements), 1):
        cost_total = lot * cost
        benefit = price * req
        total_cost += cost_total
        total_benefit += benefit
        table.add_row([
            f"Lot {i}", round(lot, 2), cost, round(cost_total, 2),
            round(price, 5), round(benefit, 2)
        ])

    print(table)
    print(f"→ Coût total minimal (Patibulaire) : {round(total_cost, 2)}")
    print(f"→ Bénéfice total maximal (Detailin) : {round(total_benefit, 2)}")




def study_sensitivity(costs, constraints, requirements):
    print("\n" + "=" * 110)
    print("                   QUESTION 3 (Suite) : Étude de sensibilité – Variation du prix du Lot 1")
    print(110* "=" + "\n")

    price_range = list(range(1, 31))
    cost_totals = []
    profit_totals = []

    for new_price in price_range:
        modified_costs = costs.copy()
        modified_costs[0] = new_price

        primal = GeneralizedPrimalProblem(modified_costs, constraints, requirements)
        lots, total_cost = primal.solve()
        cost_totals.append(total_cost if total_cost else 0)

        dual = GeneralizedDualProblem(modified_costs, constraints, requirements)
        prices, profit = dual.solve()
        profit_totals.append(profit if profit else 0)

    plot_generalized_sensitivity(price_range, cost_totals, profit_totals)


def main():
    print("\n" + "=" * 80)
    print("               GÉNÉRALISATION D'UN PROBLÈME D'OPTIMISATION LINÉAIRE")
    print(80* "=" + "\n")

    data = load_data("generalisation_data.json")

    costs = data["costs"]
    constraints = data["constraints"]
    requirements = data["requirements"]
    armes = data["armes"]

    display_lot_table(constraints, costs, armes)

    primal = GeneralizedPrimalProblem(costs, constraints, requirements)
    lots, cost_total = primal.solve()
    display_primal_solution(lots, costs)

    dual = GeneralizedDualProblem(costs, constraints, requirements)
    prices, profit = dual.solve()
    display_dual_solution(prices, requirements, armes)

    display_comparative_table(lots, costs, prices, armes, requirements)

    study_sensitivity(costs, constraints, requirements)


if __name__ == "__main__":
    main()
