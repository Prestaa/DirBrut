from datetime import datetime
from termcolor import colored
from sys import exit
import requests
import argparse
import keyboard

def Banner(wlst, url, ua):
    taille = sum(1 for _ in open(wlst))

    if len(ua) == 0:
        ua="None" 
        
    print(f"""
 ________  ___  ________  ________  ________  ___  ___  _________   
|\   ___ \|\  \|\   __  \|\   __  \|\   __  \|\  \|\  \|\___   ___\ 
\ \  \_|\ \ \  \ \  \|\  \ \  \|\ /\ \  \|\  \ \  \\\\\  \|___ \  \_| 
 \ \  \ \\\\ \ \  \ \   _  _\ \   __  \ \   _  _\ \  \\\\\  \   \ \  \  
  \ \  \_\\\\ \ \  \ \  \\\\  \\\\ \  \|\  \ \  \\\\  \\\\ \  \\\\\  \   \ \  \ 
   \ \_______\ \__\ \__\\\\ _\\\\ \_______\ \__\\\\ _\\\\ \_______\   \ \__\\
    \|_______|\|__|\|__|\|__|\|_______|\|__|\|__|\|_______|    \|__|
                                                                    
⸻⸻⸻⸻⸻⸻⸻⸻⸻
[+] Method:     HTTP GET
[+] User-agent: {ua}
[+] Target:     {url}
[+] Wordlist:   {wlst} mots  
[+] Taille:     {taille}    

⸻⸻⸻⸻⸻⸻⸻⸻⸻    
HotKeys:
[P] : Pause | [R] Restart | [Q] : Quitter | [S] : Stats
⸻⸻⸻⸻⸻⸻⸻⸻⸻

""")   


def TempsPris(start,endl):
        
    heures = int(endl.strftime("%H")) - int(start.strftime("%H"))
    minutes = int(endl.strftime("%M")) - int(start.strftime("%M"))
    secondes = int(endl.strftime("%S")) - int(start.strftime("%S"))
    
    a = 0
    time = ""
    
    for i in heures, minutes, secondes:
        
        if i==0:
            pass
        else:
            if a==0:
                time += str(i)+"h"
                
            elif a==1:
                time += str(i)+"m"
                
            elif a==2:      
                time += str(i)+"s"     
        a+=1
    
    if len(time) == 0:
        time = "0s"
    
    return time    
   

def Bruteforcer(url, wlst, ua):
    try:
        with open(wlst, "r", encoding = "ISO-8859-1") as wordlist:
            w = wordlist.read().split()
    
    except FileNotFoundError:
        print(colored("[!] Le fichier n'existe pas", 'red'))
        exit()
  
    except PermissionError:
        print(colored("[!] Permission refusée", 'red'))
        exit()
        
    v = 0   
    for i in range( 0 , len(w) ):
               
        if keyboard.is_pressed("P") or keyboard.is_pressed("p") :
            print(colored("""\n[i] Script mis en pause """, "yellow"))
            p_press = True
            
            while p_press==True:
                if keyboard.is_pressed("r") or keyboard.is_pressed("R"):
                    break
                else:
                    continue
                    
        if keyboard.is_pressed("Q") or keyboard.is_pressed("q") :
            print(colored("\n[!] Exiting...", 'red'))
            exit()
        
        if keyboard.is_pressed("S") or keyboard.is_pressed("s") :
            print("")
            print(f"-> Ligne       : {i} / {len(w)} ")
            print(f"-> Progression : { int( ( i / len(w) ) * 100) }% ")
            print(f"-> Fichiers    : {v} Fichiers/Répértoires trouvés")
            print("")
        
        site = f"{url}/{w[i]}"
        
        headers = {
            "User-Agent":ua
        }
        r = requests.get(site, headers=headers )
        
        if r.status_code !=404:
            printr(r.status_code, w[i])
            v += 1

            
def printr(code, site):
    if 100 <= code < 300:
        color =  "green"    
    elif 300 <= code < 400:
        color =  "yellow"
    elif 400 <= code < 500:
        color = "red"
    elif 500 <= code <= 599:
        color = "purple"

    print(colored( f"/{site} : {code}" , color)) 
   
             
def main(url , wlst, ua):
    Banner(wlst,url, ua)

    start = datetime.now()
    print(colored(f"[i] Lancement du script à : " + start.strftime("%H:%M:%S")+ "\n" , "yellow")) 
    
    Bruteforcer(url,wlst, ua)
    
    endl = datetime.now()
    
    Time = TempsPris(start, endl)
    print( colored(f"\n[i] Terminé à " + endl.strftime("%H:%M:%S") + ", taked " + Time , "yellow") )
        

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-u",
        "--url",
        help="The url of the website",
        required=True
        )
    parser.add_argument(
        "-w",
        "--wordlist",
        help="The wordlist",
        required=True
    ) 
    parser.add_argument(
        "-ua",
        "--user-agent",
        help="Un user-agent",
        required=False,
        default = ""
    ) 
    args = parser.parse_args()  ; url = args.url ; wlst = args.wordlist ; ua = args.user_agent
    
    main(url, wlst, ua)