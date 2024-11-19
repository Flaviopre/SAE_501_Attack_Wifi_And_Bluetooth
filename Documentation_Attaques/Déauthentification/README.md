### **L'attaque de désauthentification WiFi en détail**

L'attaque de désauthentification WiFi est une technique simple mais efficace pour déconnecter des clients d'un réseau WiFi. Elle s'appuie sur la faiblesse du protocole **802.11** utilisé pour les communications WiFi, où les trames de gestion (comme les trames de désauthentification et de déconnexion) ne sont pas authentifiées ni chiffrées dans les versions WPA2 ou antérieures.

---

### **Fonctionnement détaillé de l'attaque**
Voici les étapes d'une attaque typique :

#### 1. **Mise en mode moniteur**
- **Préparation** : L'attaquant configure sa carte réseau sans fil pour écouter passivement les trames WiFi en activant le **mode moniteur** via un outil comme **airmon-ng**.
- **Objectif** : Observer tout le trafic dans la zone pour identifier les points d'accès (SSID/BSSID) et les clients connectés (adresses MAC).

#### 2. **Identification des cibles**
- L'attaquant utilise un outil tel que **airodump-ng** pour :
  - Scanner les réseaux à proximité.
  - Repérer un réseau cible (SSID/BSSID).
  - Identifier les clients associés à ce réseau (leurs adresses MAC).

#### 3. **Envoi de trames de désauthentification**
- Une fois la cible identifiée (point d'accès et client spécifique), l'attaquant utilise **aireplay-ng** ou un outil similaire pour injecter de **fausses trames de désauthentification**.
- Ces trames sont envoyées avec l'adresse MAC du point d'accès, imitant une demande légitime de désauthentification.
- **Option ciblée ou globale** :
  - **Ciblée** : L'attaquant vise un client spécifique.
  - **Globale** : L'attaquant vise tous les clients connectés à un réseau en envoyant des trames en broadcast.

#### 4. **Impact sur le réseau**
- Les clients recevant ces trames croient qu'elles proviennent du point d'accès légitime.
- Ils se déconnectent immédiatement du réseau, entraînant un **déni de service (DoS)** temporaire.
- Certains clients tentent de se reconnecter immédiatement, ce qui expose davantage de trames WiFi exploitables (comme un handshake WPA pour une attaque ultérieure).

---

### **Applications avancées de l'attaque**
Outre le DoS, cette attaque peut être utilisée comme point de départ pour d'autres attaques plus complexes, notamment :

#### 1. **Capture de handshake WPA/WPA2**
- En forçant un client à se déconnecter, on peut capturer le processus de reconnexion.
- Si le client se reconnecte, il échange un handshake WPA (Pairwise Transient Key - PTK), essentiel pour craquer le mot de passe à l'aide d'un dictionnaire.

#### 2. **Attaque de type "Man-in-the-Middle" (MiTM)**
- L'attaquant crée un faux point d'accès (AP rogue) et incite les clients déconnectés à s'y reconnecter.
- Cela permet d’intercepter les données transmises par les clients (identifiants, mots de passe, trafic).

#### 3. **Exploitation pour des attaques sur le protocole 802.11**
- Analyse approfondie des trames WiFi capturées pour exploiter d'autres vulnérabilités ou collecter des informations sensibles.

---

### **Outils couramment utilisés**
Voici quelques outils pour mener une attaque de désauthentification :

1. **Aircrack-ng Suite** :
   - **Airmon-ng** : Active le mode moniteur.
   - **Airodump-ng** : Permet d’identifier les AP et les clients connectés.
   - **Aireplay-ng** : Injecte les trames de désauthentification.

2. **Wireshark** :
   - Analyse les trames capturées.
   - Visualise les interactions réseau et identifie les trames de gestion.

3. **hcxdumptool** et **hcxtools** :
   - Outils modernes pour capturer des handshakes WPA et tester les mots de passe.

4. **Scapy** :
   - Bibliothèque Python puissante pour construire et injecter des paquets personnalisés.

---

### **Protection contre les attaques de désauthentification**
Plusieurs contre-mesures peuvent être utilisées pour prévenir ces attaques :

#### 1. **Protocole WPA3**
- WPA3 introduit la fonction **SAE (Simultaneous Authentication of Equals)**, qui améliore la sécurité des connexions et empêche les attaques basées sur la capture de handshakes.
- Cependant, WPA3 n'est pas encore largement adopté, et beaucoup de réseaux utilisent encore WPA2.

#### 2. **802.11w (PMF - Protected Management Frames)**
- Ce standard protège les trames de gestion (comme les trames de désauthentification ou de désassociation).
- PMF empêche les trames de gestion non authentiques d’être acceptées par les clients.
- PMF est disponible avec WPA2, mais il doit être activé explicitement dans la configuration du routeur.

#### 3. **Filtrage des adresses MAC**
- Restreindre les connexions réseau aux appareils autorisés peut compliquer les attaques, mais ce n’est pas une solution infaillible (l’adresse MAC peut être usurpée).

#### 4. **Surveillance des anomalies réseau**
- Les systèmes de détection d'intrusion (IDS) peuvent être utilisés pour identifier un volume élevé de trames de désauthentification et alerter les administrateurs réseau.

#### 5. **Isolation des clients**
- Certains routeurs offrent une option pour empêcher les clients d’interagir directement entre eux, réduisant l'impact des attaques MiTM.

---

### **Limites et inconvénients**
1. **Utilisation légitime** : L'attaque de désauthentification peut également être exploitée dans des tests de pénétration pour évaluer la robustesse des réseaux WiFi.
2. **Impact limité contre WPA3/802.11w** : Ces protections rendent l'attaque presque impossible dans les réseaux modernes.
3. **Environnement bruyant** : L'attaque peut causer une surcharge réseau ou être rapidement détectée par des outils de surveillance.

---

### **Résumé**
L'attaque de désauthentification est un outil puissant dans les tests de sécurité WiFi mais reste une faille exploitée dans les réseaux vulnérables. Les évolutions des standards WiFi, comme WPA3 et 802.11w, cherchent à contrer ces failles. Toutefois, de nombreux réseaux actuels restent vulnérables, ce qui souligne l'importance d'une configuration de sécurité rigoureuse.
