### **Le cracking de mot de passe WPA2**

Le cracking de mot de passe WPA2 est une technique utilisée pour accéder à un réseau WiFi protégé en exploitant des failles dans le protocole d'authentification. Cette méthode permet à un attaquant de capturer un **handshake WPA** et de tenter de deviner la clé partagée (PSK) du réseau.

---

### **Fonctionnement détaillé du cracking WPA2**

Voici les étapes clés pour effectuer un craquage de mot de passe WPA2 :

#### **1. Identification du réseau cible**
- L’attaquant utilise des outils comme **airodump-ng** pour scanner les réseaux disponibles.  
- Les informations essentielles sont collectées, notamment :  
  - Le **SSID** (nom du réseau).  
  - Le **BSSID** (adresse MAC du point d’accès).  
  - Le **canal** utilisé par le réseau.  
  - La liste des clients connectés.  

#### **2. Capture du handshake WPA**
- Le **handshake WPA** est une séquence d’échanges entre un point d’accès et un client lors de la connexion.  
- Pour capturer ce handshake, deux méthodes sont possibles :  
  1. Attendre qu’un client se connecte naturellement au réseau.  
  2. Provoquer une reconnexion forcée en utilisant une attaque de désauthentification avec **aireplay-ng**.  
- Le handshake capturé est ensuite sauvegardé dans un fichier `.cap`.  

#### **3. Validation du handshake capturé**
- Avant de lancer le craquage, l’attaquant vérifie que le handshake capturé est exploitable.  
- Des outils comme **Wireshark**, **Cowpatty** ou **Aircrack-ng** sont utilisés pour cette validation.  

#### **4. Craquage du mot de passe**
- Une fois le fichier `.cap` validé, l’attaquant utilise deux méthodes principales pour deviner le mot de passe :  
  1. **Attaque par dictionnaire** : Essaye des mots de passe préenregistrés dans un fichier (comme **rockyou.txt**).  
  2. **Attaque par force brute** : Teste toutes les combinaisons possibles de caractères.  
- Des outils comme **Hashcat** permettent d’accélérer ces attaques en utilisant la puissance de calcul des GPU.  

#### **5. Connexion au réseau**
- Une fois le mot de passe découvert, l’attaquant peut se connecter au réseau WiFi, l’utiliser pour accéder à Internet, ou lancer des attaques supplémentaires.  

---

### **Applications avancées du cracking WPA2**

Le cracking de WPA2 peut être exploité pour réaliser diverses attaques sophistiquées :

#### **1. Interception de trafic réseau**
- Une fois connecté, l’attaquant peut surveiller et analyser le trafic réseau pour intercepter :  
  - Les identifiants de connexion.  
  - Les sessions web non sécurisées (HTTP).  
  - Les données personnelles échangées.  

#### **2. Attaques de type "Man-in-the-Middle" (MiTM)**
- L’attaquant redirige le trafic réseau des victimes à travers son appareil, permettant :  
  - L’interception des données sensibles.  
  - La modification des requêtes ou réponses (injection de malwares, redirection vers des sites malveillants).  

#### **3. Déni de service ciblé**
- Une fois connecté, l’attaquant peut surcharger le réseau ou déconnecter les autres utilisateurs légitimes via des attaques de désauthentification répétées.  

#### **4. Exécution de scripts malveillants**
- L’attaquant peut injecter des scripts malveillants dans les sites visités par les utilisateurs, facilitant la compromission de leurs appareils.  

---

### **Outils couramment utilisés pour le cracking WPA2**

1. **Aircrack-ng Suite**  
   - **airodump-ng** : Pour scanner les réseaux et capturer les handshakes.  
   - **aireplay-ng** : Pour lancer des attaques de désauthentification.  
   - **aircrack-ng** : Pour craquer le mot de passe via des attaques par dictionnaire ou force brute.  

2. **Hashcat**  
   - Exploite la puissance des GPU pour accélérer le processus de craquage.  

3. **Cowpatty**  
   - Permet de vérifier et de craquer les handshakes capturés.  

4. **Wireshark**  
   - Analyse les fichiers `.cap` et valide la capture des handshakes.  

5. **John the Ripper**  
   - Utile pour le craquage des mots de passe en complément des dictionnaires.  

6. **Dictionnaires de mots de passe**  
   - Contiennent des mots de passe courants à tester (exemple : **rockyou.txt**).  

---

### **Comment se protéger contre le cracking WPA2**

#### **1. Utiliser des mots de passe robustes**
- Évitez les mots de passe simples ou courants comme "password" ou "12345678".  
- Optez pour des mots de passe longs et complexes combinant lettres, chiffres et symboles.  

#### **2. Adopter le WPA3**
- WPA3, la norme successor du WPA2, améliore considérablement la sécurité en rendant les attaques de craquage hors ligne presque impossibles.  

#### **3. Désactiver le WPS**
- Le **Wi-Fi Protected Setup (WPS)** est vulnérable à des attaques, facilitant le craquage des réseaux. Désactivez cette fonctionnalité si elle est activée.  

#### **4. Activer le 802.11w (PMF)**
- Le **Protected Management Frames** protège contre les attaques de désauthentification, rendant la capture de handshakes plus difficile.  

#### **5. Surveiller le réseau**
- Utilisez un système de détection d’intrusion WiFi (WIDS) pour identifier des activités suspectes ou des connexions non autorisées.  

#### **6. Changer régulièrement le mot de passe**
- Modifiez le mot de passe WiFi périodiquement pour limiter les risques de compromission.  

#### **7. Utiliser un VPN**
- En cryptant tout le trafic entre votre appareil et Internet, un VPN empêche qu’un attaquant connecté au même réseau puisse intercepter vos données.  

---

### **Faiblesses du WPA2 et limites de l'attaque**

#### **1. Protocoles modernes comme WPA3**
- Les réseaux utilisant WPA3 résistent aux méthodes classiques de capture et de craquage des handshakes.  

#### **2. Temps et puissance de calcul**
- Les mots de passe longs et complexes augmentent drastiquement le temps nécessaire pour un craquage par force brute.  

#### **3. Détection d’activités suspectes**
- Les appareils modernes et certains routeurs peuvent détecter les attaques de désauthentification et d’autres activités anormales sur le réseau.  

---

### **Résumé**

Le cracking de WPA2 reste une technique puissante pour accéder à un réseau WiFi protégé, mais il nécessite une préparation minutieuse, des outils spécialisés, et des ressources de calcul importantes. Heureusement, des mesures comme l’utilisation de WPA3, la surveillance des réseaux et des mots de passe robustes permettent de se prémunir contre cette attaque.
