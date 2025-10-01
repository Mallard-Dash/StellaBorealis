# Budget - StellaBorealis (simple MVP)
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


def _file_path(username: str) -> str:
    """Return path to user budget file"""
    filename = f"{username}.json"
    return os.path.join(BASE_PATH, filename)


def _load_user(username: str) -> dict:
    """Load user data or init structure"""
    path = _file_path(username)
    if not os.path.exists(path):
        return {"user": username, "months": {}}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {"user": username, "months": {}}


def _save_user(username: str, data: dict) -> None:
    """Save user data"""
    path = _file_path(username)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp, path)


def sold_vehicle(username: str):
    reg = input("Enter registration-number of the vehicle that is sold: ").strip().upper()
    reg = re.sub(r"\s+", "", (reg or ""))
    '''
    The idea is that this file 'talks' with the vehicle-file.
    If the entered sold vehicles registration number matches a vehicle in corresponding file,
    the program will write that that vehicle is sold with todays date.
    '''
    
    raw_amount = input("Enter sale amount (SEK) [press Enter to skip]: ").strip()
    amount = None
    if raw_amount:
        try:
            amount = float(raw_amount)
        except ValueError:
            print(Fore.YELLOW + "Invalid amount. Skipping income value.")
            amount = None

    # 1) Update the USER budget file under current month
    ts = datetime.date.today().isoformat()
    month = datetime.date.today().strftime("%Y-%m")

    data = _load_user(username)  # uses your helpers from earlier
    data["months"].setdefault(month, {"incomes": [], "expenses": [], "comments": []})

    income_entry = {
        "type": "Vehicle sale",
        "registration": reg,
        "date": ts
    }
    if amount is not None:
        income_entry["amount"] = amount

    data["months"][month]["incomes"].append(income_entry)
    _save_user(username, data)
    print(Fore.GREEN + f"Vehicle sale logged in {username}.json")

    # 2) Update the VEHICLE file (Vehicles/<REG>.json) to append 'VEHICLE SOLD'
    try:
        # If your file is named vehicle.py:
        from vehicle import mark_vehicle_sold
        mark_vehicle_sold(reg)
    except Exception:
        # Fallback: write directly if import failed
        vehicles_path = os.path.join(BASE_DIR, "Vehicles")
        os.makedirs(vehicles_path, exist_ok=True)
        filename = reg if reg.endswith(".json") else f"{reg}.json"
        path = os.path.join(vehicles_path, filename)

        veh_data = []
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    loaded = json.load(f)
                    if isinstance(loaded, list):
                        veh_data = loaded
                    elif isinstance(loaded, dict):
                        veh_data = [loaded]
            except json.JSONDecodeError:
                veh_data = []

        veh_data.append({"VEHICLE SOLD": ts}) #<-----This is the append-line i mentioned before
        tmp = path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(veh_data, f, ensure_ascii=False, indent=2)
        os.replace(tmp, path)
        print(Fore.BLUE + f"(fallback) Updated vehicle file → {os.path.basename(path)}")




def sold_property(username: str):
    try:
        amount = float(input("Enter property sale income: "))
    except ValueError:
        print("Please enter only numbers.")
        return

    ts = datetime.date.today().isoformat() #Timestamp variable

    data = _load_user(username)
    month = datetime.date.today().strftime("%Y-%m")
    data["months"].setdefault(month, {"incomes": [], "expenses": [], "comments": []})

    data["months"][month]["incomes"].append({
        "type": "Property sale",
        "amount": amount,
        "date": ts
    }) #The data is then added to the user budget

    _save_user(username, data)
    print(Fore.GREEN + "Property sale saved.")


def sold_stock(username: str): #This function could have future-potential
    try:
        amount = float(input("Enter stock sale income: "))
    except ValueError:
        print("Please enter only numbers.")
        return

    ts = datetime.date.today().isoformat()

    data = _load_user(username)
    month = datetime.date.today().strftime("%Y-%m")
    data["months"].setdefault(month, {"incomes": [], "expenses": [], "comments": []})

    data["months"][month]["incomes"].append({
        "type": "Stock sale",
        "amount": amount,
        "date": ts
    })

    _save_user(username, data)
    print(Fore.GREEN + "Stock sale saved.") 


def sold_object(username: str):
    try:
        amount = float(input("Enter how much income you gained from sold object: "))
    except ValueError:
        print("Please enter only numbers.")
        return

    taxated = input("Did you pay tax for the sold object? (yes/no): ").strip().lower()

    net_income = amount
    taxes = 0.0
    if taxated in ("yes", "y"):
        try:
            tax_percent = float(input("How many percent is the tax? "))
            taxes = amount * (tax_percent / 100)
            net_income = amount - taxes
        except ValueError:
            print("Invalid tax input.")

    ts = datetime.date.today().isoformat()
    data = _load_user(username)
    month = datetime.date.today().strftime("%Y-%m")
    data["months"].setdefault(month, {"incomes": [], "expenses": [], "comments": []})

    data["months"][month]["incomes"].append({
        "type": "Object sale",
        "amount": amount,
        "net_income": net_income,
        "taxes": taxes,
        "date": ts
    })

    _save_user(username, data)
    print(Fore.GREEN + f"Object sale saved. Net: {net_income} SEK")


def is_sale_income(username: str):
    sale_kind = input("What kind of asset did you sell? (Property, Vehicle, Stock, Object): ").strip().lower()
    if sale_kind == "property":
        sold_property(username)
    elif sale_kind == "vehicle":
        sold_vehicle(username)
    elif sale_kind == "stock":
        sold_stock(username)
    elif sale_kind == "object":
        sold_object(username)
    else:
        print("Please enter a valid input.")
        #In the future this could be expanded with more options


class Budget():
    def __init__(self, username: str):
        self.username = username

    def add_income(self):
        try:
            income = float(input("Please enter amount: "))
        except ValueError:
            print("Please enter only numbers.")
            return

        source = input("Please enter type of income (Salary, Loan, Contribution, Inheritance, Sold-asset): ").strip().lower()
        ts = datetime.date.today().isoformat()
        month = datetime.date.today().strftime("%Y-%m")

        data = _load_user(self.username)
        data["months"].setdefault(month, {"incomes": [], "expenses": [], "comments": []})

        if source in ("sold-asset", "asset", "sale"):
            is_sale_income(self.username)
        else:
            data["months"][month]["incomes"].append({
                "type": source,
                "amount": income,
                "date": ts
            })
            _save_user(self.username, data)
            print(Fore.GREEN + "Income saved.")

    def add_expense(self):
        category = input("Category (e.g. Housing, Food, Transport): ").strip()
        label = input("Label (e.g. Rent, Groceries, Diesel): ").strip()
        try:
            amount = float(input("Please enter amount: "))
        except ValueError:
            print("Please enter only numbers.")
            return

        ts = datetime.date.today().isoformat()
        month = datetime.date.today().strftime("%Y-%m")

        data = _load_user(self.username)
        data["months"].setdefault(month, {"incomes": [], "expenses": [], "comments": []})
        data["months"][month]["expenses"].append({
            "category": category,
            "label": label,
            "amount": amount,
            "date": ts
        })

        _save_user(self.username, data)
        print(Fore.GREEN + "Expense saved.")

    def write_month_budget(self):
        """Write a summary for current month into comments."""
        month = datetime.date.today().strftime("%Y-%m")
        data = _load_user(self.username)
        if month not in data["months"]:
            print("No data for this month.")
            return

        incomes = sum(i.get("amount", i.get("net_income", 0)) for i in data["months"][month]["incomes"])
        expenses = sum(e["amount"] for e in data["months"][month]["expenses"])
        balance = incomes - expenses

        comment = f"Summary for {month}: Incomes={incomes}, Expenses={expenses}, Balance={balance}"
        if expenses > incomes:
            comment += " (Warning: expenses exceed incomes!)"

        data["months"][month]["comments"].append(comment)
        _save_user(self.username, data)
        print(Fore.BLUE + "Month budget summary written.")


class Budget_AI(): #This class is for future use!
    def __init__(self):
        pass


def budget_menu():
    username = input("Enter your username: ").strip()
    b = Budget(username)

    while True:
        print("***Budget menu***\n",
              "1. Add income\n",
              "2. Add expense\n",
              "3. Write month budget summary\n",
              "4. Exit to main menu\n")
        try:
            menu_choice = int(input("Please enter a number between 1-4: "))
        except ValueError:
            print(Fore.RED + "Please enter a number only: ")
            continue

        if menu_choice == 1:
            b.add_income()
        elif menu_choice == 2:
            b.add_expense()
        elif menu_choice == 3:
            b.write_month_budget()
        elif menu_choice == 4:
            for i in range(3, 0, -1):
                print(i)
                time.sleep(0.5)
            print(Fore.BLUE + "Back to main menu...")
            import main
            main.run_app()
        else:
            print(Fore.RED + "Please enter a valid int between 1-4: ")

if __name__ == "__main__":
    budget_menu()


    #Say hi to Fred!
    
    ####--------#####
    ##             ##
    #   O      O    #
    #              #
    ##      V     ##
    ####         ####
    #################