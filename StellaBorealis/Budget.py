#Budget
import os
import datetime
import json
import time
import re
from colorama import init, Fore, Style
init(autoreset=True)

BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = os.path.join(BASE_DIR, "Budget")
os.makedirs(BASE_PATH, exist_ok=True)

def _file_path(name: str) -> str:
    if not name.endswith(".json"):
        name += ".json"
        os.path.join(BASE_PATH, name)

def sold_vehicle():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    vehicles_path = os.path.join(base_dir, "Vehicles")
    os.makedirs(vehicles_path, exist_ok=True)

    reg = input("Enter registration-number of the vehicle that is sold: ")
    reg = re.sub(r"\s+", "", (reg or "").upper())


    filename = reg if reg.endswith(".json") else f"{reg}.json"
    path = os.path.join(vehicles_path, filename)

    ts = datetime.datetime.now().strftime("%Y-%m-%d")


    data = []
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                loaded = json.load(f)
                if isinstance(loaded, list):
                    data = loaded
        except json.JSONDecodeError:
            data = []

    data.append({"VEHICLE SOLD": ts})


    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp, path)

    print(Fore.GREEN + f"Vehicle sold! → {os.path.basename(path)}")


def is_sale_income():
    try:
        sale_kind = str(input("What kind of asset did you sale? (Property, Vehicle, Stock, Object)"))
    except ValueError:
        print("Please enter only letters without numbers: ")

    if sale_kind == "PROPERTY".upper or "Property".lower:
        pass
    elif sale_kind == "VEHICLE".upper or "vehicle".lower:
        sold_vehicle()
    elif sale_kind == "STOCK".upper or "stock".lower:
        pass
    elif sale_kind == "OBJECT".upper or "object".lower:
        pass
    else:
        print("Please enter a valid input: ")

class Budget():
    def __init__(self):
        pass

    def add_income():
        income = float(input("Please enter amount: "))
        source = input("Please enter type of income (Salary, Loan, Contribution, Inheritance, Sold-asset)")

    

    def add_expense(category, label, amount, date, recurring=False):
        pass

class Budget_AI():
    def __init__(self):
        pass
    '''BudgetAnalyzer

Input: ett Budget-objekt.

Output: comments (lista med korta “bra/mindre bra” insikter).

Regler (exempel):

Om spent(category) > limit → “Du spränger X.”

Om savings_rate < mål → “Låg sparnivå, överväg att sänka Y.”

Om recurring tar > N% av inkomsten → “Hög andel fasta kostnader.”

Trend: jämför mot föregående månad (om filen finns) och skriv “+12% på mat”.'''

def budget_menu():
    while True:
        print("***Budget menu***\n",
              "1. New budget\n",
              "2. Open budget\n",
              "3. Delete budget\n",
              "4. Budget-analyzer\n",
              "5. Exit to main menu\n")
        try:
            menu_choice = int(input("Please enter a number between 1-4: "))
        except ValueError:
            print("Please enter a number only: ")

        
        if menu_choice == 1:
            sold_vehicle()
        elif menu_choice == 2:
            pass
        elif menu_choice == 3:
            pass
        elif menu_choice == 4:
            pass
        elif menu_choice == 5:
                for i in range(3, 0, -1):
                    print(i)
                    time.sleep(0.5)
                print(Fore.BLUE + "Back to main menu...")
                import main
        else:
            print(Fore.RED + "Please enter a valid int between 1-4: ")

budget_menu()

'''
Validering & kvalitet

month måste vara giltig (YYYY-MM) och unik per fil.

amount >= 0.

category måste finnas vid expense.

currency (SEK / EUR / …) hålls konsekvent (inga blandningar).

Funktionella idéer

Rollover/kuvert: överskott i ett kuvert flyttas till nästa månad.

Återkommande: auto-lägg recurring (hyra, mobil, försäkring) vid ny månad.

Mål: savings_goal i Budget → kommentar om måluppfyllnad.

Snabbstatistik:

top_3_categories() (mest spenderat),

burn_rate_per_day() (prognos),

safe_to_spend(category).

Menyflöde (håll UI tunt)

New budget → skapa Budget(month, currency) → fråga total inkomst → välj kuvert + tak.

Open budget → välj månad → visa sammanfattning, topp-kategorier, kommentarer.

Add expense / Add income → enkel input, direkt spara.

Delete budget → plocka filen efter bekräftelse.

Analyze → kör BudgetAnalyzer och visa “bra/mindre bra”.

Naming & stil

Håll engelska konsekvent.

Klassnamn CamelCase; fält/metoder snake_case.

Datum ISO-8601 (YYYY-MM-DD). month hålls separat (YYYY-MM).

Stretch (när grunden sitter)

Export: CSV per månad / kategori.

Templates: “Student”, “Familj”, “Bilfokus” (förifyllda kategorier).

CLI-flags (Typer/Click) för snabb import: budget add expense --cat Food --amount 129.

Visualisering senare: spara data på ett sätt som är lätt att mata in i en TUI eller graf.
'''