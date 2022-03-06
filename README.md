# Bot Twitter Ricard

## Présentation
Bot twitter qui permet de chercher automatiquement via l'API de MétéoFrance la météo des villes

Si la météo est propice à boire un Ricard (grand soleil ou soleil timide derrière des nuages) alors cette ville apparaitra dans un tweet
posté de manière hebdomadaire à 10h !

En l'occurence voici le lien de mon bot: https://twitter.com/Meteo_du_Ricard

## Pré-requis

Avoir installé le module python tweepy: ```pip install tweepy```

https://github.com/tweepy/tweepy

Le module python meteo-france: ```pip install meteofrance-api```

https://github.com/hacf-fr/meteofrance-api

## Informations

Les villes à tester sont stockées dans le fichier **/cache/villes**

Afin de se connecter à l'API twitter il faut mettre les informations de votre compte dans le fichier **/cache/id** de cette manière

- 1ère ligne: API key
- 2ème ligne: API secret key
- 3ème ligne: Token
- 4ème ligne: Token secret

## Utile

Commande **Cron** pour activer le script tout les matins à 10h: ```00 10 * * * python3 /path_to_your_file/main.py >> /path_to_your_file/log.txt```

