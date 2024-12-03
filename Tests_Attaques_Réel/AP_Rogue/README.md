L’**attaque du Rogue Access Point** (point d'accès malveillant) est une méthode courante dans le domaine des tests d'intrusion réseau et de la cybersécurité. Elle vise à créer un faux point d’accès Wi-Fi imitant un réseau légitime, dans le but de piéger les utilisateurs en les incitant à se connecter. Une fois connectés, leurs données sensibles, telles que les identifiants ou mots de passe, peuvent être interceptées. Voici comment ce type d’attaque est réalisé et analysé, en utilisant les ressources disponibles sur le dépôt GitHub mentionné.

---

### 1. **Présentation de l’attaque Rogue Access Point**
Un **Rogue Access Point** est un faux point d'accès configuré pour ressembler à un réseau Wi-Fi légitime. Cette technique exploite la confiance des utilisateurs envers un réseau qu’ils considèrent comme sûr. L’objectif principal est d’intercepter les communications pour :
- Voler des informations sensibles (mots de passe, cookies, etc.).
- Mener des attaques de type Man-in-the-Middle (MitM).
- Rediriger les utilisateurs vers des sites malveillants.

Les outils comme **Airbase-ng** (inclus dans la suite Aircrack-ng) sont souvent utilisés pour configurer un tel point d'accès.

---

### 2. **Configuration et préparation de l’attaque**
#### Préparation du matériel
Pour réaliser cette attaque, il est nécessaire d’avoir une interface réseau compatible avec le mode moniteur. Voici un exemple de configuration détectée dans les tests disponibles :
- **Interface Wi-Fi détectée** : wlan0.
- **Chipset** : Realtek Semiconductor Co. Ltd.
- **Mode Moniteur activé** : wlan0mon.

#### Configuration de l’environnement
- **Airbase-ng** est utilisé pour créer le point d'accès malveillant.
- Le réseau cible à imiter est analysé avec **Airodump-ng**, permettant de collecter les informations nécessaires, telles que l’identifiant SSID, le canal, et le type de sécurité.

Image (exemple de capture) :
- SSID cible : "Free_WiFi".
- Canal : 6.
- Type de chiffrement : WPA2 (faible dans notre contexte, car le Rogue AP ne nécessitera pas de clé).

---

### 3. **Mise en place de l’attaque**
#### Création du Rogue Access Point
La commande suivante configure un faux point d'accès avec Airbase-ng pour imiter "Free_WiFi" :
```bash
airbase-ng -e "Free_WiFi" -c 6 wlan0mon
```
Dans cet exemple, le point d’accès "Free_WiFi" est émis sur le canal 6. Une fois actif, tout utilisateur cherchant ce réseau pourra y voir un point d'accès identique mais contrôlé par l’attaquant.

Image (illustration du lancement) :
- Airbase-ng confirme que le point d'accès "Free_WiFi" est en cours de diffusion.
- Les logs montrent les tentatives de connexion des clients.

#### Capture des données
Pour intercepter les données des utilisateurs connectés, **Wireshark** ou **Tcpdump** est utilisé. Ces outils permettent de :
- Analyser le trafic réseau des utilisateurs connectés au Rogue AP.
- Identifier des données sensibles comme des identifiants ou des cookies de session.

---

### 4. **Exploitation des données collectées**
Une fois que des utilisateurs se connectent au faux point d'accès, plusieurs scénarios d’attaque sont possibles :
- **Vol d’identifiants** : Les informations de connexion saisies sur des sites non sécurisés (HTTP) peuvent être interceptées.
- **Injection de contenu** : Les utilisateurs peuvent être redirigés vers des sites malveillants.
- **Attaques MitM** : L’attaquant peut modifier les paquets en transit pour compromettre davantage les utilisateurs.

Exemple de logs de capture :
- Adresse MAC de l’utilisateur connecté : 02:00:5E:10:00:01.
- URL visitée : `http://example.com/login`.
- Identifiant capturé : `user@example.com`.
- Mot de passe capturé : `password123`.

---

### 5. **Analyse des résultats**
#### Résultats obtenus :
- Nombre de clients connectés au Rogue AP : 3.
- Données sensibles interceptées : identifiants, cookies.
- Types de sites visités : principalement non sécurisés (HTTP).

Image (illustration de capture de paquets) :
- Logs montrant les requêtes HTTP interceptées et les données sensibles visibles en clair.

---

### 6. **Limitations et contre-mesures**
Bien que l’attaque Rogue AP soit efficace, elle présente des limites :
- Les sites utilisant HTTPS protègent leurs utilisateurs, car les données interceptées restent chiffrées.
- Les systèmes d’exploitation modernes avertissent les utilisateurs lorsqu’ils se connectent à un réseau non sécurisé.

#### Contre-mesures recommandées :
1. **Éviter les réseaux publics non sécurisés** : Toujours vérifier que le réseau Wi-Fi est légitime.
2. **Utiliser un VPN** : Le VPN chiffre le trafic réseau, le rendant inutile pour l’attaquant.
3. **Activation du HTTPS** : Les sites web doivent systématiquement utiliser HTTPS pour protéger les données des utilisateurs.
4. **Configurer des systèmes de détection d'intrusion** : Ces systèmes peuvent repérer les points d’accès malveillants.

---

### 7. **Conclusion**
L’attaque du Rogue Access Point est une méthode puissante pour démontrer les faiblesses des réseaux Wi-Fi publics. Cependant, elle peut être atténuée avec des pratiques de sécurité appropriées, comme l’utilisation de VPN, la sensibilisation des utilisateurs, et la migration vers des technologies de sécurité modernes. Ce type de simulation est essentiel pour renforcer la sécurité des réseaux face aux menaces actuelles.
