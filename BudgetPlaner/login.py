#loginsidan. Om en användare inte finns så kan man skapa ett konto. Man loggar in med ett lösenord och ett användarnamn.
import os
import colorama
from colorama import init, Fore, Style
import sqlite3
from colorama import init
init(autoreset=True)
BASE_PATH = os.path.join(os.getcwd(), "Users-") #Här sparas användaruppgifterna.
os.makedirs(BASE_PATH, exist_ok=True)

# 1) Databas & tabell
conn = sqlite3.connect("users.db")
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL
)
""")
conn.commit()

def login():
    user = input("Användarnamn: ")
    pw   = input("Lösenord: ")
    c.execute("SELECT 1 FROM users WHERE username=? AND password=?", (user, pw))
    if c.fetchone():
        print("Inloggad!")
    else:
        print("Fel användarnamn eller lösenord.")
        
def nytt_konto():
    user = input("Välj användarnamn: ")
    pw   = input("Välj lösenord: ")
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?,?)", (user, pw))
        conn.commit()
        print("Konto skapat! Du kan nu logga in.")
    except sqlite3.IntegrityError:
        print("Användarnamnet är upptaget.")


while True: #Inlogg-meny
    Fore.RESET
    print("***Inloggnings-sida***\n" \
    "1. Logga in\n" \
    "2. Skapa konto\n" \
    "3. Avsluta")
    menyval=int(input("Ange ett menyval: "))

    if menyval==1:
         login()
    elif menyval==2:
        nytt_konto()
    elif menyval==3:
        print(Fore.YELLOW+("Hej då :)"))
        Fore.RESET
        break
    else:
        print("Ange ett menyval mellan 1-3")

conn.close()