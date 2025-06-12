"""
Ce fichier Contient les fonctions de visualisation :

- 'plot_3d_graph' : projection graphique 3D du problème de base
- 'plot_sensitivity_graph' : visualisation de la variation du coût et du bénéfice  
en fonction du prix d’un lot (étude de sensibilité)

Utilise Matplotlib pour afficher les courbes.
"""



import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch


def plot_3d_graph(A, b, res):

    """
    Affiche un graphique 3D représentant les contraintes linéaires
    du problème primal sous forme de plans dans l'espace.

    Agrs :
        A (list[list[float]]) : Matrice des coefficients des contraintes (5x3)
        b (list[float]) : Côté droit des inégalités, représentant les besoins
        res (list[float]) : Coordonnées (x, y, z) de la solution optimale

    Ce graphique montre :
    - Les plans d'inégalités formés par chaque contrainte.
    - Le point rouge représentant la solution optimale.
    """

    x = np.linspace(0, 1000, 300)
    y = np.linspace(0, 1000, 300)
    x, y = np.meshgrid(x, y)

    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111, projection='3d')


    colors = ['#4682B4', '#32CD32', '#FFD700', '#FF6347', '#6A5ACD']
    labels = ['Fusils', 'Grenades', 'Chars', 'Mitrailleuses', 'Bazookas']


    legend_elements = []
    for i, (a, bi, color, label) in enumerate(zip(A, b, colors, labels)):
        if a[2] != 0:
            z = (bi - a[0] * x - a[1] * y) / a[2]
            ax.plot_surface(x, y, z, alpha=0.6, rstride=30, cstride=30, color=color, label=label)
            legend_elements.append(Patch(color=color, label=f"Contrainte {label}"))

    point_x, point_y, point_z = res
    ax.scatter(point_x, point_y, point_z, color='red', s=150, label="Solution optimale", marker='o')


    ax.plot([point_x, point_x], [point_y, point_y], [0, point_z], color='black', linestyle='--', linewidth=2)
    ax.plot([0, point_x], [point_y, point_y], [point_z, point_z], color='black', linestyle='--', linewidth=2)
    ax.plot([point_x, point_x], [0, point_y], [point_z, point_z], color='black', linestyle='--', linewidth=2)
    
    ax.text(point_x, point_y, point_z, f"  Optimal ({round(point_x, 2)}, {round(point_y, 2)}, {round(point_z, 2)})",
            color='darkred', fontsize=12, weight='bold')


    ax.set_xlabel('Quantité de Lot 1', fontsize=14, labelpad=15)
    ax.set_ylabel('Quantité de Lot 2', fontsize=14, labelpad=15)
    ax.set_zlabel('Quantité de Lot 3', fontsize=14, labelpad=15)
    ax.set_title("Optimisation des lots d'armement  Pays PATIBULAIRE", fontsize=18, pad=20)
    ax.legend(handles=legend_elements, loc='upper right', fontsize=12)
    plt.show()

def plot_sensitivity_graph(price_range, cost_totals, profit_totals):

    """
    Affiche l'étude de sensibilité du prix du Lot 1.

    Agrs :
        price_range (list[int]) : Liste des prix testés pour le Lot 1 (ex: 1 à 30 M$)
        cost_totals (list[float]) : Coûts totaux obtenus pour chaque prix
        profit_totals (list[float]) : Bénéfices totaux obtenus pour chaque prix

    Ce graphique contient deux courbes :
        - Ligne bleue : Coût total de l’achat des lots (problème primal)
        - Ligne verte : Bénéfice total du vendeur (problème dual)

    L'objectif est de visualiser à partir de quel prix
    le coût ou le bénéfice devient stable ( optimal ).

    Exemple visuel :
        o Coût     (bleu)
        x Bénéfice (vert)
    """
    
    plt.figure(figsize=(10, 6))
    plt.plot(price_range, cost_totals, label="Coût total (M$)", marker='o', color='blue')
    plt.plot(price_range, profit_totals, label="Bénéfice total (M$)", marker='x', color='green')
    plt.title("Impact de la variation du prix du Lot 1 sur le coût et le bénéfice")
    plt.xlabel("Prix du Lot 1 (M$)")
    plt.ylabel("Montant (M$)")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.show()
    