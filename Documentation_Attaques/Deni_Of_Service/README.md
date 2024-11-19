### Le déni de service (DoS) sur les réseaux WiFi

Le déni de service (DoS) sur les réseaux WiFi est une attaque visant à rendre un réseau sans fil indisponible pour ses utilisateurs légitimes. Elle s'appuie sur des failles dans les protocoles de communication ou sur la saturation des ressources pour perturber ou bloquer le trafic réseau.

---

### Fonctionnement détaillé d’une attaque DoS sur WiFi

Voici les étapes clés pour réaliser une attaque DoS sur un réseau WiFi :

#### 1. **Identification du réseau cible**  
L’attaquant commence par scanner les réseaux WiFi environnants en utilisant des outils comme **airodump-ng**.  
Les informations essentielles collectées incluent :  
- **SSID** : Nom du réseau.  
- **BSSID** : Adresse MAC du point d'accès.  
- **Canal** : Fréquence utilisée par le réseau.  
- **Liste des clients connectés** : Appareils associés au réseau.

#### 2. **Lancement de l’attaque DoS**  
Une fois le réseau cible identifié, plusieurs méthodes permettent de mener une attaque DoS :

##### a. **Attaque de désauthentification**  
Cette méthode consiste à envoyer des paquets de désauthentification aux clients connectés au réseau, les forçant à se déconnecter.  
- Outil utilisé : **aireplay-ng**.  
- L’attaquant spécifie le BSSID du point d’accès et l’adresse MAC de la victime pour cibler un appareil spécifique, ou choisit de déconnecter tous les clients simultanément.

##### b. **Saturation par inondation de paquets**  
L'attaquant envoie un grand nombre de paquets pour saturer le réseau, provoquant un ralentissement ou une panne.  
- Outils : **MDK3** ou **MDK4**, qui peuvent envoyer des paquets de balise (beacon), des requêtes de sonde (probe requests), ou d'autres types de messages.

##### c. **Exploitation des failles protocolaires**  
Certaines attaques exploitent des vulnérabilités dans les standards WiFi comme les frames de gestion non protégées (sans **802.11w**). Cela permet à un attaquant de mener des attaques de fragmentation ou d'injecter des frames malveillantes.

#### 3. **Maintien de l’attaque**  
Pour garantir une perturbation continue, l’attaquant automatise l'envoi de paquets ou exécute des scripts qui assurent une attaque permanente.

---

### Applications avancées des attaques DoS sur WiFi  

#### 1. **Perturbation de services critiques**  
Une attaque DoS peut viser des infrastructures sensibles, perturbant les communications dans des environnements professionnels ou industriels.  

#### 2. **Facilitation d’autres attaques**  
Le DoS peut être utilisé comme une première étape pour affaiblir la sécurité d'un réseau :  
- **Forcer les utilisateurs à se reconnecter** pour capturer des handshakes WPA et lancer une attaque de cracking.  
- **Créer une diversion** pendant qu'une autre attaque est menée (par exemple, exfiltration de données).

#### 3. **Attaque ciblée sur des utilisateurs spécifiques**  
Un attaquant peut cibler des appareils précis pour les empêcher d’accéder au réseau tout en laissant les autres utilisateurs connectés.

---

### Outils couramment utilisés pour les attaques DoS sur WiFi  

- **Aireplay-ng**  
  Permet d’envoyer des paquets de désauthentification pour déconnecter des clients du réseau.  
- **MDK3/MDK4**  
  Outils puissants pour réaliser diverses attaques DoS par inondation de paquets ou exploitation de failles protocolaires.  
- **Wireshark**  
  Utilisé pour analyser le trafic et vérifier l'impact de l’attaque en temps réel.  
- **Scapy**  
  Permet de construire des paquets personnalisés pour des attaques spécifiques.

---

### Comment se protéger contre les attaques DoS sur WiFi  

#### 1. **Activer le 802.11w (PMF)**  
Le **Protected Management Frames** protège les frames de gestion contre les manipulations malveillantes, rendant les attaques de désauthentification moins efficaces.

#### 2. **Configurer un système de détection d'intrusion WiFi (WIDS)**  
Un **WIDS** peut détecter des attaques de type DoS et alerter l’administrateur réseau.

#### 3. **Segmenter le réseau**  
La séparation des réseaux (réseau principal et réseau invité) limite l’impact d’une attaque DoS à une portion du réseau.

#### 4. **Changer les canaux fréquemment**  
L'utilisation de canaux WiFi moins encombrés et le changement périodique de ces derniers peuvent réduire l'efficacité des attaques DoS par saturation.

#### 5. **Adopter des technologies WiFi modernes**  
Les réseaux utilisant les normes **WiFi 6** ou **WiFi 6E** bénéficient de meilleures protections contre les interférences et saturations.

#### 6. **Limiter la portée du signal WiFi**  
Réduire la portée du réseau diminue le risque qu’un attaquant à distance puisse interagir avec le point d’accès.

#### 7. **Mettre en place un VPN**  
Un VPN ne prévient pas l’attaque DoS mais garantit que les données échangées restent chiffrées en cas de connexion forcée à un réseau compromis.

---

### Faiblesses et limites des attaques DoS sur WiFi  

#### 1. **Détection par les administrateurs réseau**  
Les solutions modernes de surveillance réseau peuvent détecter rapidement les attaques DoS, permettant une intervention rapide.

#### 2. **Impact limité sur des réseaux robustes**  
Les réseaux bien configurés, utilisant des technologies avancées, peuvent résister aux attaques DoS ou en minimiser l’impact.

#### 3. **Durée et ressources nécessaires**  
Une attaque DoS prolongée nécessite une présence constante de l’attaquant à proximité et des ressources suffisantes pour maintenir l’attaque.

---

### Résumé  
Le déni de service sur les réseaux WiFi est une attaque perturbatrice qui peut compromettre l’accessibilité des services réseau. Cependant, avec des outils adaptés et des protections robustes comme **802.11w**, WIDS, ou des technologies modernes, il est possible de réduire significativement les risques liés à ces attaques.
