#FROM SEPTEMBER THE 30TH BudgetPlaner is named StellaBorealis
import os
import colorama
from colorama import init, Fore, Style
import sqlite3
from colorama import init
import hashlib
import getpass
init(autoreset=True)
BASE_PATH = os.path.join(os.getcwd(), "Users-") #This is the user database
os.makedirs(BASE_PATH, exist_ok=True)

#This is the sqlite3 database table
conn = sqlite3.connect("users.db")
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL
)
""")
conn.commit()

def login(): #Login function
    user = input("Username: ")
    pw   = input("Password: ")
    c.execute("SELECT 1 FROM users WHERE username=? AND password=?", (user, pw))
    if c.fetchone():
        print("Logged in!")
        import main
    else:
        print("Oops! Your password OR/AND username is not correct.")

def check_username(user: str): #Function to check if username meets requirements
        user = user.strip()
        if not user: return False, "Username cannot be empty."
        if len(user) < 4: return False, "Username must be at least 4 characters."
        if any(ch.isspace() for ch in user): return False, "Username cannot contain spaces."
        if len(user) > 25: return False, "Username max length is 25."
        return True, ""

def check_password(pw: str): #function to check if password meets requirements AND is also hashed-out
    if not pw: return False, "Password cannot be empty."
    if any(ch.isspace() for ch in pw): return False, "Password cannot contain spaces."
    if not (4 <= len(pw) <= 25): return False, "Password must be 4-25 characters."
    return True, ""
        
def new_user():
    while True:
        try:
            user = input("Choose username (4-25 characters): ").strip()
            ok, msg = check_username(user)
            if not ok:
                print(msg)
                continue

            pw = getpass.getpass("Choose a password (4-25 characters): ")
            ok, msg = check_password(pw)
            if not ok:
                print(msg)
                continue

            pw2 = getpass.getpass("Enter the password again: ")
            if pw != pw2:
                print("The passwords do not match. Try again.")
                continue

            try:
                c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user, pw))
                conn.commit()
                print("User created!")
                break
            except sqlite3.IntegrityError:
                print("Oh dear. This username is already taken, choose another.")
                continue

        except KeyboardInterrupt:
            print("\nCancelled by user.")
            break


while True: #Login
    Fore.RESET
    print("***WELCOME***\n" \
    "1. Log in\n" \
    "2. Create account\n" \
    "3. Exit")
    try:
        menyval=int(input("Enter a choice from 1-3: "))
    except ValueError:
        print("Please enter an int from 1-3")
        continue

    if menyval==1:
         login()
    elif menyval==2:
        nytt_konto()
    elif menyval==3:
        print(Fore.YELLOW+("Bye... :)"))
        Fore.RESET
        break
    else:
        print("Wrong input. Please enter a value between 1-3")

conn.close()