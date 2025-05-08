import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from mpl_toolkits.mplot3d import Axes3D

def plot_3d_graph(A, b, res):
    x = np.linspace(0, 1000, 300)
    y = np.linspace(0, 1000, 300)
    x, y = np.meshgrid(x, y)

    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111, projection='3d')

    # Couleurs et libellés des contraintes
    colors = ['#4682B4', '#32CD32', '#FFD700', '#FF6347', '#6A5ACD']
    labels = ['Fusils', 'Grenades', 'Chars', 'Mitrailleuses', 'Bazookas']

    # Légende dynamique
    legend_elements = []

    # Tracer les surfaces des contraintes
    for i, (a, bi, color, label) in enumerate(zip(A, b, colors, labels)):
        if a[2] != 0:
            z = (bi - a[0] * x - a[1] * y) / a[2]
            ax.plot_surface(x, y, z, alpha=0.6, rstride=30, cstride=30, color=color, label=label)
            legend_elements.append(Patch(color=color, label=f"Contrainte {label}"))

    # Point optimal
    point_x, point_y, point_z = res
    ax.scatter(point_x, point_y, point_z, color='red', s=150, label="Solution optimale", marker='o')

    # Tracer les projections
    ax.plot([point_x, point_x], [point_y, point_y], [0, point_z], color='black', linestyle='--', linewidth=2)
    ax.plot([0, point_x], [point_y, point_y], [point_z, point_z], color='black', linestyle='--', linewidth=2)
    ax.plot([point_x, point_x], [0, point_y], [point_z, point_z], color='black', linestyle='--', linewidth=2)

    # Annotations
    ax.text(point_x, point_y, point_z, f"  Optimal ({round(point_x, 2)}, {round(point_y, 2)}, {round(point_z, 2)})",
            color='darkred', fontsize=12, weight='bold')

    # Axes et légendes
    ax.set_xlabel('Quantité de Lot 1', fontsize=14, labelpad=15)
    ax.set_ylabel('Quantité de Lot 2', fontsize=14, labelpad=15)
    ax.set_zlabel('Quantité de Lot 3', fontsize=14, labelpad=15)
    ax.set_title("Optimisation des lots d'armement - Pays PATIBULAIRE", fontsize=18, pad=20)

    # Légende
    ax.legend(handles=legend_elements, loc='upper right', fontsize=12)

    # Affichage
    plt.show()

def plot_sensitivity_graph(price_range, cost_totals, profit_totals):
    plt.figure(figsize=(10, 6))

    # Graphique du coût total
    plt.plot(price_range, cost_totals, label="Coût total (M$)", marker='o', color='blue')

    # Graphique du bénéfice total
    plt.plot(price_range, profit_totals, label="Bénéfice total (M$)", marker='x', color='green')

    # Configuration du graphique
    plt.title("Impact de la variation du prix du Lot 1 sur le coût et le bénéfice")
    plt.xlabel("Prix du Lot 1 (M$)")
    plt.ylabel("Montant (M$)")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.show()