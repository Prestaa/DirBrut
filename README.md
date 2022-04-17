# DirBrut

DirBrut is a python3 command-line tool for web directory/file bruteforcing.


## Installation :
```
git clone https://github.com/PrestaDZ/DirBrut.git
cd DirBrut
pip3 install -r requirements.txt
```

## Usage :

```
$ python3 DirBrut.py -h

usage: DirBrut.py [-h] -u URL -w WORDLIST [-ua USER_AGENT]

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     The url of the website
  -w WORDLIST, --wordlist WORDLIST
                        The wordlist
  -ua USER_AGENT, --user-agent USER_AGENT
                        Un user-agent
                        
```


## Exemple :

```
$ python3 DirBrut.py -u https://example.com -w common.txt -ua Mozilla/5.0

 ________  ___  ________  ________  ________  ___  ___  _________
|\   ___ \|\  \|\   __  \|\   __  \|\   __  \|\  \|\  \|\___   ___\
\ \  \_|\ \ \  \ \  \|\  \ \  \|\ /\ \  \|\  \ \  \\\  \|___ \  \_|
 \ \  \ \\ \ \  \ \   _  _\ \   __  \ \   _  _\ \  \\\  \   \ \  \
  \ \  \_\\ \ \  \ \  \\  \\ \  \|\  \ \  \\  \\ \  \\\  \   \ \  \
   \ \_______\ \__\ \__\\ _\\ \_______\ \__\\ _\\ \_______\   \ \__\
    \|_______|\|__|\|__|\|__|\|_______|\|__|\|__|\|_______|    \|__|

⸻⸻⸻⸻⸻⸻⸻⸻⸻
[+] Method:     HTTP GET
[+] User-agent: Mozilla/5.0
[+] Target:     https://example.com
[+] Wordlist:   common.txt
[+] Taille:     4713 mots

⸻⸻⸻⸻⸻⸻⸻⸻⸻
HotKeys:
[P] : Pause | [R] Restart | [Q] : Quitter | [S] : Stats
⸻⸻⸻⸻⸻⸻⸻⸻⸻


[i] Lancement du script à : 15:27:12

/admin : 401
/index : 200
/arch : 200
/assets : 403

[i] Terminé à 15:37:55, taked 10m43s

```

## Hotkeys:

S:
```
-> Ligne       : 307 / 4716 
-> Progression : 6%
-> Fichiers    : 11 Fichiers/Répértoires trouvés
```

P:
```
Pause the script
```

R
```
Restart the script
```
permettra de le relancer. Enfin Q permet de quitter le programme proprement.


## Informations :

- Written by : Presta
- Language : Python3
