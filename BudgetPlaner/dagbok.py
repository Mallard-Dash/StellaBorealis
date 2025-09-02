#Dagbokssidan

import os
import datetime
from colorama import init, Fore, Style
BASE_PATH = os.path.join(os.getcwd(), "Dagbok-") #Skapar en mapp som heter "Dagbok-'namn'".
os.makedirs(BASE_PATH, exist_ok=True)

def ny_dagbok(): #Skriv ny dagbok, finns ingen fil skapas det en. Nya entrys läggs till under föregående.
            namn=input("Ange ditt användarnamn: \n").strip()
            cont=input("Skriv inlägg: \n")
            x=datetime.datetime.now()
            ts= x.now().strftime("%b-%d-%Y--%H:%M")

            with open(BASE_PATH + f"{namn}.txt", "a", encoding="utf-8") as f:
                f.write(f"{ts}: {cont} \n")
                print(Fore.GREEN+("Inlägg skapat.."))
                Fore.RESET

def open_d():
            namn=input("Ange ditt användarnamn: ").strip() #Öppna dagbok
            f = open(BASE_PATH + f"{namn}.txt")
            print(f.read())
            f.close()

def remove_d():
        namn = input("Ange ditt användarnamn: ").strip() # Radera dagbok
        fil = os.path.join(BASE_PATH, f"{namn}.txt")

        if os.path.exists(fil):
                os.remove(fil)
                print(Fore.GREEN+("Filen är nu raderad.."))
                Fore.RESET
        else:
                print(Fore.RED+("Filen hittades inte, har du verkligen skrivit rätt filnamn?"))
                Fore.RESET
                         
while True:
        print("\n---Dagboksmeny---\n", #Meny för dagboksdel
        "1. Nytt dagboksinlägg\n",
        "2. Öppna dagbok\n",
        "3. Radera dagbok\n",
        "4. Tillbaka till huvudmenyn\n")
        val=int(input("Ange ett menyval mellan 1-4: "))

        if val==1:
                ny_dagbok()

        elif val==2:
                open_d()

        elif val==3:
                remove_d()

        elif val==4:
                print("Återgår till huvudmenyn...")
                Fore.RESET
                import main
             
    

             
             
                     