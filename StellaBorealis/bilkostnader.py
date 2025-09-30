#Filen som tar hand om bilkostnader.
#Detta var från början ett eget program men nu valde jag att svetsa samman det som en del i det stora programmet.

import datetime
import os
import json
import colorama
from colorama import init, Fore, Style
BASE_PATH = os.path.join(os.getcwd(), "Fordon-") #Skapar en mapp som heter "Fordon-'info'"
os.makedirs(BASE_PATH, exist_ok=True)
from colorama import init, Fore, Style

def open_servicebook():
            print("Tillgängliga bilar:")
            for fil in os.listdir(BASE_PATH):
                    print(Fore.YELLOW + fil)
            while True:
                regnr=input(Fore.RESET + f"Ange registreringsnummer: ")
                filnamn = os.path.join(BASE_PATH, regnr)
                if os.path.exists(filnamn):
                    with open(filnamn, "r", encoding="utf-8") as f:
                        print(f.read())
                        break

                else:
                    print(Fore.RED + "Filen existerar inte, försök igen.")

def nytt_regnr():
    ny=input("Ange ett regnummer till bilen du vill lägga in: ")
    x=datetime.datetime.now()
    filnamn= (f"{BASE_PATH}/{ny}.json")
    with open(filnamn, "w", encoding="utf-8") as fil:
        fil.write(f"{ny}, {x.day}-{x.month}-{x.year}\n")
        print(Fore.GREEN + f"{ny} är nu sparad.")
        Fore.RESET

def ny_service():
    d=datetime.datetime.now()
    servicerad=input("Ange registreringsnummer")
    miltal=input("Ange miltal: ")
    job=input("Skriv vad du har gjort för service: ")

    data = {
        "Datum": d.strftime("%Y-%m-%d %H:%M"),
        "Regnr": servicerad,
        "Miltal": miltal,
        "Typ av service": job,
    }
    with open(os.path.join(BASE_PATH, servicerad), "a", encoding="utf-8") as fil:
        json.dump(data, fil, ensure_ascii=False)
        fil.write("\n")
        print(Fore.GREEN + f"Sparat i filen: {servicerad}")
        (Fore.RESET)


def bildata():
    regnummer_bildata=input("Ange regnummer: ")
    filnamn = os.path.join(BASE_PATH, regnummer_bildata)
    with open(filnamn, "r", encoding="utf-8") as f:
        print(f.read())


def kunskapsbank():
    regnummer_kunskapsbank=input("Ange regnummer: ")
    filnamn = os.path.join(BASE_PATH, regnummer_kunskapsbank)
    with open(filnamn, "r", encoding="utf-8") as f:
        print(f.read())


def körjournal():
    datum=input("Ange datum: ")
    regnr_journal=input("Ange regnummer: ")
    start=input("Ange ort där du startar: ")
    dest=input("Ange mål: ")
    sträcka=input("Hur många kilometer har du kört?")
    bränsle=input("Ange ungefärlig mängd bränsle som gått åt i liter: ")
    kostnad=float(input("Hur mycket kostar bränslet per liter?"))
    mil_pris=int(bränsle/sträcka)
    total_kostnad=float(mil_pris*sträcka)


    data={
        "Datum": datum,
        "Regnummer":regnr_journal,
        "Start": start,
        "Destination": dest,
        "Sträcka": sträcka,
        "Förbrukning": bränsle,
        "Snittförbrukning": mil_pris,
        "Kostnad": total_kostnad,
    }

    with open(BASE_PATH + regnr_journal, "a", encoding="utf-8") as fil:
        json.dump(data, fil, ensure_ascii=False)
        fil.write("\n")
        print(Fore.GREEN + (f"Sparat i filen: {regnr_journal}"))
        Fore.RESET
    
while True:
    print("\n***Huvudmeny***\n",
    "1. Öppna servicebok\n", 
    "2. Skriv ny servicerad\n", 
    "3. Få reda på data om specifik bil\n",  #Vätskemängder, serviceintervall, sådant som är bra att veta, kommande reparationer.
    "4. Lägg in nytt regnummer\n", 
    "5. Körjournal\n",      # En körjournal som kan räkna fram snittförbrukning, kostnaden, kostnaden/mil.
    "6. Kunskapsbanken\n",  #Här lagras kunskap som är bra att veta om respektive fordon
    "7. Avsluta program\n")

    menyval=int(input("Ange ett menyval: "))
    if menyval==1:
        open_servicebook()
    elif menyval==2:
        ny_service()
    elif menyval==3:
        bildata()
    elif menyval==4:
        nytt_regnr()
    elif menyval==5:
        körjournal()
    elif menyval==6:
        kunskapsbank()
    elif menyval==7:
        break
    else:
        print("Ogiltligt val, försök igen.")
