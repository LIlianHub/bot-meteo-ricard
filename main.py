from tweet import *
from meteo import *

def main():
    API_Twitter = Authentification_twitter()
    if(API_Twitter):
        print("API twitter bien chargée ...")
        print("Récupération des villes avec un beau temps ...")
        ville_ensoleille, ville_eclairci = RecupMeteo()
        print("Envoie du tweet ...")
        EnvoieTweet(API_Twitter, ville_ensoleille, ville_eclairci)
        print("Tweet envoyé, fermeture du programme ...")
    
    else:
        print("Erreur lors de l'authentification")


if __name__ == "__main__":
    main()

