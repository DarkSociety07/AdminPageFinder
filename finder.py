from colorama import Fore
import requests
import sys
import os


# dark_society07

def site():
    if os.name == "nt":
      os.system("cls")
      print("")
    elif os.name == "posix":
      os.system("clear")
        
    search = open("page.txt", 'r')
    url = input(Fore.LIGHTGREEN_EX+"""┌─[Dark-Society07~@HOME]
 └──╼ $  Entr URL :""")

    if "http://" or "https://" not in url:
        url = "http://"+url
    else:
        pass
    try:
        for page in search:
            req = requests.get(url + "/" + page)
            if req.status_code == 200:
                print(Fore.LIGHTGREEN_EX + "[+] " + Fore.LIGHTWHITE_EX + "page ok " + url + "/" + page)
            else:
            	pass
                #print(Fore.LIGHTRED_EX + "[-] " + Fore.LIGHTWHITE_EX + "not page " + url + "/" + page)
    except requests.exceptions.MissingSchema:
        print("\nUrl eshtebah ast lotfan dobare vard konid! : \n")
    except NameResolutionError:
    	os.system("python3 dibagsite.py")
    except NameError: 
    	os.system("python3 dibagsite.py")
    	print("place Enter URL...")
    	
    	
    	
    	
    	
    	
site()

