"""
    Ce script permet à l’utilisateur de saisir manuellement les données nécessaires
    à la généralisation du problème d’optimisation militaire :

    - les coûts des lots
    - la composition des lots
    - les besoins minimaux en armement
    - les noms des armements

    Les données sont ensuite sauvegardées automatiquement dans un fichier JSON
    situé dans le dossier 'Data', pour être utilisées ultérieurement par 'app.py' dans Optimisation_militaire.
"""




import json
import os

def ask_for_list(prompt, length=None):

    """
    Demande à l’utilisateur une liste de valeurs numériques saisies sur une seule ligne

    Agrss :
    - prompt (str)       : message affiché à l’utilisateur
    - length (int) : nombre exact de valeurs attendues

    Retour :
    - list of float : les valeurs saisies par l’utilisateur
    """

    while True:
        try:
            values = input(prompt).strip().split()
            if length is not None and len(values) != length:
                print(f"Erreur : vous devez saisir exactement {length} valeurs.")
                continue
            return [float(v) for v in values]
        except ValueError:
            print("Erreur : saisie incorrecte, veuillez entrer des nombres séparés par des espaces.")

def main():

    """
    Elle guide l’utilisateur à travers :
    - la saisie des coûts des lots
    - la définition du nombre de types d’armement
    - la saisie de la composition de chaque lot
    - la saisie des besoins minimaux
    - la saisie des noms des armements

    Les données sont sauvegardées dans 'Data/generalisation_data.json'
    """

    print("\n===     Saisie interactive des données pour l'optimisation militaire     === ")
    costs = ask_for_list("\n-->  Entrez les coûts des lots (exemple : 10 12 15) : ")
    n_lots = len(costs)
    n_constraints = int(input("\n-->  Combien de types d’armement différents (contraintes) souhaitez-vous définir ? : "))


    print(f"\n--> Pour chaque type d’armement, entrez les quantités contenues dans les {n_lots} lots.")
    constraints = []
    for i in range(n_constraints):
        prompt = f"   🔹 Type d’armement #{i+1} (quantités dans chaque lot, séparées par espaces) : "
        row = ask_for_list(prompt, length=n_lots)
        constraints.append(row)

    requirements = ask_for_list(f"\n-->  Entrez les besoins minimaux pour chaque type d’armement (exemple : 1000 500 200) : ",
        length=n_constraints)

    armes = []
    print("\n-->  Nommez chaque type d’armement (exemple : fusils, grenades, chars...) :")
    for i in range(n_constraints):
        nom = input(f"   🔹 Nom du type d’armement #{i+1} : ")
        armes.append(nom)

    data = {
        "costs": costs,
        "constraints": constraints,
        "requirements": requirements,
        "armes": armes
    }

    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Data"))
    os.makedirs(base_dir, exist_ok=True)
    filepath = os.path.join(base_dir, "generalisation_data.json")

    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)
    print(f"\n Données sauvegardées avec succès dans {filepath}")



if __name__ == "__main__":
    main()
