Attaque de Cracking WPA2 Password avec Wifinvite

L’attaque de cracking de mot de passe WPA2, qui est l’une des méthodes de sécurisation des réseaux Wi-Fi les plus courantes, consiste à récupérer le mot de passe du réseau pour y accéder sans autorisation. Dans ce cadre, l'outil Wifite est fréquemment utilisé, car il permet d’automatiser le processus de recherche et de craquage des réseaux Wi-Fi protégés par WPA/WPA2, WEP, et d'autres protocoles de sécurité. Cette attaque comporte plusieurs étapes techniques précises, que je vais détailler ici.

### 1. Présentation de WPA2 et des faiblesses exploitables
WPA2 (Wi-Fi Protected Access II) est une norme de sécurité pour les réseaux Wi-Fi qui utilise le chiffrement AES (Advanced Encryption Standard) et le protocole CCMP (Counter Mode Cipher Block Chaining Message Authentication Code Protocol) pour sécuriser la connexion. Bien que WPA2 soit robuste, il présente certaines vulnérabilités, notamment contre les attaques par force brute et dictionnaire, principalement lorsqu'un mot de passe faible ou simple est utilisé. 

### 2. Préparation de l'attaque avec Wifite
Wifite est un outil de ligne de commande conçu pour automatiser le processus de craquage des réseaux Wi-Fi. Avant de lancer l'attaque, il est nécessaire de :
- Configurer une interface Wi-Fi en mode moniteur pour écouter les réseaux Wi-Fi environnants. Cela signifie que la carte réseau doit être capable d'intercepter les paquets qui circulent sur le réseau. Wifite va pouvoir le faire tout seul lorsque nous lancons la commande qui va avec wifivite :
 
- Identifier le réseau cible en utilisant des outils comme Airodump-ng, intégré dans Wifite, qui analyse les réseaux disponibles et identifie les points d’accès (SSID) et leur niveau de sécurité (WEP, WPA, WPA2).

Wifite va pouvoir le faire tout seul lorsque nous lancons la commande qui va avec wifivite :

![image](https://github.com/user-attachments/assets/6cc7ea31-69c6-4400-bc9b-99d27b8c8ded)

### 3. Capture du Handshake WPA2
La phase cruciale de l'attaque consiste à capturer le handshake WPA2, qui est un échange de clés entre le routeur et un périphérique client lorsqu’une connexion est établie. Wifite effectue cette opération en :

1. Forçant la déconnexion d’un périphérique déjà connecté (attaque de de-authentication), ce qui oblige l’appareil à se reconnecter. Cette étape se fait généralement via une attaque de-auth qui envoie des paquets de désauthentification pour forcer un périphérique à quitter temporairement le réseau.
2. Lors de la reconnexion du périphérique, Wifite peut capturer le handshake. Cette capture est essentielle, car elle contient des informations codées (en hachage) sur le mot de passe.

Le handshake ne donne pas directement le mot de passe, mais il est nécessaire pour le processus de déchiffrement ultérieur.

### 4. Déchiffrement du Handshake via des attaques par dictionnaire ou brute force
Une fois le handshake capturé, l'étape suivante est de tester des mots de passe jusqu'à trouver le bon. Cela peut se faire de deux manières principales :
- Attaque par dictionnaire : Wifite utilise un fichier de mots de passe prédéfini (fichier de dictionnaire) et teste chaque mot de passe pour voir s’il correspond à celui du handshake. Cette approche est rapide si le mot de passe est simple ou fait partie des mots de passe courants.
- Attaque par force brute : Cette approche consiste à tester toutes les combinaisons possibles jusqu’à trouver la bonne. Elle est bien plus longue et rarement efficace pour des mots de passe forts ou complexes, mais elle peut réussir pour des mots de passe courts ou peu complexes.

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
