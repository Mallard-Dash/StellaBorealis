#Ett program som håller reda på månadsbudget, räknar och som dessutom kan komma med förslag.

import math

def main_menu():
    print("\n***Huvudmeny***\n" \
    "1. Budgetering\n" \
    "2. Ekonomiska verktyg\n" \
    "3. Bilkostnader\n" \
    "4. Dagbok\n" \
    "5. Logga ut\n")


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
        print("Du är nu utloggad...")
        import login
    