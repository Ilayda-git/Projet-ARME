# INTRODUCTION:

Ce projet ARME simule la planification d’achats d’armements pour le pays fictif PATIBULAIRE, qui doit satisfaire des besoins minimaux en défense tout en minimisant le coût total.

ProjetARME est une bibliothèque Python conçue pour résoudre des problèmes de programmation linéaire. Elle propose une interface claire et facile à utiliser, adaptée à divers domaines tels que la logistique, la gestion de la production ou la planification.

# Fonctionnalités principales

- Résolution de problèmes de programmation linéaire appliqués à la planification d’achats militaires.
- Version classique avec données fixes.
- Version généralisée avec interface utilisateur et visualisations graphiques.
- Étude de sensibilité sur les prix.
- Tests unitaires pour garantir la robustesse du code.

Ce module permet de résoudre différents types de problèmes. L'un d'eux, appelé ProblemePrimal, vise à minimiser les dépenses du consommateur pour différents lots fournis par un ou plusieurs vendeurs. L'autre, appelé ProblemeDual, vise à maximiser le profit d'un vendeur unique.

Ce travail illustre les enjeux économiques et stratégiques liés à l’achat d’armements dans un cadre optimisé.

# STRUCTURE DU PROJET:

Le projet est organisé en plusieurs dossiers distincts pour bien séparer les différentes parties. 
- Le dossier DATA contient les fichiers JSON qui regroupent les données utilisées, telles que les coûts, contraintes et besoins servant aux calculs d’optimisation. 
- Le dossier optimisation_militaire contient la version généralisée du projet avec quatre fichiers principaux : main.py pour lancer cette version, generalisation.py qui inclut la modélisation étendue, graphique.py qui fournit les fonctions de visualisation, et interface.py qui gère l’interaction utilisateur. 
- Le dossier resolution contient la version classique du problème avec trois fichiers : main.py, question.py qui définit les classes PrimalProblem et DualProblem ainsi que leurs méthodes de résolution, et graphique.py pour les visualisations graphiques. 
- Enfin, le dossier test regroupe deux fichiers de tests unitaires, test_generalisation.py et test_question.py, qui permettent de vérifier la validité et la robustesse du code.

projet_arme/
│
├── DATA/
│   └── data.json                 # Fichier JSON contenant les données (coûts, contraintes, besoins)
│
├── optimisation_militaire/
│   ├── graphique.py              # Fonctions pour visualisations graphiques (version généralisée)
│   ├── generalisation.py         # Modélisation généralisée du problème d'optimisation
│   ├── interface.py             # Interface utilisateur pour interagir avec la version généralisée
│   └── main.py                  # Script principal pour lancer la version généralisée
│
├── resolution/
│   ├── graphique.py              # Fonctions graphiques pour la version classique
│   ├── main.py                   # Script principal pour lancer la version classique
│   └── question.py               # Définition des classes PrimalProblem et DualProblem
│
└── test/
    ├── test_generalisation.py   # Tests unitaires pour la version généralisée
    └── test_question.py          # Tests unitaires pour la version classique

# EXIGENCE:
Python3.11

# INSTALATION :
## VIA PIP
python -m pip install git+https://github.com/Ilayda-git/Projet-ARME.git

Une fois la bibliothèque installée sur votre machine, vous pouvez l’utiliser directement dans vos scripts Python. La création d’un environnement virtuel n’est alors pas indispensable, bien qu’elle reste recommandée pour isoler les dépendances d’un projet.

## VIA LE CLONAGE ET POETRY
- Clonez le package avec la commande suivante :
git clone https://github.com/Ilayda-git/Projet-ARME.git

- Ouvrez un terminal dans le répertoire racine du package avec la commande :
cd ./Projet-ARME

- Créez un environnement virtuel et installez les dépendances avec la commande :
python -m poetry install

- Activez l'environnement virtuel avec la commande :
python -m poetry env activate

(arme-smQvmoZ_-py3.12)= Lorsque vous voyez (arme-smQvmoZ_-py3.12) affiché dans votre terminal, cela signifie que vous êtes actuellement dans l’environnement virtuel dédié à votre projet. Ce nom correspond à l’environnement virtuel créé et activé par Poetry pour isoler les dépendances de ce projet.

Tant que cet environnement est actif, toutes les commandes Python que vous lancez s’exécutent dans cet espace isolé. Cela garantit que votre projet utilise uniquement les bibliothèques et dépendances installées dans cet environnement, sans interférer avec d’autres projets ou avec l’installation globale de Python sur votre ordinateur.
