### **Rogue Access Point avec l'utilisation de hostapd, dnsmasq, httcrack, et redirection Apache**
---
### 1. **Présentation de l’attaque Rogue Access Point**
Un **Rogue Access Point** (Point d'accès malveillant) exploite la confiance des utilisateurs envers un réseau Wi-Fi légitime pour intercepter des données sensibles ou rediriger vers des pages malveillantes. L’utilisation d’outils comme **hostapd**, **dnsmasq**, et des configurations de serveur web avec **Apache** permet de créer un faux point d’accès et de capter les informations transmises.

#### Objectifs principaux :
- Voler des identifiants, mots de passe ou cookies.
- Intercepter et analyser les communications des utilisateurs.
- Rediriger les utilisateurs vers des pages web malveillantes à l’aide d’un serveur local (ex. : page de phishing).

---

### 2. **Préparation de l’attaque**
#### **Matériel requis :**
1. Une interface Wi-Fi prenant en charge le mode AP (point d'accès).
2. Un ordinateur (par exemple, sous Linux) avec les outils suivants installés :
   - **hostapd** : pour émettre un point d'accès Wi-Fi.
   - **dnsmasq** : pour gérer le DHCP et le DNS.
   - **Apache** : pour héberger les pages malveillantes.
   - **httcrack** : pour capturer et analyser les identifiants.

#### **Analyse préliminaire du réseau cible :**
- Utiliser **Airodump-ng** pour identifier les réseaux à imiter :
  - **SSID cible** : FAKE-Eduroam-Touche-PAS
  - **Canal** : 1
  - **Type de chiffrement** : Aucun (réseau ouvert) avec uun portail captif

#### Configuration des outils nécessaires :
1. **hostapd** : Crée un point d’accès malveillant imitant le réseau légitime.
2. **dnsmasq** : Configure un serveur DHCP et DNS local pour rediriger tout le trafic.
3. **Apache** : Héberge une page de connexion malveillante (par exemple, un portail captif).
4. **Httcrack** : Capture et analyse les données collectées.

---
### 3. **Mise en place du Rogue Access Point**
#### **Configuration de dnsmasq :**
Configurer **dnsmasq** pour gérer le DHCP et le DNS. Créer un fichier de configuration (`dnsmasq.conf`) :
```ini
interface=wlp6s0
dhcp-range=192.168.1.2,192.168.1.250,12h
dhcp-option=3,192.168.1.1
dhcp-option=6,192.168.1.1
address=/#/192.168.1.1
```

Cette configuration pour **dnsmasq** permet de configurer un serveur DHCP et DNS sur l'interface réseau spécifiée. La ligne `interface=wlp6s0` désigne l'interface Wi-Fi utilisée pour la diffusion. Le paramètre `dhcp-range=192.168.1.2,192.168.1.250,12h` définit une plage d’adresses IP à attribuer dynamiquement aux clients, de `192.168.1.2` à `192.168.1.250`, avec une durée de bail de 12 heures. Les options `dhcp-option=3,192.168.1.1` et `dhcp-option=6,192.168.1.1` spécifient respectivement la passerelle par défaut et le serveur DNS, ici tous deux définis sur `192.168.1.1`. Enfin, `address=/#/192.168.1.1` redirige toutes les requêtes DNS vers l’adresse `192.168.1.1`, souvent utilisée pour intercepter ou rediriger le trafic des utilisateurs connectés au réseau. 

Démarrer dnsmasq :
```bash
sudo dnsmasq -C dnsmasq.conf
```

#### **Configuration de hostapd :**
Créer un fichier de configuration pour **hostapd** (`hostapd.conf`) :
```ini
#Configuration de l'interface sans-fil 
interface=wlp6s0

#Configuration du Nom Wifi
ssid=FAKE-Eduroam-Touche-PAS

#Configuration du SSID
channel=1

#Configuration du Driver
driver=nl80211
```
Cette configuration pour hostapd sert à créer un point d'accès Wi-Fi malveillant (Rogue Access Point) avec les paramètres suivants :
Interface sans fil : La ligne interface=wlp6s0 désigne l'interface réseau Wi-Fi utilisée pour diffuser le signal. Cette interface doit être compatible avec le mode AP (point d'accès).
Nom du réseau Wi-Fi (SSID) : Le paramètre ssid=FAKE-Eduroam-Touche-PAS définit le nom du réseau diffusé, conçu pour imiter un réseau légitime, dans ce cas "Eduroam".
Canal : Le paramètre channel=1 fixe le canal Wi-Fi utilisé pour la diffusion, ce qui peut être optimisé en fonction des analyses du spectre pour éviter les interférences.
Pilote réseau : La ligne driver=nl80211 spécifie le pilote utilisé pour gérer la carte Wi-Fi. Le pilote nl80211 est compatible avec la plupart des cartes modernes prenant en charge les modes AP et moniteur.


Lancer hostapd avec la commande suivante :
```bash
hostapd hostapd.conf -B
```
L'éxécution de ces commandes ce feront dans une machine Parrot OS. Il est important d'exécuter **dnsmasq** avant **hostapd** pour assurer un fonctionnement optimal du point d'accès Wi-Fi. **Dnsmasq** configure les services DHCP et DNS, permettant aux clients de recevoir une adresse IP et de résoudre les noms de domaine une fois connectés. Si **hostapd** est exécuté en premier, les clients pourront se connecter au point d'accès, mais ils ne recevront pas d'adresse IP ni de service DNS, rendant leur connexion inutilisable jusqu'à ce que **dnsmasq** soit démarré. L'ordre garantit ainsi une expérience réseau fluide pour les utilisateurs connectés.
![image](https://github.com/user-attachments/assets/7d8ff656-5782-4c27-93e8-ef286a9bb13b)

Il faut évidemment une fois ceci configuré, mettre l'adresse de notre interface sans fil en 192.168.1.1 afin de spécifier que notre point d'accès est l'interface de notre attaquant et que toutes les requêtes viennent à notre machine.
```bash
ifconfig wlp6s0 192.168.1.1/24
```
![image](https://github.com/user-attachments/assets/21dde581-3a47-4fa3-a1b2-b6e10eabf026)

### 5. **Exploitation des données**
Une fois les utilisateurs connectés au Rogue Access Point :
- Les identifiants saisis sur la page malveillante sont enregistrés.
- Les requêtes des utilisateurs sont inspectées pour capturer des cookies de session.
- Les utilisateurs peuvent être redirigés vers des pages web malveillantes ou manipulées pour compromettre davantage leur appareil.

---

### 6. **Contre-mesures**
#### **Pour les utilisateurs :**
1. **Éviter les réseaux publics non sécurisés** : Vérifier l’authenticité des points d’accès Wi-Fi.
2. **Toujours utiliser HTTPS** : Vérifier que le cadenas est présent dans la barre d’adresse.
3. **Activer un VPN** : Chiffre le trafic réseau pour éviter toute interception.

#### **Pour les administrateurs réseau :**
1. **Détecter les Rogue Access Points** : Utiliser des outils de détection comme **Kismet**.
2. **Utiliser des solutions WPA3** : Les réseaux modernes avec WPA3 offrent une sécurité renforcée.
3. **Sensibiliser les utilisateurs** : Former les employés et le public à reconnaître les réseaux douteux.

---

### 7. **Conclusion**
L’utilisation combinée de **hostapd**, **dnsmasq**, **httcrack**, et **Apache** permet de simuler une attaque de Rogue Access Point sophistiquée. Bien que cette méthode démontre les failles des réseaux Wi-Fi publics, elle souligne également l’importance de pratiques de sécurité rigoureuses. Ces tests sont essentiels pour renforcer les infrastructures contre les menaces modernes.

