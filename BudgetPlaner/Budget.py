#Budgeteringssidan
import os
import datetime
import json
from colorama import init, Fore, Style
BASE_PATH = os.path.join(os.getcwd(), "Budget-") #Skapar en mapp som heter "Budget-'namn'"
os.makedirs(BASE_PATH, exist_ok=True)

def budget():                               #Menyval i print-format. Riktiga menyn är längst ner.
    print("\n***Budgetmeny***\n" \
    "1. Skapa en ny månadsbudget\n" \
    "2. Öppna befintlig budget\n" \
    "3. Ange ett nytt sparmål\n" \
    "4. Tillbaka till huvudmeny\n")


def månadsbudget_meny():
    namn=input("Ange ditt användarnamn\n")
    month=input("Vilken månad ska budgeten avse?\n")
    lön=int(input("Ange nettolön i hela siffror utan mellanslag.\n"))
    boende=int(input("Ange dina kostnader för bolån, hyra, hemförsäkring: \n"))
    el=int(input("Ange din el-kostnad: \n"))
    fordon=int(input("Ange dina fordonskostnader såsom drivmedel, underhåll, försäkring: \n"))
    lån=int(input("Ange dina lånekostnader för alla lån utom bolån: \n"))
    resor=int(input("Ange dina resekostnader såsom busskort, taxi, färjor: \n"))
    mat=int(input("Ange dina matkostnader både hemma och ute: \n"))
    förbrukningsvaror=int(input("Ange kostnaden för tillexempel; wc-papper, tvättmedel : \n"))
    hygien=int(input("Ange dina kostnader för tillexempel; schampo, tvål, hudkräm, rakartiklar, tandkräm: \n"))
    godis=int(input("Ange dina kostnader för godis, tobak, alkohol m.m: \n"))
    kläder=int(input("Ange dina kostnader för kläder och skor: \n"))
    fritid=int(input("Ange dina kostnader för Böcker, cykel, föreningsavgifter, hobby m.m: \n"))
    möbler=int(input("Ange dina kostnader för möbler eller andra husgeråd till hemmet: \n"))
    hälsa=int(input("Ange kostnader för läkarbesök, mediciner, gymkort m.m: \n"))
    djur=int(input("Ange kostnader för eventuella husdjur: \n"))
    mobil=int(input("Ange kostnader för telefonabonnemang, prenumerationer m.m\n"))

    total_utgift=boende+el+fordon+lån+resor+mat+förbrukningsvaror+hygien+godis+kläder+fritid+möbler+hälsa+djur+mobil
    resterande=lön-total_utgift

    x=datetime.datetime.now()
    ts= x.now().strftime("%b-%d-%Y--%H:%M")

    mån={"Budgeten avser följande månad": month}
    inc={"Lön": lön}

    entry1={"Boende": boende}
    entry2={"El": el}
    entry3={"Fordon": fordon}
    entry4={"övriga lån": lån}
    entry5={"Resor": resor}
    entry6={"Mat": mat}
    entry7={"Förbrukningsvaror": förbrukningsvaror}
    entry8={"Hygien": hygien}
    entry9={"Godis": godis}
    entry10={"Kläder": kläder}
    entry11={"Fritid": fritid}
    entry12={"Möbler": möbler}
    entry13={"Hälsa": hälsa}
    entry14={"Djur": djur}
    entry15={"Mobiltelefon": mobil}


#Nedastående variabler används ej men var tänkta att användas i en utökad version av programmet.
    u1=("Det verkar som om dina totala utgifter är högre än din inkomst den här månaden,"
        "Du har ett underskott på ",resterande,"Kr. Kolla igenom och håll koll på utgifterna och stryp dem innan det spårar ur.")
    u2=("Din boendekostnad är mer än 30% av din lön. Kika om du kan förhandla om bättre lånevillkor med banken.")
    u3=("Du lägger cirka", fordon, "Kr på ditt/dina fordon och det är ganska mycket.\n",
        "Du kan få ner dina fordonskostnader genom att kolla var pengarna försvinner. Fråga dig själv detta:\n",
        "Kör jag mer än nödvändigt? Kan jag reparera bilen själv och utföra service på egen hand?\n",
        "Kan jag få till en annan billigare försäkring? Är bilen helt enkelt för dyr i drift?")
    u4=("Du har lånekostnader som uppgår till", lån, "Kr. Blancolån som icke sällan har hög ränta\n",
        "kan verkligen äta upp en budget. Här kan man spara mycket pengar om man slår ihop smålån\n",
        "och verkligen ser över och förstår vilka räntor man betalar.")
    u5=("Du lägger cirka", godis, "Kr på godis och/eller tobak/alkohol. Se det mer som ett 'treat' när du gjort något bra för dig själv.\n",
        "Om du dessutom röker eller snusar så finns det både pengar och hälsa att spara. Ett paket cigaretter varannan dag blir cirka 800 Kr i månaden.\n",
        "Då hade du bara haft ungefär", total_utgift-800," Kr i utgifter denna månad. Att dessutom sluta röka/snusa kommer ge dig ett längre ocvh roligare liv.")
    u6=("Höga kostnader för telefon eller netflix-abonnemang kan snabbt bli en stor hög av utgifter om man inte har koll på dem. Kolla igenom alla dina\n",
        "abonnemang det vill säga; Streamingtjänster, bredband, telefon, matlådor till dörren, m.m.")

    with open(BASE_PATH + f"{namn}.json", "a", encoding="utf-8") as f:
                                                                         #Budgetlistan
            f.write(json.dumps(mån, ensure_ascii=False) + "\n")
            f.write(json.dumps(inc, ensure_ascii=False) + "\n")
            
            f.write(json.dumps(entry1, ensure_ascii=False) + "\n")
            f.write(json.dumps(entry2, ensure_ascii=False) + "\n")
            f.write(json.dumps(entry3, ensure_ascii=False) + "\n")
            f.write(json.dumps(entry4, ensure_ascii=False) + "\n")
            f.write(json.dumps(entry5, ensure_ascii=False) + "\n")
            f.write(json.dumps(entry6, ensure_ascii=False) + "\n")
            f.write(json.dumps(entry7, ensure_ascii=False) + "\n")
            f.write(json.dumps(entry8, ensure_ascii=False) + "\n")
            f.write(json.dumps(entry9, ensure_ascii=False) + "\n")
            f.write(json.dumps(entry10, ensure_ascii=False) + "\n")
            f.write(json.dumps(entry11, ensure_ascii=False) + "\n")
            f.write(json.dumps(entry12, ensure_ascii=False) + "\n")
            f.write(json.dumps(entry13, ensure_ascii=False) + "\n")
            f.write(json.dumps(entry14, ensure_ascii=False) + "\n")
            f.write(json.dumps(entry15, ensure_ascii=False) + "\n")
            f.write(json.dumps(f"Dina totala utgifter denna månad uppgår till {total_utgift} Kr", ensure_ascii=False) + "\n")
            f.write(json.dumps(f"Då har du {resterande} Kr kvar till sparande och annat.", ensure_ascii=False) + "\n")
            print("Budget skapad..")

            #if total_utgift>lön:
                #f.write(json.dumps(u1, ensure_ascii=False) + "\n") Används ej!
            #if boende>lön%0.35:
                #f.write(json.dumps(u2, ensure_ascii=False) + "\n")
            #if fordon>5000:
                #f.write(json.dumps(u3, ensure_ascii=False) + "\n")
            #if lån>2000:
                #f.write(json.dumps(u4, ensure_ascii=False) + "\n")
            #if godis>1000:
                #f.write(json.dumps(u5, ensure_ascii=False) + "\n")
            #if mobil>1000:
                #f.write(json.dumps(u6, ensure_ascii=False) + "\n")
    
while True:       #Här är menyn för budget-delen som låter användaren välja menyval med siffror.
    budget()
    menyval=(int(input("Ange ett menyval mellan 1-4 ")))

    if menyval==1:
        månadsbudget_meny()
    if menyval==2:
        print("Öppna befintlig budget... kommer i senare version")
    if menyval==3:
        print("Nytt sparmål... kommer i senare version")
    if menyval==4:
        print("Återgår till huvudmenyn...")
        import main
    else:
        print("Ange en siffra mellan 1-4")
