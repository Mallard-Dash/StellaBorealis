#Den programdel som ansvarar för finansverktyg. Tanken är att hjälpa användaren med ekonomiska råd.
import colorama
import math
from colorama import init, Fore, Style

        
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

#def sparmål():
    

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
        print("Kommer snart...")
    elif menyval==3:
        kalkylator()
    elif menyval==4:
        import main



    
    

            