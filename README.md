<h1>Monte Carlo pour le Puissance 4 en Python</h1>

<h2>Introduction</h2>
Dans ce workshop, vous apprendrez à implémenter l'algorithme de Monte Carlo pour développer une IA capable de jouer au Puissance 4. Vous découvrirez comment simuler des parties de jeu, évaluer des stratégies, et optimiser les performances de l'IA.

<h2>Installation</h2>
Avant de commencer, assurez-vous d'avoir Python installé sur votre système.

Installation Fedora :

```bash
sudo dnf update
sudo dnf install python3
sudo dnf install python3-pip
```

Installation Ubuntu :

```bash
sudo apt update
sudo apt install python3
sudo apt install python3-pip
```

<h1>Configuration du Projet</h1>
<h2>Étape 1 : Préparation de l'Environnement</h2>
Clonez le repository et préparez votre environnement.

```
git clone git@github.com:NicolasPoupon/Workshop-MonteCarlo.git
```

<h2>Étape 2 : Comprendre le Jeu de Base</h2>
Renseignez vous sur l’algorithme de Monte-Carlo.
Familiarisez-vous avec le code de base du jeu Puissance 4. Jouez quelques parties contre l'IA qui joue aléatoirement pour comprendre la mécanique du jeu.

```bash
./main.py
```

<h1>Exercices</h1>

<h2>Exercice 1 : Evaluer le résultat d’une partie</h2>
Afin de mettre en place l’algorithme il va falloir que l’ia comprenne ce qu’est une partie gagnante, nulle ou perdante.
Pour cela vous allez de voir implémetez une fonction dans la classe Puissance4. La fonction doit return 1 si l’ia gagne, -1 si le joueur gagne et 0 en cas de partie null.
Aidez vous de la fonction "is_finished".


<h2>Exercice 2 : Simulation de Partie Aléatoire</h2>
Maintenant qu’on arrive à classer les parties il va falloir simuler des parties.
Pour cela vous devez implémenter dans la class Puissance4 une fonction pour simuler des parties aléatoires à partir d'un état de jeu donné.
Le but est de copier l’état du jeu actuel et de jouer un premier coup aléatoire pour l’ia puis un coup aléatoire pour l’adversaire et ansi de suite jusqu’a ce qu’une partie se termine.
Vous devez renvoyer le résultats de la partie à la fin de votre fonction.
Vous pouvez commencer de cette manière :

```python
def simulate_random_game(self, start_player):
        simulation = copy.deepcopy(self)
```

<h2>Exercice 3 : Implémentation Basique de Monte Carlo</h2>
Créez une fonction qui utilise la fonction de l’exercice précédent afin tester chacun des coups possible. Le résultat de chaque partie doit être sauvegardé dans un tableau.

<h2>Exercice 4 : Améliorer la fonction d’évaluation des parties</h2>
Modifiez la fonction d’évaluation des parties afin que l’évalation soit plus pertinente. Pour cela vous devez prendre en compte le nombre de tours qu’a duré la simulation. Plus une partie est perdu vite plus le score attribué doit être négatif, à l’inverse plus une partie est gagné vite plus le
score attribué a la partie doit être haut.

<h2>Exercice 5 : Choisir le bon coup</h2>
Maintenant faites choisir à votre ia le meilleure coup en fonction de vos résultats de simulation.

<h2>Exercice 6 : Faire un grand nombre de simulations </h2>
Modifier votre fonction qui lance les simulation afin qu’elle prenne en argument le nombre de simulations à lancer.


<h2>Exercice 7 : Combiner le Monte Carlo avec un autre algorithm</h2>
Pour le moment les simulations des parties sont faites à partir de coups totalements aléatoires.
Pour que le résultat soit pertinent il faut améliorer la qualité des simulations en utilisant un autre algorithm.
Pour ce dernier exercise vous devez combiner le Monte Carlo avec un algorithm de votre choix.

<h2>Exercice 8 : Parallélisation des Simulations</h2>
Exécuter plusieurs simulations simultanément pour améliorer les performances avec des threads.
