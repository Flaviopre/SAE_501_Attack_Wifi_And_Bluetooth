Sujet n°6 – Monitoring et hacking WiFi et Bluetooth Réalisé par Flavio Fernandes De Araujo, Loris Glaise et Alexis Quinot


Lors de l’un des TP WiFi, vous aurez l’occasion de visualiser les trames WiFi qui circulent entre un point d’accès et une carte réseau WiFi. La suite logique de ce TP serait de procéder à des tentatives d’attaque (déauthentification, désassociation, interception de mot de passe, etc….). Mais d’une part, le TP est déjà très complet, et d’autre part, cela peut avoir des conséquences si le sujet n’est pas suivi
scrupuleusement (si on faisait ça sur le réseau de l’IUT au lieu de le faire sur un réseau local). Comme pour d’autres manipulations, l’idée est d’intercepter les trames émises, en filaire, à l’aide de la radiologicielle (en reliant le connecteur d’antenne du point d’accès à la clé SDR). Dans la pratique, on utilisera un Adalm Pluto car la bande passante sera plus importante qu’une clé SDR.

Ainsi, il faudra:

- Visualiser le spectre WiFi via l’adalm PLuto

- Parvenir à visualiser les trames qui circulent via l’adalm Pluto, sur Wireshark (pour cette étape, on pourra rester en WiFi).

- Testez le bon fonctionnement en filaire.

- Envoyez différentes trames pour déauthentifier un client, obtenir son mot de passe, etc…
  
- Observez sous Wireshark l’influence de ces trames.

- Suivant le temps qu’il restera, on pourra ensuite étudier le protocole Bluetooth, en visualisant les trames sous Wireshark aux différentes étapes de l’association
