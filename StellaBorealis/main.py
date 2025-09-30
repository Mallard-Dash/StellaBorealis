#Main-filen i programmet. Egentligen bara en meny för att välja dest.

import math
import colorama
from colorama import init, Fore, Style

def main_menu():
    print("\n***Huvudmeny***\n" \
    "1. Budgetering\n" \
    "2. Ekonomiska verktyg\n" \
    "3. Bilkostnader\n" \
    "4. Dagbok\n" \
    "5. Verktyg\n" \
    "6. Logga ut\n")


while True:
    main_menu()
    menyval=int(input("Ange ett menyval mellan 1-5"))
    if menyval==1:
        import Budget
    if menyval==2:
        import finance_tools
    if menyval==3:
        import bilkostnader
    if menyval==4:
        import dagbok
    if menyval==5:
        import tools
    if menyval==6:
        print(Fore.YELLOW+("Du är nu utloggad..."))
        Fore.RESET
        import login
    