#!/usr/bin/env python3

from termcolor import colored
from datetime import datetime
from sys import exit
import argparse
import socket

def Banner():
    
    print(colored("""
     ____                               ____           _     _               
    | __ )  __ _ _ __  _ __   ___ _ __ / ___|_ __ __ _| |__ | |__   ___ _ __ 
    |  _ \ / _` | '_ \| '_ \ / _ \ '__| |  _| '__/ _` | '_ \| '_ \ / _ \ '__|
    | |_) | (_| | | | | | | |  __/ |  | |_| | | | (_| | |_) | |_) |  __/ |   
    |____/ \__,_|_| |_|_| |_|\___|_|   \____|_|  \__,_|_.__/|_.__/ \___|_|       
    """, 'green'))
    
    print(colored("   --< Search for banners\n   --< By @Presta\n\n", 'red'))


def StripPorts(ports):
    p1=""
    p2=""
    
    if "-" not in ports:
        print(colored("[!] --port option must be like : -p 5-100  ", 'red'))
        exit()
    
    
    for i in range(0,len(ports)):
        if ports[i]=="-":
            nbr = i+1
            break
        else:
            p1+=ports[i]
            
    for i in range(nbr, len(ports)):
        p2 += ports[i]
    
    try:
        p1 = int(p1)
        p2 = int(p2)
    except:
        print(colored("[!] Port must be numbers !", 'red'))
        exit()
    
    if p1 > 65535 or p2 > 65535:
        print(colored("[!] Port must be in range 0 to 65535", "red"))
        exit()

    liste = [p1, p2]      
    return liste

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

def GetBanner(ip, porttuple, time):
    
    p1 = int(porttuple[0])
    p2 = int(porttuple[1])+1
    
    for i in range(p1,p2):   
        
        try:     
            s = socket.socket()
            s.settimeout(time)
            s.connect(( str(ip) , int(i) ))
            
        except ConnectionRefusedError:
            pass
        
        except socket.gaierror:
            print(colored(f"[!] Cannot connect to {ip} try to increase the timeout value or check te ip adress", 'red'))
            exit()
        except OSError:
            print(colored(f"[!] Cannot connect to {ip} try to increase the timeout value or check te ip adress", 'red'))
            exit()   
        var=""
        
        try:
            var = str(s.recv(1024).decode('UTF-8'))
        except socket.timeout:
            pass
        except UnicodeDecodeError:
            pass
        except OSError:
            print(colored(f"[!] Cannot connect to {ip} try to increase the timeout value or check te ip adress", 'red'))
            exit()
            
        if len(var) >0:          
            print(colored(f"[+] At port {i} : " , 'green') + colored( var, 'red'), end="") 


def main(ip, porttuple, time):
    
    try:
        time = int(time)
    except:
        print(colored("[!] Time must be an integer !", 'red'))
        exit()
    if time<5:
        print(colored(f"[!] The timeout is set to {time}, programm may not work correctly", 'red'))

        
    start = datetime.now()
    print(colored(f"[i] Starting at : " + start.strftime("%H:%M:%S")+ "\n" , "yellow"))
    
    GetBanner(ip, porttuple,time)
    
    endl = datetime.now()
    Time = TempsPris(start, endl)
   
    print( colored(f"\n[i] Ending at " + endl.strftime("%H:%M:%S") + ", scanned in " + Time , "yellow") )

    
if __name__ == "__main__":
    Banner()
    parser = argparse.ArgumentParser("")

    parser.add_argument(
        "-i",
        "--ip",
        help="The ip address.",
        required=True
        )
    parser.add_argument(
        "-p",
        "--ports",
        help="Range port to scan (default is 1-65535) | ( python3 BannerGrabber.py -p 1-100 ).",
        required=False,
        default="1-65535"
        )
    parser.add_argument(
        "-t",
        "--timeout",
        help="time before closing the communication in second, minimum is 5",
        required=False,
        default="5"
        )     
    args = parser.parse_args()  ; ip_add = args.ip ; ports=args.ports ; time=args.timeout
      
    porttuple = StripPorts(ports)
    
    main(ip_add, porttuple, time)
