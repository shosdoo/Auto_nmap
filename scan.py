import os
import subprocess
from termcolor import colored,cprint


prompt_message = colored("[+] Ingresa la ip:", "red",attrs=["bold"])
main_ip = input(prompt_message)

def exploit():
    escaneo = f'nmap -p- --open -sS --min-rate 5000 -Pn -n -oG ports.txt {main_ip}'
    regular_exp = "cat ports.txt | grep -oE '[0-9]+/open' | tr '/' ' ' | awk '{print $1}'| tr '\n' ','| sed 's/.$//';echo" 
    ejecucion_escaneo = subprocess.run(escaneo,shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE) 
    open_ports = subprocess.run(regular_exp,shell=True,capture_output=True,text=True)
    out_open = open_ports.stdout.strip()
    promt_ports = colored(f"[+] Puertos abiertos:","magenta",attrs=["bold"])
    colr_open = colored(out_open,"red",attrs=['bold'])
    print(promt_ports,colr_open)
    
    scan_versions = f"nmap -sC -sV -p {out_open} -oN versions.txt {main_ip}"    
    subprocess.run(scan_versions,shell=True,capture_output=True,text=True)
    os.remove('ports.txt')
    cprint("\n[+] Resultados de escaneo guardado en: versions.txt\n","red",attrs=["bold"])
    

if __name__ == '__main__':
    exploit()