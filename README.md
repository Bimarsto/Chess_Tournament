# Chess_Tournament# OpenClassrooms: Projet 4: Chess Tournament
>Ce programme a été créé dans le cadre du projet 4 du parcours "Développeur d'application - Python" d'OpenClassrooms.
Il s'agit d'un gestionnaire de tournois d'échecs.
## Installation:
Commencez tout d'abord par installer Python.
Lancez ensuite la console, placez-vous dans le dossier de votre choix puis clonez ce repository :
```
git clone https://github.com/Bimarsto/Chess_Tournament.git
```
Placez-vous dans le dossier OC_P4_ChessTournament, puis créez un nouvel environnement virtuel :
```
python -m venv env
```
Ensuite, activez-le.
Windows:
```
env\scripts\activate.bat
```
Linux:
```
source env/bin/activate
```
Il ne reste plus qu'à installer les packages requis :
```
pip install -r requirements.txt
```
Vous pouvez enfin lancer le script :
```
python main.py
```

## Utilisation
Le menu principal est divisé en 4 options.
### 1) Créer un nouveau tournoi
- Le programme vous permet de gérer des tournois d'échecs. Lors de la première utilisation, sélectionnez "Créer un tournoi", puis laissez vous guider.
- Si aucun joueur n'est présent dans la base de donnée, vous serez invité à en créer.
- Lors d'un tournoi, vous serez invité, pour chaque round, à rentrer les résultats de chaque match. A la fin de chaque round, un classement sera généré.
### 2) Accéder à un tournoi
- Cette section vous permet de charger un tournoi depuis la base de donnée.
- Une fois le tournoi chargé, vous serez invité à le continuer.
### 3) Ajouter un nouveau joueur
- Lorsque vous sélectionnez cette option, vous êtes invité à rentrer l'ensemble des informations du joueur à créer.
### 4) Modifier un joueur
- Avec cette option, vous pouvez modifier les informations d'un joueur.
- Une fois sélectionné, vous serez invité à choisir le joueur puis l'information du joueur à modifier.
### 5) Les rapports
- Cette section vous permet de générer différents rapports.

## Générer le rapport Flake8
- Installez flake8 avec la commande : 
```
pip intall flake8-html
```
- S'il n'existe pas, créer un fichier setup.cfg
- Ecrire le texte suivant dedans :
```
[flake8]
exclude = .git,.gitignore,./env,.idea,__pycache__
max-line-length = 119
```
- Tapez la commande:
```
flake8 --format=html --htmldir=flake-report
```
- Le rapport sera généré dans le dossier flake8.