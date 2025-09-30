#Den programdel som ansvarar för finansverktyg. Tanken är att hjälpa användaren med ekonomiska råd.
import colorama
import math
import json
import os
from colorama import init, Fore, Style
BASE_PATH = os.path.join(os.getcwd(), "Budget-") #Skapar en mapp som heter "Budget-'namn'"
os.makedirs(BASE_PATH, exist_ok=True)

        
def ränta_på_ränta():
    print("Ränta-på-ränta är en ekonomisk effekt med stor potential. Tanken är att pengar som växer genom ränta",
          "kommer bli större, och sen blir pengarna + ränta ännu större. Det brukar jämföras med en snöboll",
          "som rullas utför en backe. I början är det bara en liten snöboll, men ju längre ner för backen",
          "den rullar desto större blir den. I den här kalkylatorn kan du ange startkapital, ränta och år",
          "för att få fram hur kraftig ränta-på-ränta effekten kan vara.")

    startkapital=int(input("Ange startkapital: "))
    ränta=int(input("Ange räntan i procent: "))
    år=int(input("Ange antal år: "))
    svar=startkapital*(1+ränta/100)*år
    utr=ränta_på_ränta(startkapital,ränta,år)
    print(f"Du har angett följande: \n",
          f"Startkapital = {startkapital}Kr\n",
          f"Ränta = {ränta} %\n",
          f"Antal år = {år} år\n",
          f"Total summa = {utr:1f} Kr")
    return svar

def sparmål():
    namn=(input("Ange ditt användarnamn: "))
    sparmål=(input("Ange ditt sparmål: (Tex. Ny bil, resa, buffert) "))
    målbelopp=int(input("Ange ditt målbelopp: (Hur mycket kostar det du vill spara till?) "))
    månadssparande=int(input("Ange ditt månadssparande: (Hur mycket kan du spara varje månad?) "))

    with open(BASE_PATH + f"{namn}_sparmål.json", "a", encoding="utf-8") as f:
        f.write(json.dumps(f"Sparmål {sparmål}", ensure_ascii=False) + "\n")
        f.write(json.dumps(f"Målbelopp: {målbelopp} Kr", ensure_ascii=False) + "\n")
        f.write(json.dumps(f"Månadssparande: {månadssparande} Kr", ensure_ascii=False) + "\n")
        f.write(json.dumps(f"Du kommer nå ditt sparmål om {målbelopp/månadssparande:.1f} månader", ensure_ascii=False) + "\n")
        f.write(json.dumps(f"Detta är ungefär {målbelopp/månadssparande/12:.1f} år", ensure_ascii=False) + "\n")
        print(Fore.GREEN("Sparmål skapat.."))
        Fore.RESET
    

def kalkylator():
    x=float(input("Ange första talet: "))
    y=float(input("Ange andra talet, annars skriv 0: "))
    opr=input("Välj räkneoperation (+, -, *, /, x**y, root)")
    if opr=="+":
        print ("Svar: ",x+y)
    elif opr=="-":
        print ("Svar: ",x-y)
    elif opr=="*":
        print ("Svar: ",x*y)
    elif opr=="/":
        print ("Svar: ",x/y)
    elif opr=="x**y":
        print ("Svar: ",x**y)
    elif opr=="root":
        print ("Svar: ",math.sqrt(x))


while True:
    print("\n***Finans-meny***\n",
        "1. Räkna ränta-på-ränta\n",
        "2. Ange sparmål\n",
        "3. Öppna kalkylatorn\n",
        "4. Tillbaka till huvudmeny\n")
    menyval=(int(input("Ange ett menyval mellan 1-4 ")))

    if menyval==1:
        ränta_på_ränta()
    elif menyval==2:
        sparmål()
    elif menyval==3:
        kalkylator()
    elif menyval==4:
        import main



    
    

            