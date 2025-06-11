"""
Ce fichier exécute l’analyse du problème d’optimisation généralisé à partir des données saisies dans interface.py 
et sauvegardées dans le fichier JSON.

Il permet de :
- Résoudre le problème primal (minimisation des coûts pour le client)
- Résoudre le problème dual (maximisation du bénéfice pour le fournisseur)
- Comparer les deux solutions
- Étudier l’impact du prix du Lot 1 sur le coût total et le bénéfice

Les résultats sont affichés sous forme de tableaux et de graphique.
"""




import os
import json
from generalisation import GeneralizedPrimalProblem, GeneralizedDualProblem
from graphique import plot_generalized_sensitivity
from prettytable import PrettyTable


def load_data(filename):
    
    """
    Charge les données JSON nécessaires à la résolution du problème d'optimisation.

    Paramètre :
        filename (str) : Nom du fichier JSON situé dans le dossier 'Data'.

    Retourne fichier 'generalisation_data.json' : 
        dict : Contenu du fichier contenant :
            - costs : Liste des coûts des lots
            - constraints : Matrice des contraintes par type d’armement
            - requirements : Liste des besoins minimaux
            - armes : Liste des types d’armement

    Exemple :
        {
            "costs": [10, 12, 15],
            "constraints": [[500, 300, 800], ...],
            "requirements": [100000, 200000, ...],
            "armes": ["fusils", "grenades", ...]
        }
    """
    
    path = os.path.join(os.path.dirname(__file__), '..', 'Data', filename)
    with open(path, 'r') as f:
        return json.load(f)



def display_lot_table(constraints, costs, armes):
    
    """
    Affiche le tableau initial des types d’armement contenus dans chaque lot, ainsi que leur coût. 

    Paramètres :
        constraints (list[list[float]]) : Quantité d’armement par lot
        costs (list[float]) : Coût de chaque lot
        armes (list[str]) : Nom des types d’armement

    Exemple de tableau affiché :
        ================================================================================
                    GÉNÉRALISATION D'UN PROBLÈME D'OPTIMISATION LINÉAIRE
        ================================================================================
    
        +---------------------+--------+--------+--------+
        | Type d'armement     | Lot 1  | Lot 2  | Lot 3  |
        +---------------------+--------+--------+--------+
        | Fusils plasma       |  300   |  600   |  500   |
        | Grenades soniques   |  800   | 1000   | 1200   |
        | Chars amphibies     |   12   |   8    |  20    |
        | Mitrailleuses laser |   50   |   60   |  70    |
        | Bazookas autonomes  |   30   |   90   | 160    |
        | Coûts des lots      |  7 M$  | 11 M$  | 14 M$  |
        +---------------------+--------+--------+--------+
    """
    
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
    
    """
    Résout et affiche la solution du problème primal (minimisation du coût).

    Paramètres :
        lots (list[float]) : Quantité de chaque lot acheté
        costs (list[float]) : Coût unitaire de chaque lot

    Affiche :
        ==============================================================================================================
                    QUESTION 1 : Quelle est la solution optimale pour le Client (minimiser les coûts)
        ==============================================================================================================
    
        +-------+----------+----------------+-------------+
        |  Lot  | Quantité | Coût unitaire  | Coût total  |
        +-------+----------+----------------+-------------+
        | Lot 1 |  111.11  |      7.0       |    777.78   |
        | Lot 2 |  111.11  |      11.0      |   1222.22   |
        | Lot 3 |   0.0    |      14.0      |     0.0     |
        +-------+----------+----------------+-------------+
        -> Coût total minimal (client) : 2000.0
    """

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
    print(f"-> Coût total minimal (client) : {round(total_cost, 2)}")



def display_dual_solution(prices, requirements, armes):
    
    """
    Résout et affiche la solution du problème dual (maximisation du bénéfice).

    Paramètres :
        prices (list[float]) : Prix unitaires optimaux des types d’armement.
        requirements (list[float]) : Quantité minimale demandée pour chaque armement.
        armes (list[str]) : Noms des armements.

    Affiche :
        ==============================================================================================================
                    QUESTION 2 : Quelle est la solution optimale pour le Fournisseur (maximiser les bénéfices)
        ==============================================================================================================
        
        +---------------------+---------------+-----------+
        |   Type d'armement   | Prix unitaire | Bénéfice  |
        +---------------------+---------------+-----------+
        |       fusils        |      0.01     |   1000.0  |
        |  Grenades soniques  |     0.005     |   1000.0  |
        |   Chars amphibies   |      0.0      |    0.0    |
        | Mitrailleuses laser |      0.0      |    0.0    |
        |  Bazookas autonomes |      0.0      |    0.0    |
        +---------------------+---------------+-----------+
        -> Bénéfice total maximal (Fournisseur) : 2000.0 
    """
    
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
    print(f"-> Bénéfice total maximal (Fournisseur) : {round(total_profit, 2)} ")
    return total_profit



def display_comparative_table(lots, costs, prices, armes, requirements):
    
    """
    Affiche un tableau croisé comparant la solution du primal et du dual.

    Paramètres :
        lots (list[float]) : Quantité de chaque lot acheté.
        costs (list[float]) : Coût unitaire de chaque lot.
        prices (list[float]) : Prix unitaire optimal de chaque armement.
        armes (list[str]) : Types d’armement.
        requirements (list[float]) : Besoins minimaux en armement.

    Affiche :
        =========================================================================
                    QUESTION 3 : COMPARAISON PRIMAL / DUAL
        =========================================================================

    
        +-------+----------+---------------+------------+---------------+-----------+
        |  Lot  | Quantité | Coût unitaire | Coût total | Prix unitaire | Bénéfice  |
        +-------+----------+---------------+------------+---------------+-----------+
        | Lot 1 |  111.11  |      7.0      |   777.78   |      0.01     |   1000.0  |
        | Lot 2 |  111.11  |      11.0     |  1222.22   |     0.005     |   1000.0  |
        | Lot 3 |   0.0    |      14.0     |    0.0     |      0.0      |    0.0    |
        +-------+----------+---------------+------------+---------------+-----------+
        -> Coût total minimal (Patibulaire) : 2000.0
        -> Bénéfice total maximal (Detailin) : 2000.0
    """
    
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
    print(f"-> Coût total minimal (Patibulaire) : {round(total_cost, 2)}")
    print(f"-> Bénéfice total maximal (Detailin) : {round(total_benefit, 2)}")



def study_sensitivity(costs, constraints, requirements):
    
    """
    Analyse l’impact de la variation du prix du premier lot sur :
    - le coût total pour le client
    - le bénéfice total du fournisseur

    Paramètres :
    - costs (list of float)       : liste des prix initiaux des lots
    - constraints (list of list)  : matrice de composition des lots
    - requirements (list of int)  : besoins à satisfaire

    Retour :
    - Affiche un graphique de sensibilité
    """
    
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
    
    """
    Fonction principale exécutée lors du lancement du programme.

    Étapes :
        1. Chargement des données JSON depuis le dossier Data (via 'interface.py')
        2. Affichage des données des lots et armements
        3. Résolution du problème primal
        4. Résolution du problème dual
        5. Affichage comparatif Primal / Dual
        6. Étude de sensibilité du prix du Lot 1

    Ce fichier complète 'interface.py' qui sert à initialiser les données utilisateur.
    """

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
