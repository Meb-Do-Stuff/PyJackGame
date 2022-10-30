# <u>PyJackGame</u>
[<b>GitHub</b>](https://github.com/MeblIkea/PyJackGame)<br>
Pour directement jouer au jeu, allez voir dans les [<b>Releases</b>](https://github.com/MeblIkea/PyJackGame/releases/latest)<br>
Si vous avez des questions, vous pouvez me contacter sur Discord (<b>Meb#2325</b>).
##

### Modules:

```
random  # Pour générer les nombres aléatoires et piocher les cartes.
typing  # Pour indiquer des arguments pour des fonctions.
math  # Pour la trigonométrie (j'ai tout fait sans tuto, je suis fier).
pygame  # Pour afficher le jeu.
os  # Pour charger les cartes avec moins de code (en regardant directement dans les répertoires)
sys  # Pour fermer le jeu.
textwrap  # Pour gérer les chaines de caractères trop longues.
pygame-button (pygame_button)  # Pour générer des boutons plus simplement.
pygame-textinput (pygame_textinput)  # Pour générer des cases de saisie de texte plus simplement.

# Certains de ces modules sont build-in, sinon regarder dans `requirements.txt`.
```

### Structure:

```
blackjack.py:

BlackJackGame	# L'objet du jeu, pour pouvoir le re-utiliser facilement
├─ __init__(self, nbr_jrs)  # Initialise les valeurs
├─ reset_cards(self)  # Réinitialise les valeurs, permet de refaire une partie.
├─ next_round(self, as_function, retire_functio)  # Passe au prochain tour.
├─ get_score(self)  # Donne le score des joueurs (à faire en fin de jeu).

main  # Fonction "test" (dans le cas où on veut utiliser ce fichier en tant que module)
├─ as_test(joueur) # Demande au joueur 0 au cas où il recupère un AS.
├─ stop_test(joueur) # Demande au joueur 0 si il veut arréter le jeu si score égale ou supérieur à 16.
```

```
interface.py:

Cartes	# Objet cartes, réunis toutes les fonctions nécessaires à l'affichage des cartes dedans.
├─ __init__(self)  # Initialise les valeurs
├─ trigo_calc(rad, multi, centre)  # Permet de calculer la position d'une carte grâce à une valeur en radiant (+ centre optionel).

Display  # Objet de l'écran, réunis les fonctions utiles à l'affichage.
├─ __init__(self)  # Initialise les valeurs
├─ reset_error(self) # Met la valeur self.error à "".
├─ board(self) # Met le fond du plateau.
├─ update(self) # Actualise les élements à l'écran.
```

```
main.py:

setup()	# Fonction qui demande combien de joueurs dans la partie.

as_func() # Fonction qui demande au joueur si il pionche un as, si il veut l'utiliser comme 1 ou 11.
retire_func() # Fonction qui demande au joueur si il veux s'arrêter si il à plus de 16.

main # Lance le jeu
```

Dans le code, toutes les fonctions sont commentées, pour que ce soit le plus simple à lire et re-utiliser.
