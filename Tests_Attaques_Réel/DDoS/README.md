## DDoS sur le Wi-Fi : Attaque de désauthentification avec aireplay-ng

**1. Présentation de l'attaque DDoS Wi-Fi**  
Cette attaque vise à perturber le fonctionnement d'un réseau Wi-Fi légitime en envoyant des paquets de désauthentification aux appareils connectés. Cela force les utilisateurs à se déconnecter continuellement du réseau, rendant la connexion inutilisable.  
Le script Python fourni facilite cette attaque en automatisant plusieurs étapes : identification du réseau cible, mise en mode surveillance de l'adaptateur Wi-Fi, et exécution de l'attaque de désauthentification avec `aireplay-ng`.  

**Objectifs principaux :**
- Perturber le réseau Wi-Fi légitime.
- Forcer les utilisateurs à perdre leur connexion.
- Potentiellement préparer une attaque secondaire, comme l'usurpation d'un réseau avec un Rogue Access Point.  

---

## 2. Préparation de l’attaque  

**Matériel requis :**  
- Une interface Wi-Fi prenant en charge le mode monitor.  
- Un ordinateur (sous Linux, par ex., Kali ou Parrot OS).  
- Les outils installés : `aircrack-ng` (incluant `airodump-ng`, `aireplay-ng`), Python 3.  

**Script utilisé :** Le script Python fourni automatise les étapes suivantes :  
1. **Identification des réseaux Wi-Fi disponibles.**  
2. **Mise en mode surveillance de l'interface Wi-Fi.**  
3. **Exécution d'une attaque de désauthentification.**

---

## 3. Étapes de l'attaque

### 3.1 Identification des réseaux Wi-Fi
- Le script exécute `iwconfig` pour détecter les interfaces Wi-Fi disponibles.  
- Une fois une interface sélectionnée, il passe en mode surveillance avec `airmon-ng start`.  
- `airodump-ng` est utilisé pour scanner les réseaux disponibles, dont les détails sont sauvegardés dans un fichier CSV.  
- Les réseaux détectés sont affichés dans un tableau pour que l'utilisateur choisisse la cible.  

**Exemple d’affichage :**
```plaintext
No |    BSSID              | Channel | ESSID                         
___|    ___________________|_________|______________________________
0  |  00:11:22:33:44:55    |    1    | WiFi-Exemple1
1  |  66:77:88:99:AA:BB    |    6    | WiFi-Exemple2
```

---

### 3.2 Passage en mode surveillance
Une fois la cible sélectionnée, l'adaptateur Wi-Fi est configuré pour écouter sur le canal du réseau cible :
```bash
airmon-ng start wlan0mon <channel>
```
Le script exécute cette commande automatiquement après le choix du réseau.

---

### 3.3 Attaque de désauthentification
L'attaque utilise `aireplay-ng` pour envoyer un flot continu de paquets de désauthentification vers tous les clients connectés :
```bash
aireplay-ng --deauth 0 -a <BSSID> wlan0mon
```
- `--deauth 0` : Envoie un nombre illimité de paquets de désauthentification.  
- `-a <BSSID>` : Spécifie le BSSID (identifiant du point d'accès).  
- `wlan0mon` : Interface Wi-Fi en mode surveillance.

Le script exécute cette commande en arrière-plan avec `subprocess.Popen`.

---

## 4. Phase de test
Sur notre machine attaquante, nous allons lancer le script python en Super Utilisateur afin que le fichier aient tous les droits sur notre machine et puisse faire ce qu'il veut. 
Pour l'interface choisie, nous utiliserons celle de base qui fera parfaitemment l'affaire. Evidemment, sur la machine attaquante, python3 et les modules nécessaires pour le script doivent être installé.
Pour lancer le script, nous allons utiliser la commande suivante :
```bash
python3 Script_Python.py
```
![image](https://github.com/user-attachments/assets/79011b4f-119a-489a-94ac-10a67866ff85)

Une fois executé, nous devons choisir l'interface que nous allons chosir afin d'émettre les trames et DDoS le réseau Wi-Fi. 
On voit que l'on doit choisir un numéro et que ce numéro est le 0 :
![image](https://github.com/user-attachments/assets/544c7c60-6635-4dce-b42c-a9b8901c3d19)

Une fois ceci effectué, cela va scanner les différents Wi-Fi disponible afin de voir et de choisir lequel attaquer.
On créera un réseau Wifi avec un point d'accès LinkSys WRT54GL, avec un réseau Wifi 2.4GHz nommée FAKE-Eduroam-Touche-PAS (comme le Rogue AP) sur le channel 1 avec une méthode d'authentification WPA2-PSK.
Cela va faire une analyse des réseaux Wi-Fi avec le nom de chaque réseau Wifi, le BSSID associé, le canal du réseau et l'ESSID. 
Etant donnée que nous sommes dans une salle bondée de réseau Wifi, on trouvera plusieurs types de réseau disponibles : 
![image](https://github.com/user-attachments/assets/fea63c19-dc68-4bc4-bc71-a4507190d25b)

Nous choisirons le numéro 0 qui est notre premier réseau Wi-FI disponible. Mais avant cela, un cleint va se connecter à notre réseau Wifi à l'aide du mot de passe testtest et qui va nous permettre de simuler un arrêt de service. Il sera connecté non pas à Internet mais seulement en local afin d'éviter les erreurs. On verra donc le client connecté :
![image](https://github.com/user-attachments/assets/d2473b43-97fc-4220-ae53-8f4c0856c48e)

On lancera maintenant l'attaque afin de voir ce que cela fait en choisssant le bon ESSID.
![image](https://github.com/user-attachments/assets/1a4da302-df85-461a-82c6-f93acd8f9077)


**Indicateurs de réussite :**  
- Les utilisateurs du réseau cible perdent leur connexion.  
- Le terminal affiche un message indiquant que l'attaque est en cours.  

---

## 5. Contre-mesures

**Pour les utilisateurs :**  
- Évitez les réseaux Wi-Fi ouverts ou non sécurisés.  
- Utilisez des solutions VPN pour protéger vos connexions.  
- Optez pour des équipements compatibles WPA3, qui offrent une meilleure protection.  

**Pour les administrateurs réseau :**  
- Utilisez des outils de détection d'intrusion, comme Kismet, pour identifier les attaques de désauthentification.  
- Mettez en place des solutions comme la détection des paquets de désauthentification pour bloquer ce type d’attaque.  
- Activez les fonctions de gestion de réseau avancées sur les routeurs, qui peuvent réduire les impacts de ce genre d’attaque.

---

## 6. Conclusion  
L’attaque DDoS Wi-Fi par désauthentification est une méthode efficace pour interrompre un réseau. Le script Python simplifie sa mise en œuvre, soulignant les vulnérabilités des réseaux Wi-Fi modernes. Cela renforce l'importance d'une sécurité robuste pour les infrastructures sans fil.  

**Avertissement :** Ce guide est exclusivement à des fins éducatives et doit être utilisé uniquement sur des réseaux que vous possédez ou pour lesquels vous avez une autorisation explicite.
