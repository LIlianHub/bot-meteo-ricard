import tweepy
import datetime
import os
import os.path as op

#Outil
NOM_MOIS = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aôut", "Septembre", "Octobre", "Novembre", "Décembre"]
os.chdir("/home/lilian/Bureau/Python/Twitter/bot-twitter-ricard")

def Authentification_twitter():
    if op.isfile("cache/id"):
        fichier = open("cache/id", "r")

        # Clés de votre application
        consumer_key = fichier.readline()
        consumer_key = consumer_key.rstrip()
        consumer_secret = fichier.readline()
        consumer_secret = consumer_secret.rstrip()
        # le access_token est le token de l'application twitter que nous avons créée précédement
        access_token = fichier.readline()
        access_token = access_token.rstrip()
        access_token_secret = fichier.readline()
        access_token_secret = access_token_secret.rstrip()

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)
        fichier.close()
        return api
    else:
        return 0

def EnvoieTweet(API, jour_ensoileille, jour_eclaircie):
    date_du_jour = datetime.date.today()
    message = "Nous somme le " + str(date_du_jour.day) + " " + NOM_MOIS[int(date_du_jour.month) - 1] + " " + str(date_du_jour.year) + ",\n"
    message += "Aujourd'hui les villes où il fera bon de prendre un Ricard en terrasse au soleil sont: \n"

    for ville in jour_ensoileille:
        message += "☀️ " + ville + "\n"
    
    for ville in jour_eclaircie:
        message += "⛅ " + ville + "\n"
    
    API.update_status(status = message)




    
    




