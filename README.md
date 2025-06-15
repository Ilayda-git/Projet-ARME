# 📦 PROJET ARME – Optimisation linéaire d’achat d’armement

## INTRODUCTION

Ce projet ARME simule la planification d’achats d’armements pour le pays fictif PATIBULAIRE, qui doit satisfaire des besoins minimaux en défense tout en minimisant le coût total.

ProjetARME est une bibliothèque Python conçue pour résoudre des problèmes de programmation linéaire. Elle propose une interface claire et facile à utiliser, adaptée à divers domaines tels que la logistique, la gestion de la production ou la planification.

## Fonctionnalités principales

- Résolution de problèmes de programmation linéaire appliqués à la planification d’achats militaires.
- Version classique avec données fixes.
- Version généralisée avec interface utilisateur et visualisations graphiques.
- Étude de sensibilité sur les prix.
- Tests unitaires pour garantir la robustesse du code.

Ce module permet de résoudre différents types de problèmes. L'un d'eux, appelé ProblemePrimal, vise à minimiser les dépenses du consommateur pour différents lots fournis par un ou plusieurs vendeurs. L'autre, appelé ProblemeDual, vise à maximiser le profit d'un vendeur unique.

Ce travail illustre les enjeux économiques et stratégiques liés à l’achat d’armements dans un cadre optimisé.

## STRUCTURE DU PROJET:

Le projet est organisé en plusieurs dossiers distincts pour bien séparer les différentes parties. 
- Le dossier DATA contient les fichiers JSON qui regroupent les données utilisées, telles que les coûts, contraintes et besoins servant aux calculs d’optimisation. 
- Le dossier optimisation_militaire contient la version généralisée du projet avec quatre fichiers principaux : app.py pour lancer cette version, generalisation.py qui inclut la modélisation étendue, graphique.py qui fournit les fonctions de visualisation, et interface.py qui gère l’interaction utilisateur. 
- Le dossier resolution contient la version classique du problème avec trois fichiers : app.py, question.py qui définit les classes PrimalProblem et DualProblem ainsi que leurs méthodes de résolution, et graphique.py pour les visualisations graphiques. 
- Enfin, le dossier test regroupe deux fichiers de tests unitaires, test_optimisation_militaire.py et test_resolution.py, qui permettent de vérifier la validité et la robustesse du code.

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
│   └── app.py                           # Lancement de la version généralisée
│
├── resolution/
│   ├── question.py                      # Classes PrimalProblem et DualProblem
│   ├── graphique.py                     # Visualisation 3D du modèle classique
│   └── app.py                           # Lancement de la version classique
│
└── test/
    ├── test_optimisation_militaire.py     # Tests version généralisée
    └── test_resolution.py                 # Tests version classique
```

## EXIGENCE:
Python3.11

## INSTALATION :
### VIA PIP

```text
(base) NomDeUtilisateur python -m pip install git+https://github.com/Ilayda-git/Projet-ARME.git
```

Une fois la bibliothèque installée sur votre machine, vous pouvez l’utiliser directement dans vos scripts Python. La création d’un environnement virtuel n’est alors pas indispensable, bien qu’elle reste recommandée pour isoler les dépendances d’un projet.

### VIA LE CLONAGE ET POETRY
- Clonez le package avec la commande suivante :

```text
(base) NomDeUtilisateur git clone https://github.com/Ilayda-git/Projet-ARME.git
```

- Ouvrez un terminal dans le répertoire racine du package avec la commande :
```text
(base) NomDeUtilisateur cd ./Projet-ARME
```

- Créez un environnement virtuel et installez les dépendances avec la commande :

```text
(base) NomDeUtilisateur python -m poetry install
```

- Activez l'environnement virtuel avec la commande :

```text
(base) NomDeUtilisateur python -m poetry env activate
```

(arme-smQvmoZ_-py3.12)= Lorsque vous voyez (arme-smQvmoZ_-py3.12) affiché dans votre terminal, cela signifie que vous êtes actuellement dans l’environnement virtuel dédié à votre projet. Ce nom correspond à l’environnement virtuel créé et activé par Poetry pour isoler les dépendances de ce projet.

Tant que cet environnement est actif, toutes les commandes Python que vous lancez s’exécutent dans cet espace isolé. Cela garantit que votre projet utilise uniquement les bibliothèques et dépendances installées dans cet environnement, sans interférer avec d’autres projets ou avec l’installation globale de Python sur votre ordinateur.

## EXÉCUTION DU PROJET

### Version classique (données fixes)

```text
        (base) NomDeUtilisateur Projet-ARME % cd Resolution
        (base) NomDeUtilisateur Resolution % uv run app.py
```
Résultats :

- Coût minimal
- Bénéfice maximal
- Visualisation 3D
- Étude de sensibilité

### Version généralisée (données dynamiques)

Saisie utilisateur :
```text 
        (base) NomDeUtilisateur Projet-ARME % cd Optimisation_militaire
        (base) NomDeUtilisateur Optimisation_militaire % uv run interface.py 
        (base) NomDeUtilisateur Optimisation_militaire % uv run app.py
```
Résultats :

- Tables du primal et dual
- Comparaison des solutions
- Courbe coût vs bénéfice
