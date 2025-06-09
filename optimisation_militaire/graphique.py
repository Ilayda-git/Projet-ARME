import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from mpl_toolkits.mplot3d import Axes3D


def plot_generalized_sensitivity(price_range, cost_totals, profit_totals):
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


