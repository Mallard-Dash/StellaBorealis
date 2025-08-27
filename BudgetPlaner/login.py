#loginsidan. Om en användare inte finns så kan man skapa ett konto. Man loggar in med ett lösenord och ett användarnamn.
import os
BASE_PATH= os.path.join("C:/Users/Vince/Documents/Pythonprogram/budgetplaner") + "/"


def login():
    print("\n--- Logga in till Budgetplaner ---")
    user = input("Ange ditt namn: ").strip()
    try:
        password =(input("Ange ditt lösenord: ")).strip()
    except ValueError:
        print("Fel lösenord, försök igen!")
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
        print("Användarfilen kunde inte hittas.")
        return None
        
def nytt_konto():
    import os
    user=(input("Ange ett användarnamn: ")).strip()
    password=(input("Ange ett lösenord: ")).strip()

    with open(BASE_PATH + "users.txt", "a", encoding="utf-8") as fil:
            fil.write(f"Namn: {user}, Lösenord: {password}\n")
            print(f"Användaren {user} är nu skapad!")


while True:
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
        print("Hej då :)")
        break
    else:
        print("Ange ett menyval mellan 1-3")