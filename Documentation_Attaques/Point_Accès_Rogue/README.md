### **Le point d'accès rogue (ou AP rogue)**

Un point d'accès rogue est une méthode d'attaque où un attaquant configure un faux point d'accès WiFi pour tromper les utilisateurs et les pousser à s'y connecter. Cette technique est souvent utilisée pour intercepter des données sensibles, détourner le trafic ou exécuter des attaques de type **Man-in-the-Middle (MiTM)**.

---

### **Fonctionnement détaillé du point d'accès rogue**

Voici les étapes clés de la mise en place et de l'exploitation d'un point d'accès rogue :

#### 1. **Création du faux point d'accès (AP)**  
- L'attaquant configure un AP qui imite un réseau WiFi légitime déjà existant (même SSID, parfois même BSSID).  
- Cela peut être fait avec des outils comme **hostapd**, **airbase-ng** ou des équipements matériels spécialisés comme un WiFi Pineapple.  

#### 2. **Déploiement de l'AP rogue**  
- Le faux point d'accès est configuré avec des paramètres pour attirer les victimes :
  - Un SSID correspondant à celui d’un réseau légitime.
  - Une configuration ouverte (aucun mot de passe) ou un WPA similaire au réseau original.  
- Si l'AP légitime est encore actif, l’attaquant peut utiliser une attaque de désauthentification pour forcer les clients à se déconnecter du vrai AP et se reconnecter au rogue AP.

#### 3. **Connexion des victimes au rogue AP**  
- Les clients, croyant se connecter au réseau légitime, s'associent au faux AP.  
- Cela est souvent facilité par :
  - Des appareils configurés pour se reconnecter automatiquement à des SSID déjà connus.
  - Des utilisateurs qui sélectionnent le mauvais réseau par manque de vigilance.

#### 4. **Interception et manipulation du trafic**  
- Une fois connectées, les victimes acheminent tout leur trafic réseau via le rogue AP, qui agit comme un **proxy** entre elles et Internet.  
- Cela permet à l'attaquant de :
  - Intercepter des données sensibles (mots de passe, sessions web, etc.).
  - Modifier les réponses des serveurs (injecter des malwares, rediriger les utilisateurs).  

---

### **Applications avancées du point d'accès rogue**

L'AP rogue peut être exploité pour réaliser diverses attaques sophistiquées :

#### 1. **Attaque de type "Man-in-the-Middle" (MiTM)**  
- En capturant et en analysant les données qui transitent par le faux AP, l'attaquant peut intercepter :
  - Les identifiants de connexion.
  - Les sessions web non sécurisées (HTTP).
  - Les données personnelles échangées sur des applications.  
- En combinant l’attaque avec **sslstrip**, il peut forcer les connexions HTTPS à passer en HTTP pour intercepter davantage d’informations.  

#### 2. **Phishing via redirection**  
- L'attaquant peut rediriger les victimes vers de fausses pages de connexion (phishing) :
  - Par exemple, une page imitant l’écran de connexion du réseau légitime ou d’un service en ligne.  
- Cela permet de collecter directement des identifiants ou d'autres informations sensibles.  

#### 3. **Injection de malwares**  
- Le rogue AP peut manipuler les téléchargements ou injecter des scripts malveillants dans des sites web légitimes.  
- Les victimes exécutent alors ces fichiers ou scripts, donnant à l'attaquant un accès plus large à leurs appareils.  

#### 4. **Analyse approfondie des connexions**  
- Avec des outils comme **Wireshark**, l'attaquant peut analyser les trames réseau capturées pour identifier des failles ou des protocoles non sécurisés.  

---

### **Outils couramment utilisés pour un AP rogue**

1. **Hostapd** :  
   - Permet de configurer un point d’accès WiFi sur une machine Linux.  
2. **Airbase-ng** :  
   - Outil de la suite Aircrack-ng pour créer un AP rogue.  
3. **WiFi Pineapple** :  
   - Un appareil spécialisé qui simplifie le déploiement de rogue AP et inclut plusieurs outils pour la capture de données.  
4. **Ettercap et Bettercap** :  
   - Pour les attaques Man-in-the-Middle et la manipulation du trafic réseau.  
5. **Dnsmasq** :  
   - Gère le DNS et le DHCP pour l'AP rogue, permettant d’attribuer des adresses IP et de rediriger les requêtes DNS.  
6. **SSLstrip** :  
   - Force les connexions HTTPS à passer en HTTP afin d’intercepter les données.  

---

### **Comment se protéger contre les AP rogue**

Plusieurs mesures permettent de limiter le risque d'être victime d'un faux point d'accès :

#### 1. **Éviter les connexions automatiques**  
- Désactiver la connexion automatique aux réseaux WiFi déjà connus sur vos appareils.  
- Vérifier manuellement le SSID et les paramètres du réseau avant de s’y connecter.  

#### 2. **Utiliser un VPN**  
- Un VPN chiffre tout le trafic entre l’appareil et Internet, empêchant l’interception des données même si vous êtes connecté à un AP rogue.  

#### 3. **Privilégier HTTPS**  
- Toujours vérifier la présence du cadenas sécurisé dans la barre d’adresse pour s’assurer que la connexion est chiffrée.  
- Installer des extensions comme **HTTPS Everywhere** pour forcer l’utilisation de HTTPS sur les sites qui le supportent.  

#### 4. **Surveiller les comportements suspects**  
- Si un réseau demande un mot de passe ou des informations inhabituelles (comme un SSID ouvert avec un portail captif), cela peut indiquer une attaque.  

#### 5. **Détection d'AP rogue**  
- Les solutions de sécurité réseau (comme un IDS ou un WIDS) permettent d’identifier la présence de rogue AP dans l’environnement WiFi.  
- Les outils comme **Kismet** ou **Aircrack-ng** peuvent également être utilisés pour repérer des anomalies.  

#### 6. **Éviter les réseaux publics**  
- Les réseaux ouverts, comme ceux des cafés ou des aéroports, sont des terrains idéaux pour les AP rogue.  
- Si vous devez utiliser un réseau public, limitez les activités sensibles (banque en ligne, messageries, etc.).  

---

### **Faiblesses de l'attaque**
1. **Limitation des connexions** : Certains appareils modernes signalent les connexions WiFi suspectes ou bloquent les réseaux non sécurisés.  
2. **WPA3 et PMF** : Les protocoles modernes et l’utilisation de **Protected Management Frames** compliquent la mise en place de certaines techniques comme le spoofing d’AP.  
3. **Concurrence avec le réseau légitime** : Si le réseau légitime est toujours actif, certains clients peuvent rester connectés à celui-ci.  

---

### **Résumé**
Un point d’accès rogue est une technique redoutable pour intercepter des données ou exécuter des attaques avancées comme le phishing ou le MiTM. Cependant, des mesures comme l’utilisation d’un VPN, la vigilance lors de la connexion à des réseaux et l’adoption de normes modernes (WPA3) permettent de réduire significativement les risques.
