L'attaque de désauthentification WiFi (ou "deauthentication attack") est une forme d'attaque de déni de service (DoS) qui vise à déconnecter un client d'un réseau WiFi. Elle tire parti de la manière dont le protocole WiFi gère la déconnexion des clients en envoyant des trames de désauthentification.

Fonctionnement de l'attaque de désauthentification WiFi :

Écoute des trames WiFi : L'attaquant utilise des outils comme airmon-ng pour mettre sa carte réseau en mode moniteur, ce qui lui permet de capturer les trames WiFi échangées entre un point d'accès (AP) et les clients connectés.

Injection de trames de désauthentification : L'attaquant envoie de fausses trames de désauthentification à la cible (le client ou le point d'accès). Ces trames sont envoyées en prétendant être le point d'accès (spoofing de l'adresse MAC de l'AP), ce qui force le client à se déconnecter du réseau.

Déconnexion forcée : Le client victime reçoit ces trames et se déconnecte du réseau WiFi, pensant qu'il s'agit d'une requête légitime du point d'accès.

Conséquences :

Déni de service : La cible est déconnectée du réseau, empêchant toute communication jusqu'à ce qu'elle tente de se reconnecter.
Attaques plus sophistiquées : En forçant la déconnexion d'un client, l'attaquant peut, par exemple, capturer le processus de reconnexion et tenter une attaque de type "man-in-the-middle" (MiTM) pour intercepter des informations sensibles comme des identifiants.

Outils utilisés :

Aircrack-ng suite : Une suite d'outils pour surveiller et injecter des trames WiFi.
aireplay-ng : Outil utilisé pour envoyer des trames de désauthentification.
airodump-ng : Permet de capturer les trames WiFi et d'identifier les clients connectés à un réseau.
Wireshark : Utilisé pour analyser et visualiser les trames WiFi capturées.

Processus de l'attaque :

Étape 1 : Identification du réseau cible (SSID) et des clients connectés.
Étape 2 : Utilisation de aireplay-ng pour envoyer des trames de désauthentification ciblant un client spécifique ou tous les clients du réseau.
Étape 3 : Observation de la déconnexion du client et analyse des effets sur le réseau à l'aide de Wireshark.

Protection contre l'attaque :

WPA3 : Ce nouveau protocole de sécurité WiFi apporte une meilleure protection contre les attaques de désauthentification.
Utilisation de 802.11w : Le standard de gestion de trames protégées (PMF) aide à prévenir les attaques de désauthentification en sécurisant les trames de gestion.
