# <u>PyJackGame</u>

## 

##### Modules:

```
random  # Pour générer les nombres aléatoires et piocher les cartes.
typing  # Pour indiquer des arguments pour des fonctions
# Ces modules sont build-in.
```

##### Structure:

```
BlackJackGame	# L'objet du jeu, pour pouvoir le re-utiliser facilement
├─ __init__(self, nbr_jrs)  # Initialiser les valeurs
├─ reset_cards(self)  # Réinitialise les valeurs, permet de refaire une partie.
├─ next_round(self, as_function, retire_functio)  # Passe au prochain tour.
├─ get_score(self)  # Donne le score des joueurs (à faire en fin de jeu).

main  # Fonction "test" (dans le cas où on veut utiliser ce fichier en tant que module)
├─ as_test(joueur) # Demande au joueur 0 au cas où il recupère un AS.
├─ stop_test(joueur) # Demande au joueur 0 si il veut arréter le jeu si score égale ou supérieur à 16.
```

Dans le code, toutes les fonctions sont commentés, pour que ce soit le plus simple à re-utiliser.