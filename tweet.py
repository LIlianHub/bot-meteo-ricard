import tweepy
import datetime
import os
import os.path as op

#Outil
NOM_MOIS = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aôut", "Septembre", "Octobre", "Novembre", "Décembre"]
os.chdir("/home/lilian/Bureau/Python/Twitter/bot-meteo-ricard")
#limite de 270 au lieu de 280 pour être large
MAX_SIZE_TWEET = 270

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
    print(f"tweet du {date_du_jour}")

    message = "Nous somme le " + str(date_du_jour.day) + " " + NOM_MOIS[int(date_du_jour.month) - 1] + " " + str(date_du_jour.year) + ",\n"
    message += "Aujourd'hui les villes où il fera bon de prendre un Ricard en terrasse au soleil sont: \n"

    for ville in jour_ensoileille:
        message += "☀️ " + ville + "\n"
    
    for ville in jour_eclaircie:
        message += "⛅ " + ville + "\n"

    # Si le tweet est trop long:
    if(len(message) > MAX_SIZE_TWEET):
        # on split par ligne
        message_separe = message.split("\n")

        # Premier tweet
        message_court = ""
        parcours = 0

        # on remplit le premier tweet
        while((len(message_court) + len(message_separe[parcours])) < MAX_SIZE_TWEET):
            message_court += message_separe[parcours] + "\n"
            parcours += 1

        #fleche vers le bas, pour informer de la suite
        message_court += "⬇️"

        #on recup id du tweet qu'on vient d'envoyer
        tweet = API.update_status(status = message_court)
        id_a_rep = tweet.id

        # construction du thread !
        # Tant qu'on a pas tout ecrit
        while(parcours < len(message_separe)):
            # Obligé ce mettre l'@ de la personne a qui ont repond en l'occurence ici, nous même
            message_court = "@BotRicard"
            # tant qu'on a pas tout ecrit ou que le sous message est trop long
            while((parcours < len(message_separe)) and ((len(message_court) + len(message_separe[parcours])) < MAX_SIZE_TWEET)):
                message_court += message_separe[parcours] + "\n"
                parcours += 1

            #Si jamais il y a une suite on l'informe avec une fleche vers le bas
            if(parcours < len(message_separe)):
                message_court += "⬇️"
                
            #on tweet en réponse au précédant tweet
            tweet = API.update_status(status = message_court, in_reply_to_status_id = id_a_rep)
            id_a_rep = tweet.id

    else:
        API.update_status(status = message)




    
    




