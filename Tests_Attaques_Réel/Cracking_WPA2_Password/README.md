![image](https://github.com/user-attachments/assets/76ce15b9-a52c-490a-9e8d-423fb766c357)Attaque de Cracking WPA2 Password avec Wifinvite

L’attaque de cracking de mot de passe WPA2, qui est l’une des méthodes de sécurisation des réseaux Wi-Fi les plus courantes, consiste à récupérer le mot de passe du réseau pour y accéder sans autorisation. Dans ce cadre, l'outil Wifite est fréquemment utilisé, car il permet d’automatiser le processus de recherche et de craquage des réseaux Wi-Fi protégés par WPA/WPA2, WEP, et d'autres protocoles de sécurité. Cette attaque comporte plusieurs étapes techniques précises, que je vais détailler ici.

### 1. Présentation de WPA2 et des faiblesses exploitables
WPA2 (Wi-Fi Protected Access II) est une norme de sécurité pour les réseaux Wi-Fi qui utilise le chiffrement AES (Advanced Encryption Standard) et le protocole CCMP (Counter Mode Cipher Block Chaining Message Authentication Code Protocol) pour sécuriser la connexion. Bien que WPA2 soit robuste, il présente certaines vulnérabilités, notamment contre les attaques par force brute et dictionnaire, principalement lorsqu'un mot de passe faible ou simple est utilisé. 

### 2. Préparation de l'attaque avec Wifite
Wifite est un outil de ligne de commande conçu pour automatiser le processus de craquage des réseaux Wi-Fi. Avant de lancer l'attaque, il est nécessaire de :
- Configurer une interface Wi-Fi en mode moniteur pour écouter les réseaux Wi-Fi environnants. Cela signifie que la carte réseau doit être capable d'intercepter les paquets qui circulent sur le réseau. Wifite va pouvoir le faire tout seul lorsque nous lancons la commande qui va avec wifivite :
 
- Identifier le réseau cible en utilisant des outils comme Airodump-ng, intégré dans Wifite, qui analyse les réseaux disponibles et identifie les points d’accès (SSID) et leur niveau de sécurité (WEP, WPA, WPA2).

Wifite va pouvoir le faire tout seul lorsque nous lancons la commande qui va avec wifivite :
![image](https://github.com/user-attachments/assets/cb0f8aa6-7311-4d89-9b01-053a25a21e23)
Lors du lancement, on peut voir différentes choses s'afficher nottament l'interface Wifi que nous allons utilisé comme interface de monitoring qui va inspecter le traffic afin de voir ce qu'il se passe sur le réseau. Wifite nécessite le mode moniteur pour capturer des paquets et interagir avec les réseaux sans fil. Les caractéristiques de notre interface réseau sont donc bien celles-ci : 

Détection de l'Interface Wi-Fi
Interface détectée : wlp6s0. 
PHY : phy0 (identifiant physique de l'interface Wi-Fi).
Driver : rtw89_8852be (indique que la carte réseau utilise le pilote Realtek).
Chipset : Realtek Semiconductor Co. Ltd. RTL8852BE.
Description : L'interface est compatible avec les standards 802.11ax (Wi-Fi 6), ce qui est pertinent pour des attaques modernes.

![image](https://github.com/user-attachments/assets/6cc7ea31-69c6-4400-bc9b-99d27b8c8ded)
On pourra analyser sur cette image : 
1. Activation du Mode Moniteur
La première ligne confirme que l'interface Wi-Fi wlp6s0 a été configurée en mode moniteur, ce qui permet de capturer des paquets sans se connecter au réseau. Cela est une étape essentielle pour écouter les communications des réseaux environnants.

2. Liste des Réseaux Disponibles
La capture liste les réseaux Wi-Fi détectés, avec plusieurs colonnes d’informations essentielles :
NUM : Numéro d'identification du réseau dans la liste.
ESSID : Nom du réseau (SSID).
CH (Channel) : Canal utilisé par le réseau.
ENCR (Encryption) : Type de chiffrement utilisé (WPA, WPA2, WPA-E, WPA-P, etc.).
PWR (Power) : Indique la puissance du signal (en dBm), une valeur élevée reflète un réseau proche.
WPS : Si activé, cela pourrait indiquer une vulnérabilité exploitable (ce n'est pas le cas ici).
CLIENT : Nombre de clients connectés au réseau.

3. Analyse du Réseau Cible : AP_A_Attaquer
ESSID : AP_A_Attaquer (SSID choisi comme cible par l’utilisateur).
CH : Canal 6.
ENCR : WPA-P, probablement WPA2 avec un mot de passe partagé (PSK).
PWR : 64 dB, ce qui indique une bonne puissance de signal.
CLIENT : 1 client connecté, ce qui est crucial pour capturer un handshake. L'attaque peut forcer la déconnexion de ce client pour obtenir les données nécessaires lors de sa reconnexion.

4. Stratégie d'Attaque Possible
Avec ces informations, l'attaque typique contre AP_A_Attaquer suivra les étapes suivantes :

Capture du Handshake : Étant donné qu'il y a un client actif (1), une attaque de désauthentification sera déclenchée pour forcer le périphérique à se reconnecter. Le handshake sera capturé lors de la tentative de connexion.

Craquage du Handshake : Une fois le handshake obtenu, Wifite procédera à une attaque par dictionnaire ou brute force, en fonction de la configuration.

On choisira lors de cette phase l'attaque sur la point d'accès AP_A_ATTAQUER représenté par le numéro 2 c'est celui-ci que nous utiliserons.

### 3. Capture du Handshake WPA2
La phase cruciale de l'attaque consiste à capturer le handshake WPA2, qui est un échange de clés entre le routeur et un périphérique client lorsqu’une connexion est établie. Wifite effectue cette opération en :

1. Forçant la déconnexion d’un périphérique déjà connecté (attaque de de-authentication), ce qui oblige l’appareil à se reconnecter. Cette étape se fait généralement via une attaque de-auth qui envoie des paquets de désauthentification pour forcer un périphérique à quitter temporairement le réseau.
2. Lors de la reconnexion du périphérique, Wifite peut capturer le handshake. Cette capture est essentielle, car elle contient des informations codées (en hachage) sur le mot de passe.

Le handshake ne donne pas directement le mot de passe, mais il est nécessaire pour le processus de déchiffrement ultérieur.

### 4. Déchiffrement du Handshake via des attaques par dictionnaire ou brute force
Une fois le handshake capturé, l'étape suivante est de tester des mots de passe jusqu'à trouver le bon. Cela peut se faire de deux manières principales :
- Attaque par dictionnaire : Wifite utilise un fichier de mots de passe prédéfini (fichier de dictionnaire) et teste chaque mot de passe pour voir s’il correspond à celui du handshake. Cette approche est rapide si le mot de passe est simple ou fait partie des mots de passe courants.
- Attaque par force brute : Cette approche consiste à tester toutes les combinaisons possibles jusqu’à trouver la bonne. Elle est bien plus longue et rarement efficace pour des mots de passe forts ou complexes, mais elle peut réussir pour des mots de passe courts ou peu complexes.

![image](https://github.com/user-attachments/assets/2b7419b6-8f20-448e-be70-b761b0f97043)
Sur cette capture, nous voyons différentes choses. Wifite tente de capturer le PMKID (Pairwise Master Key Identifier), une méthode d'attaque rapide si le réseau le supporte.
Le message "Waiting for PMKID" indique que Wifite écoute les paquets pour tenter de récupérer cette clé. Mais on utilisera pas cette attaque, on l'interrompera donc. On utilisera par la suite le Capture de Handshake WPA. On voit sur la capture que le Handshake est détecté : Wifite détecte un nouveau client connecté au réseau : 62:9A:EE:EA:C7:30. Cet événement permet de capturer le handshake WPA, une étape critique pour le craquage des mots de passe. Le message "Captured handshake" confirme que le handshake a été obtenu avec succès.

Wifite enregistre une copie du handshake dans un fichier .cap nommé : hs/handshake_APAATTAQUER_C0-56-27-73-35-B8_2024-11-14T16-21-53.cap

Ce fichier contient les informations nécessaires pour une attaque par force brute ou par dictionnaire.

Wifite utilise trois outils pour valider l'authenticité du handshake :
Tshark : Confirme que le fichier .cap contient un handshake valide pour C0:56:27:73:35
Cowpatty : Indique également que le handshake est valide.
Aircrack-ng : Valide le handshake pour l'AP AP_A_ATTAQUER.
Cela garantit que le fichier est utilisable pour une tentative de craquage.

### 5. Analyse des résultats et connexion au réseau
Si un mot de passe correspondant est trouvé, l’attaquant peut alors utiliser ce mot de passe pour se connecter au réseau Wi-Fi ciblé. 

### Limitations et Contre-Mesures de Sécurité
Bien que l'attaque par Wifite et d’autres outils similaires soit possible, elle présente des limitations, notamment si :
- Le mot de passe est fort et long (les attaques par dictionnaire et par force brute deviennent alors presque impossibles à réussir).
- Des mécanismes de protection avancés, comme WPA3, sont utilisés. WPA3 utilise des protocoles plus robustes comme Simultaneous Authentication of Equals (SAE), qui rend les attaques par capture de handshake et par dictionnaire inutiles.

Pour se protéger contre ce type d’attaque, il est recommandé de :
- Utiliser des mots de passe forts, c'est-à-dire longs, avec des caractères spéciaux, des chiffres, et des lettres majuscules/minuscules.
- Désactiver la fonction WPS (Wi-Fi Protected Setup), souvent exploitée dans les attaques.
- Utiliser WPA3 si le routeur le supporte, car il corrige de nombreuses faiblesses de WPA2.

### Conclusion
L’attaque de cracking WPA2 avec Wifite, bien qu’accessible et automatisée, repose sur une série de faiblesses bien identifiées de WPA2. Toutefois, elle est contrée par des pratiques de sécurité comme l’utilisation de mots de passe robustes et la migration vers des standards de sécurité plus récents.
