#Dagbokssidan

import os
import datetime
BASE_PATH= os.path.join("C:/Users/Vince/Documents/Pythonprogram/budgetplaner") + "/"

def ny_dagbok():
            namn=input("Ange ditt användarnamn: \n").strip()
            cont=input("Skriv inlägg: \n")
            x=datetime.datetime.now()
            ts= x.now().strftime("%b-%d-%Y--%H:%M")

            with open(BASE_PATH + f"{namn}.txt", "a", encoding="utf-8") as f:
                f.write(f"{ts}: {cont} \n")
                print("Inlägg skapat..")

def open_d():
            namn=input("Ange ditt användarnamn: ").strip()
            f = open(BASE_PATH + f"{namn}.txt")
            print(f.read())
            f.close()

def remove_d():
        namn = input("Ange ditt användarnamn: ").strip()
        fil = os.path.join(BASE_PATH, f"{namn}.txt")

        if os.path.exists(fil):
                os.remove(fil)
                print("Filen är nu raderad..")
        else:
                print("Filen hittades inte, har du verkligen skrivit rätt filnamn?")
                         
while True:
        print("\n---Dagboksmeny---\n",
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
                import main
             
    

             
             
                     