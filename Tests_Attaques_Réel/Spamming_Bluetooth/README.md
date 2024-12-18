### Attaque de Spam de Notifications avec Bluetooth LE à l’aide de l’application Android **Bluetooth LE Spam**  
---

### 1. Présentation de l'attaque  
L’attaque de spam de notifications via Bluetooth Low Energy (BLE) utilise une application Android rootée, telle que **Bluetooth LE Spam**, pour envoyer un flux continu de messages non sollicités aux appareils cibles. Cette méthode est simple et efficace, rendant les appareils Bluetooth inutilisables en saturant leur système de notifications.  

L’application permet d’automatiser plusieurs étapes clés :  
- Découverte des appareils BLE à proximité.  
- Sélection de la cible parmi les périphériques détectés.  
- Envoi massif de notifications ou messages publicitaires via le protocole BLE.  

#### Objectifs principaux :  
- Perturber l’expérience utilisateur de l’appareil ciblé.  
- Démontrer la vulnérabilité de certains périphériques à ce type d’attaque.  
- Éventuellement préparer des attaques secondaires, comme un déni de service ou une tentative de pairage forcé.  

---

### 2. Préparation de l’attaque  

#### Prérequis :  
- Un smartphone Android rooté avec Bluetooth 4.0 ou supérieur.  
- L’application **Bluetooth LE Spam** installée. Cette application, en mode root, donne accès à des fonctionnalités avancées pour manipuler le protocole BLE.  
- Autorisations root pour garantir le bon fonctionnement de l’application.  

#### Étapes préparatoires :  
1. **Téléchargement et installation** :  
Téléchargez l’APK de l’application **Bluetooth LE Spam** depuis une source fiable (par exemple, un dépôt GitHub ou une archive pour chercheurs en sécurité).  
Activez l’installation d’applications depuis des sources inconnues dans les paramètres Android.  
Installez l’APK et vérifiez que les autorisations root sont bien configurées.
     

2. **Configuration du smartphone Android** :  
Activez le Bluetooth sur l’appareil.
Placez-vous dans une zone où des appareils BLE sont activés et accessibles.  

4. **Environnement cible** :  
Assurez-vous d’être à proximité des appareils que vous souhaitez cibler. La portée BLE est généralement de 10 à 30 mètres, en fonction de la puissance du signal et des obstacles.  

---

### 3. Étapes de l’attaque  

#### 3.1 Découverte des périphériques BLE  
Lancez l’application **Bluetooth LE Spam** qui est disponible juste en haut Bluetooth_Spam_BLE.apk.
Utilisez la fonction de balayage BLE pour détecter les périphériques à proximité.  


#### 3.3 Envoi massif de notifications  
Utilisez l’application pour envoyer un flot continu de notifications via le protocole GATT (Generic Attribute Profile).  
Configurez les paramètres de l’attaque :  
**Intervalle d’envoi** : Pour augmenter l’impact, réduisez l’intervalle entre les notifications.  
**Contenu des notifications** : Certains appareils affichent les messages, d'autres les ignorent. Vous pouvez personnaliser le texte ou envoyer des valeurs aléatoires.  
L’application **Bluetooth LE Spam** gère ces étapes automatiquement en exploitant la vulnérabilité des services GATT de l’appareil cible.  

#### Indicateurs de succès :  
Le périphérique cible affiche un grand nombre de notifications ou ralentit considérablement.  
Certains appareils peuvent redémarrer ou désactiver temporairement leur Bluetooth pour se protéger.  

---

### 4. Phase de test  

1. **Configuration de l’environnement test** :  
Configurez un périphérique Bluetooth pour observer l’impact. Dans notre cas, nous utiliserons un téléphone Android, un iPhone ainsi que un ordinateur Windows.
Assurez-vous que l’appareil cible est à portée et en mode découverte BLE, où simplement avec le Bluetooth d'allumé car il sera automatiquement activé si le Bluetooth l'est aussi.   

2. **Déclenchement de l’attaque sur Windows** :  
Lancez l’envoi des notifications via **Bluetooth LE Spam**. Dans notre cas nous nous rendrons là où toutes les attaques sont stockées et nous allons séléctionner pour commencer le sapm de Notification Windows. Pour cela, on se rend dans la section Kitchen Sink Collection (terme souvent utilisé dans le contexte du développement ou des environnements de démonstration pour désigner un ensemble exhaustif d'exemples, de fonctions ou de tests dans un seul package) qui regroupe un grand nombre d'attaques disponible puis on se rendra dans Swift Pairing List (Au lieu de chercher manuellement les appareils à proximité, la Swift Pairing List affiche automatiquement les appareils Bluetooth disponibles lorsque certains critères sont remplis.) qui contient un certain nombre de Device qui seront les appareils qui tentent de se connecter.
![image](https://github.com/user-attachments/assets/1fa3abb9-6f47-4cac-a66b-7c44553448d9)

Une fois cela séléctionner on peut appuyer sur le Bouton Play tout en séléctionnent la liste afin dee répééter ce Spam avec différents Devices. Sur notre ordinateur Windows avec le bluetooth allumé, on obtient des notifications demandant de se connecter à l'appareil portant le nom de Device X avec X un numéro quelconque : 

![image](https://github.com/user-attachments/assets/2be61f94-5c53-43df-a4bd-86738b30c6db)

Si l'on tente de fermer la fenêtre alors, elle se ferme et une autre notification apparait. On a donc bien réussis

3. **Déclenchement de l’attaque sur iPhone/iOS** :  
Même principe que précédemment sauf que cette fois-ci, nous allons sur une autre page qui est la page de iOS Action Modals List (Les modales d’action sont des éléments d'interface utilisateur qui permettent de présenter des choix ou des interactions spécifiques dans une vue temporaire qui s’affiche par-dessus le contenu principal.) Elle contient différent appareil de l'écosystème Apple et qui vont demander de se connecter à chaque fois que l'appareil est allumé. La page de l'application contient ceci:
![image](https://github.com/user-attachments/assets/38879a48-dbcc-4153-8438-40b00c0e9acb)



5. **Exemple d’effet sur la cible** :  
   - Une montre connectée peut afficher une avalanche de messages sur son écran.  
   - Un casque Bluetooth peut perdre la connexion avec son appareil maître.
   - Blocage ou ralentissement de l’interface utilisateur.  
   - Batterie qui se vide rapidement à cause du traitement des requêtes.  
   - Déconnexion ou désactivation du Bluetooth.    

---

### 5. Contre-mesures  

#### Pour les utilisateurs :  
- Désactivez le Bluetooth lorsqu’il n’est pas utilisé.  
- Activez les paramètres de confidentialité pour limiter la découverte de votre appareil.  
- Utilisez des appareils disposant de protocoles sécurisés contre le spam BLE.  

#### Pour les fabricants :  
- Implémentez des filtres pour limiter la fréquence des messages entrants via BLE.  
- Bloquez les requêtes provenant de sources non appariées.  
- Adoptez les dernières versions de Bluetooth Core Specification avec des protections renforcées contre ce type d’attaque.  

---

### 6. Conclusion  

L’attaque de spam de notifications via Bluetooth LE est un exemple pratique des vulnérabilités des appareils connectés. Avec une application comme **Bluetooth LE Spam**, un smartphone Android rooté peut devenir un outil puissant pour perturber les périphériques BLE à proximité.  
