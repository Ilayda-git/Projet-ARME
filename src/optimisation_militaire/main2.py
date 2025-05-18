import os
import json
from prettytable import PrettyTable
from primal import PrimalProblem
from dual import DualProblem
from graphique import plot_generalized_sensitivity


def load_data(file_name):
    """Charge les données JSON depuis le dossier data/ en chemin absolu"""
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "data", file_name)
    with open(file_path, 'r') as f:
        return json.load(f)

def display_input_data(constraints, costs, armes):
    print("\n" + "=" * 80)
    print("Ces marchands proposent différents types de lots (M$ = millions de dollars).")
    print("=" * 80)

    table = PrettyTable()
    table.field_names = ["Type d'armement"] + [f"Lot {i+1}" for i in range(len(costs))]

    for i, arme in enumerate(armes):
        table.add_row([arme] + constraints[i])

    table.add_row(["Coûts des lots"] + [f"{c} M$" for c in costs])
    print(table)

def display_primal_solution(lots, costs):
    table = PrettyTable()
    table.field_names = ["Lot", "Quantité", "Coût unitaire (M$)", "Coût total (M$)"]

    total_cost = 0
    for i, (lot, cost) in enumerate(zip(lots, costs), 1):
        cost_total = lot * cost
        total_cost += cost_total
        table.add_row([f"Lot {i}", round(lot, 2), cost, round(cost_total, 2)])

    print(table)
    print(f"→ Coût total minimal (Patibulaire) : {round(total_cost, 2)} M$")
    return total_cost, lots

def display_dual_solution(prices, armes):
    table = PrettyTable()
    table.field_names = ["Type d'armement", "Prix unitaire (M$)", "Bénéfice (M$)"]

    benefit_total = 0
    for arme, price in zip(armes, prices):
        if arme.lower() == "fusils":
            benefit = price * 100000
        elif arme.lower() == "grenades":
            benefit = price * 200000
        elif arme.lower() == "chars":
            benefit = price * 100
        elif arme.lower() == "mitrailleuses":
            benefit = price * 400
        elif arme.lower() == "bazookas":
            benefit = price * 400
        else:
            benefit = 0
        benefit_total += benefit
        table.add_row([arme, round(price * 1_000_000, 5), round(benefit * 100, 2)])

    print(table)
    print(f"→ Bénéfice total maximal (Detailin) : {round(benefit_total, 2)} M$")
    return benefit_total, prices

def display_comparative_table(lots, costs, prices, armes):
    table = PrettyTable()
    table.field_names = ["Lot", "Quantité", "Coût unitaire (M$)", "Coût total (M$)", "Prix unitaire (M$)", "Bénéfice (M$)"]

    total_cost = 0
    total_benefit = 0
    for i, (lot, cost, price, arme) in enumerate(zip(lots, costs, prices, armes), 1):
        cost_total = lot * cost
        total_cost += cost_total

        if arme.lower() == "fusils":
            benefit = price * 100000
        elif arme.lower() == "grenades":
            benefit = price * 200000
        elif arme.lower() == "chars":
            benefit = price * 100
        elif arme.lower() == "mitrailleuses":
            benefit = price * 400
        elif arme.lower() == "bazookas":
            benefit = price * 400
        else:
            benefit = 0

        total_benefit += benefit

        table.add_row([
            f"Lot {i}", round(lot, 2), cost, round(cost_total, 2),
            round(price, 5), round(benefit * 100, 2)
        ])

    print(table)
    print(f"→ Coût total minimal (Patibulaire) : {round(total_cost, 2)} M$")
    print(f"→ Bénéfice total maximal (Detailin) : {round(total_benefit, 2)} M$")

def main():
    print("\n" + "="*80)
    print("               GÉNÉRALISATION D'UN PROBLÈME D'OPTIMISATION LINÉAIRE")
    print("="*80)

    data = load_data("generalisation_data.json")
    costs = data["costs"]
    constraints = data["constraints"]
    requirements = data["requirements"]
    armes = data["armes"]

    display_input_data(constraints, costs, armes)

    print("\n" + "-"*80)
    print("QUESTION 1 : Quelle est la solution optimale pour PATIBULAIRE (minimiser les coûts)")
    print("-"*80)
    primal = PrimalProblem(costs, constraints, requirements)
    lots, total_cost = primal.solve()
    total_cost, lots = display_primal_solution(lots, costs)

    print("\n" + "-"*80)
    print("QUESTION 2 : Quelle est la solution optimale pour DETAILIN (maximiser les bénéfices)")
    print("-"*80)
    dual = DualProblem(costs, constraints, requirements)
    prices, profit = dual.solve()
    benefit_total, prices = display_dual_solution(prices, armes)

    print("\n" + "="*80)
    print("                         QUESTION 3 : COMPARAISON PRIMAL / DUAL")
    print("="*80)
    display_comparative_table(lots, costs, prices, armes)

    print("\n" + "="*80)
    print("QUESTION 3 (Suite) : Étude de sensibilité – Variation du prix du Lot 1")
    print("="*80)

    price_range = list(range(1, 30))
    cost_totals = []
    profit_totals = []

    for new_price in price_range:
        temp_costs = costs.copy()
        temp_costs[0] = new_price

        primal = PrimalProblem(temp_costs, constraints, requirements)
        lots, cost_total = primal.solve()
        cost_totals.append(cost_total)

        dual = DualProblem(temp_costs, constraints, requirements)
        prices, profit = dual.solve()
        profit_totals.append(profit)

    plot_generalized_sensitivity(price_range, cost_totals, profit_totals)

if __name__ == "__main__":
    main()
