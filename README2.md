# 📦 PROJET ARME – Optimisation linéaire d’achat d’armement

## 🧭 INTRODUCTION

Ce projet ARME simule la planification d’achats d’armements pour un pays fictif. Il vise à satisfaire des besoins militaires tout en minimisant les dépenses à l’aide de la programmation linéaire.  

Deux versions sont disponibles :
- **Classique** (résolution fixe du problème primal et dual)
- **Généralisée** (saisie dynamique avec visualisations)

---

## ⚙️ FONCTIONNALITÉS

- 🔹 Résolution d’un problème d’optimisation linéaire (primal & dual)
- 🔹 Interface terminal pour saisir les données
- 🔹 Visualisation 2D & 3D
- 🔹 Étude de sensibilité (impact du prix du lot)
- 🔹 Tests unitaires avec couverture
- 🔹 Code structuré, commenté et testé

---

## 🗂️ STRUCTURE DU PROJET

```text
projet_arme/
│
├── DATA/
│   └── generalisation_data.json         # Données JSON saisies via interface
│
├── optimisation_militaire/
│   ├── interface.py                     # Saisie interactive des données
│   ├── generalisation.py                # Résolution généralisée (primal + dual)
│   ├── graphique.py                     # Courbes coût/bénéfice
│   └── main.py                          # Lancement de la version généralisée
│
├── resolution/
│   ├── question.py                      # Classes PrimalProblem et DualProblem
│   ├── graphique.py                     # Visualisation 3D du modèle classique
│   └── main.py                          # Lancement de la version classique
│
└── test/
    ├── test_generalisation.py           # Tests version généralisée
    └── test_question.py                 # Tests version classique
--- 
```

## 🐍 EXIGENCES

Python 3.11+
Modules : numpy, scipy, matplotlib, prettytable, pytest, flake8 (optionnel)


## 💻 INSTALLATION

### 📦 Via pip

python -m pip install git+https://github.com/Ilayda-git/Projet-ARME.git

### 🧪 Via clonage + Poetry

git clone https://github.com/Ilayda-git/Projet-ARME.git
cd Projet-ARME
python -m poetry install
python -m poetry env activate


## ▶️ EXÉCUTION DU PROJET

### 🔸 Version classique (données fixes)
cd resolution
python main.py
Résultats affichés :

Coût minimal
Bénéfice maximal
Visualisation 3D
Étude de sensibilité

### 🔸 Version généralisée (données dynamiques)
Saisie utilisateur :
python optimisation_militaire/interface.py
Lancement de la résolution :
python optimisation_militaire/main.py
Résultats :

- Tables du primal et dual
- Comparaison des solutions
- Courbe coût vs bénéfice


## ✅ TESTS

Lancer tous les tests + couverture :

pytest --cov=.



## 🧩 CONCLUSION

Ce projet montre l’utilité concrète de l’optimisation linéaire pour résoudre un problème stratégique.
La modélisation duale offre une lecture économique complémentaire à la solution optimale du client.

