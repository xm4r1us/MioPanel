import os 
#os.system("sudo apt-get install python-pip")
#os.system("sudo apt-get install python3-pip")
#os.system("sudo pip install discord.py colorama requests")
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet MioPanel")
print("""

    MioPanel Version 2.0.3 
    Thanks Schrader & KokoD3veloper 
    https://github.com/KokoD3veloper/MioPanel
""")


print("""
--------BruteForcer-------
[1] RDP Brute
[2] Instangram Bruteforcer
[4] Mail Checker (Before Upload mailcombo.txt)
[9] 2Capchta Checker (If You Dont Upload Proxy in proxylist.txt it dont work)
-------Scraper-------
[3] Anonfile Scraper
[8] Proxy Scraper
-------Phishing-------
[5] Phishing Script Creator And Run Localhost
[6] Clean Phishing  Script (Use After Pshing Script Creator)
[7] Run Phishing Page Ngrok (Not Our But We Will Add Script)

""")
log= raw_input("Run Your Script With Number ------->")

if (log== "1"):
   os.system("sudo python rdp.pyc")
elif (log== "9"):
   os.system("python 2capchta.py")
elif (log=="2"):
	os.system("sudo python insta.pyc")
elif (log=="3"):
	os.system(" python anonfile.pyc")
elif (log== "4"):
	os.system("python mail.pyc")
elif (log== "5"):
	os.system("sudo python3 crpage.py")
elif (log== "7"):
	os.system("")
	os.system("sudo bash socialphish.sh")
elif (log== "8"):
	os.system("python scraper.py")
	
elif (log== "6"):
	os.system("sudo rm -rf ./web")
	os.system("sudo rm -rf ./post.txt")
	print("Deleted Pshing Script You Can Use Scripts Now")
else: 
	print("This Number Not Exists")

    
	
	
