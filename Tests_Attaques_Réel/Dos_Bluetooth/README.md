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
   Lancez un scan Bluetooth pour détecter les appareils dans votre environnement :  
   ```bash
   hcitool scan
   ```  
   Vous obtiendrez une liste des adresses MAC des appareils détectés. On cherchera dans notre cas des écouteurs sans fil Apple Airpods Pro 2.
   
   
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
Une fois configuré, le script exécute des commandes comme :  
```bash
l2ping -i hci0 -s <taille_paquets> -f <adresse_MAC>
```  
Par exemple :  
```bash
l2ping -i hci0 -s 600 -f 00:11:22:33:44:55
```  

#### 3.3 Exécution multi-threadée  
Le script crée plusieurs threads pour intensifier l’attaque, ce qui se traduit par une surcharge du périphérique cible.  

---

### 4. Phase de test  

1. **Configuration de l’environnement de test** :  
   - Un smartphone Android, un iPhone ou un PC avec Bluetooth activé.  
   - Lancez l’attaque en utilisant une machine Linux avec Bluetooth fonctionnel.  

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
