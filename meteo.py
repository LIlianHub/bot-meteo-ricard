from meteofrance_api import MeteoFranceClient
import os

os.chdir("/home/lilian/Bureau/Python/Twitter/bot-meteo-ricard")

def RecupMeteo():
    ville_ensoleille = set()
    ville_eclairci = set()

    # Init client
    client = MeteoFranceClient()

    liste_ville = RecupVille()

    for ville in liste_ville:
        # On recherche la ville avec son nom
        liste_position = client.search_places(ville)
        ma_position = liste_position[0]

        # Fetch weather forecast for the location
        ma_position_prevision = client.get_forecast_for_place(ma_position)
        ma_position_prevision_par_jour = ma_position_prevision.daily_forecast

        # chaque case de la liste ma_position_prevision_par_jour
        # est un dico sur la meteo pour chaque jour ! (la case 0 c'est aujourdhui)
        # on cherche l'info weather12H puis l'element desc qui contient 
        # l'etat glocale de la meteo

        # Affichage total (optionnel)
        """for jour in ma_position_prevision_par_jour:
            for cle, valeur in jour.items():
                print("l'élément de clé", cle, "vaut", valeur)
            print(10*"-")"""
        
        # L'info importante
        info = ma_position_prevision_par_jour[0]["weather12H"]["desc"]
        
        if(info == "Ensoleillé"):
            ville_ensoleille.add(ville)
            print(f"Ville ensoleillée detéctée: {ville}")
            
        elif(info == "Eclaircies"):
            ville_eclairci.add(ville)
            print(f"Ville éclaircie detéctée: {ville}")
        else:
            ville_eclairci.add(ville)
    
    return ville_ensoleille, ville_eclairci

            

def RecupVille():
    # Renvoie un ensemble avec le nom des villes dans le fichier
    liste_ville = set()
    with open("cache/villes", "r", encoding = "utf8") as f:
        for ligne in f:
            liste_ville.add(ligne.rstrip())
    return liste_ville
    