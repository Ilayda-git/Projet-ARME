"""
Ce module contient la fonction nécessaire pour visualiser graphiquement :
- la sensibilité du coût et du bénéfice à la variation du prix d’un lot

Il utilise 'matplotlib' pour produire des visualisations lisibles et interprétables
dans le cadre de l’analyse économique et stratégique du problème.
"""




import numpy as np
import matplotlib.pyplot as plt



def plot_generalized_sensitivity(price_range, cost_totals, profit_totals):

    """
    Affiche un graphique 2D montrant l’impact de la variation du prix du Lot 1
    sur le coût total pour le client et le bénéfice total pour le fournisseur.

    Args :
    - price_range (list of int)       : liste des valeurs testées pour le prix du lot 1
    - cost_totals (list of float)     : coût total pour chaque prix
    - profit_totals (list of float)   : bénéfice total pour chaque prix
    
    Retour :
    - Affiche un graphique matplotlib
    """
    plt.figure(figsize=(10, 6))
    plt.plot(price_range, cost_totals, label="Coût total (Client)", marker="o", color="blue")
    plt.plot(price_range, profit_totals, label="Bénéfice total (Fournisseur)", marker="x", color="green")
    plt.xlabel("Prix du Lot 1 ")
    plt.ylabel("Montant ")
    plt.title("Impact de la variation du prix du Lot 1 sur le coût et le bénéfice")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


