#loginsidan. Om en användare inte finns så kan man skapa ett konto. Man loggar in med ett lösenord och ett användarnamn.
import os
import colorama
from colorama import init, Fore, Style
BASE_PATH = os.path.join(os.getcwd(), "Users-") #Här sparas användaruppgifterna.
os.makedirs(BASE_PATH, exist_ok=True)


def login(): #Inloggfunktion med felhantering.
    print("\n--- Logga in till Budgetplaner ---")
    user = input("Ange ditt namn: ").strip()
    try:
        password =(input("Ange ditt lösenord: ")).strip()
    except ValueError:
        print(Fore.RED+("Fel lösenord, försök igen!"))
        Fore.RESET  
        return None

    try:
        with open(BASE_PATH + "users.txt", "r", encoding="utf-8") as f:
                    for rad in f:
                        if f"Namn: {user}" in rad and f"Lösenord: {password}" in rad:
                            delar = rad.strip().split(", ")
                            namn = delar[0].split(": ")[1]
                            pinkod = (delar[0].split(": ")[1])
                            print(f"Välkommen {user}")
                            import main
    except FileNotFoundError:
        print(Fore.RED+("Användarfilen kunde inte hittas."))
        Fore.RESET
        return None
        
def nytt_konto(): #Funktion för att skapa nytt konto.
    import os
    user=(input("Ange ett användarnamn: ")).strip()
    password=(input("Ange ett lösenord: ")).strip()

    with open(BASE_PATH + "users.txt", "a", encoding="utf-8") as fil:
            fil.write(f"Namn: {user}, Lösenord: {password}\n")
            print(Fore.GREEN+(f"Användaren {user} är nu skapad!"))
            Fore.RESET


while True: #Inlogg-meny
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