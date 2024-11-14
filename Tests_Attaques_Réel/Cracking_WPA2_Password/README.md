Attaque de Cracking WPA2 Password avec Wifinvite
Description

L'attaque consiste à exploiter les failles dans la sécurité des réseaux WPA2 pour capturer le handshake et tenter de cracker le mot de passe. Wifinvite est un outil puissant qui permet d’automatiser ce processus. Cet outil combine la capture de handshake et le cracking à l’aide d’un dictionnaire ou d’une attaque brute force.
Fonctionnement de l'attaque :

  Scan des réseaux disponibles
  Wifinvite commence par scanner les réseaux Wi-Fi à proximité pour identifier les points d'accès cibles.

  Capture du Handshake WPA2
  Une fois un réseau cible sélectionné, l'outil force une reconnexion des clients (deauthentication) afin de capturer le handshake WPA2.

  Cracking du mot de passe 
  Wifinvite tente de cracker le mot de passe capturé en utilisant un dictionnaire ou une méthode brute force.

Explication des Résultats :
Si le mot de passe est trouvé, il sera affiché dans la console.
En cas d’échec, il est possible de tester avec un autre dictionnaire ou de modifier les paramètres de l'attaque.

Configuration avec les captures d'écrans :

Prévention :
Pour protéger un réseau contre ce type d'attaque :
Utilisez des mots de passe longs et complexes.
Désactivez WPS (Wi-Fi Protected Setup).
Surveillez les connexions suspectes à votre réseau.
