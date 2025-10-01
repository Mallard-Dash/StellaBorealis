# Vehicle

import os
import json
import re
from colorama import init, Fore, Style
import datetime
import time
init(autoreset=True)

BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = os.path.join(BASE_DIR, "Vehicles")
USER_VEH_PATH = os.path.join(BASE_DIR, "VehiclesUsers")  # per-user vehicle logs
os.makedirs(BASE_PATH, exist_ok=True)
os.makedirs(USER_VEH_PATH, exist_ok=True)


def _file_path(name: str) -> str:
    name = re.sub(r"\s+", "", (name or "").upper())
    if not name.endswith(".json"):
        name += ".json"
    return os.path.join(BASE_PATH, name)

def _user_file_path(username: str) -> str:
    username = re.sub(r"\s+", "", (username or "")).lower()
    if not username.endswith(".json"):
        username += ".json"
    return os.path.join(USER_VEH_PATH, username)

def _is_valid_year(year: int) -> bool:
    return 1900 <= year <= 2028

def _is_valid_reg(registration: str):
    registration = re.sub(r"\s+", "", (registration or "").upper())
    return bool(re.fullmatch(r"[A-Z]{3}\d{3}", registration) or re.fullmatch(r"[A-Z]{3}\d{2}[A-Z]", registration))

def _load_user_vehicle(username: str) -> dict:
    path = _user_file_path(username)
    if not os.path.exists(path):
        return {"user": username, "vehicles": {}}  
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {"user": username, "vehicles": {}}

def _save_user_vehicle(username: str, data: dict) -> None:
    path = _user_file_path(username)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp, path)

def mark_vehicle_sold(registration: str) -> bool: #This is the magic from when a vehicle is sold in budget.py
    """Append a 'VEHICLE SOLD' entry to Vehicles/<REG>.json."""
    registration = re.sub(r"\s+", "", (registration or "")).upper()
    filename = registration if registration.endswith(".json") else f"{registration}.json"
    path = os.path.join(BASE_PATH, filename)

    data = []
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                loaded = json.load(f)
                if isinstance(loaded, list):
                    data = loaded
                elif isinstance(loaded, dict):
                    data = [loaded]
        except json.JSONDecodeError:
            data = []

    ts = datetime.date.today().isoformat()
    data.append({"VEHICLE SOLD": ts})

    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp, path)

    print(Fore.BLUE + f"Updated vehicle file → {os.path.basename(path)}")
    return True


class Vehicle: #I wanted to implement a class for training.
    def __init__(self, vehicle_type, brand, model, year, registration, fuel, odometer_km):
        self.vehicle_type = vehicle_type
        self.brand = brand
        self.model = model

        if not isinstance(year, int) or not _is_valid_year(year):
            raise ValueError(Fore.RED + "Year must be an int between 1900 and 2028.")
        self.year = year

        registration = re.sub(r"\s+", "", (registration or "")).upper()
        if not _is_valid_reg(registration):
            raise ValueError(Fore.RED + "Registration must be ABC123 or ABC12A.")
        self.registration = registration

        self.fuel = (fuel or "").strip().upper()
        try:
            odo = float(odometer_km)
            if odo < 0:
                raise ValueError
        except Exception:
            raise ValueError(Fore.RED + "Odometer must be a non-negative number.")
        self.odometer_km = odo

    def add_new_vehicle():
        while True:
            vehicle_type = input("What type of vehicle? [Car/Motorcycle/Scooter/Boat]: ").strip().title()
            brand = input(f"What brand is your {vehicle_type}? ").strip().title()
            model = input(f"Okay you have a {brand}. What model? ").strip().title() #Kinda social user-prompt

            try:
                year = int(input("And what year was it made? ").strip())
                if not _is_valid_year(year):
                    print(Fore.RED + "Please enter a year between 1900-2028.")
                    continue
            except ValueError:
                print(Fore.RED + "Please enter a valid year (integer).")
                continue

            registration = input("Now enter the registration number (ABC123/ABC12A): ").strip().upper()
            if not _is_valid_reg(registration):
                print(Fore.RED + "Invalid registration format.")
                continue

            fuel = input(f"Fuel for {brand} [{'/'.join(['Gasoline','Diesel','Electricity','Windmill-fuel'])}]: ").strip().lower()
            if fuel == "windmill-fuel":
                check_q = input("Runs on air? (y/n): ").strip().lower() #Windmill-fuel!
                if check_q in {"y", "yes"} and vehicle_type.lower() == "boat":
                    print("A sailboat? Okay, I believe you.")
                elif check_q in {"n", "no"}:
                    fuel = input("Try again (Gasoline/Diesel/Electricity): ").strip().lower()
                else:
                    fuel = "gasoline"

            try:
                odometer = float(input("Last step now i promise. Enter your current odometer-number in kilometers: "))
            except ValueError:
                print(Fore.RED + "Please enter only numbers.")
                continue

            ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            path = _file_path(registration)

            data = []
            if os.path.exists(path):
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        if not isinstance(data, list):
                            data = []
                except json.JSONDecodeError:
                    data = []

            data.append({
                "Timestamp": ts,
                "Registration": registration,
                "Type": vehicle_type,
                "Brand": brand,
                "Model": model,
                "Year": year,
                "Fuel": fuel.capitalize(),
                "Odometer_km": odometer
            })

            tmp = path + ".tmp"
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            os.replace(tmp, path)

            print(Fore.GREEN + f"Entry saved → {os.path.basename(path)}")
            break


def add_new_trip():
    """Trip: username + reg + before/after odometer + fuel price + consumption per mil → cost estimate.
       Saves to VehiclesUsers/<username>.json under the registration."""
    username = input("Username (for your vehicle log): ").strip()
    reg = input("Registration (ABC123/ABC12A): ").strip().upper()
    if not _is_valid_reg(reg):
        print(Fore.RED + "Invalid registration format.")
        return

    try:
        odo_before = float(input("Odometer BEFORE (km): ").strip())
        odo_after  = float(input("Odometer AFTER (km): ").strip())
        if odo_after < odo_before:
            print(Fore.RED + "AFTER must be >= BEFORE.")
            return
    except ValueError:
        print(Fore.RED + "Please enter numeric odometer values.")
        return

    try:
        fuel_price = float(input("Fuel price (SEK / liter): ").strip())
        cons_per_mil = float(input("Consumption (liters per mil, i.e., per 10 km): ").strip())
    except ValueError:
        print(Fore.RED + "Please enter numeric values for price and consumption.")
        return

    distance_km = odo_after - odo_before
    distance_mil = distance_km / 10.0
    liters_used = cons_per_mil * distance_mil
    cost = round(liters_used * fuel_price, 2)

    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    data = _load_user_vehicle(username)
    v = data["vehicles"].setdefault(reg, {"trips": [], "services": [], "notes": [], "knowledge": {}})
    v["trips"].append({
        "Timestamp": ts,
        "Odometer_before_km": odo_before,
        "Odometer_after_km": odo_after,
        "Distance_km": distance_km,
        "Fuel_price_SEK_per_l": fuel_price,
        "Consumption_l_per_mil": cons_per_mil,
        "Liters_used": round(liters_used, 2),
        "Estimated_cost_SEK": cost
    })
    _save_user_vehicle(username, data)

    print(Fore.GREEN + f"Trip saved for {username} / {reg}. Estimated cost: {cost} SEK")
    #This trip-function could be evolved into something far more complex with maybe a built-in AI.

def add_new_service():
    """Service/repair entry stored under the user's vehicle log."""
    username = input("Username (for your vehicle log): ").strip()
    reg = input("Registration (ABC123/ABC12A): ").strip().upper()
    if not _is_valid_reg(reg):
        print(Fore.RED + "Invalid registration format.")
        return

    what = input("What was done? (service/repair details): ").strip()
    who  = input("By whom? (yourself / workshop): ").strip() # "Yourself" refers to the user obviously
    try:
        cost = float(input("Cost (SEK): ").strip())
    except ValueError:
        print(Fore.RED + "Please enter a numeric cost.")
        return

    try:
        odo = float(input("Odometer at service (km): ").strip())
    except ValueError:
        print(Fore.RED + "Please enter numeric odometer.")
        return

    try:
        next_service_mil = float(input("Kilometers until next service: ").strip())
    except ValueError:
        print(Fore.RED + "Please enter numeric kilometers.")
        return

    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    data = _load_user_vehicle(username)
    v = data["vehicles"].setdefault(reg, {"trips": [], "services": [], "notes": [], "knowledge": {}})
    v["services"].append({
        "Timestamp": ts,
        "What": what,
        "By": who,
        "Cost_SEK": cost,
        "Odometer_km": odo,
        "Next_service_in_km": next_service_mil
    })
    _save_user_vehicle(username, data)

    print(Fore.GREEN + f"Service entry saved for {username} / {reg}.")


def add_new_note():
    """Free-form note for the user's vehicle."""
    username = input("Username (for your vehicle log): ").strip()
    reg = input("Registration (ABC123/ABC12A): ").strip().upper()
    if not _is_valid_reg(reg):
        print(Fore.RED + "Invalid registration format.")
        return

    note = input("Note text: ").strip()
    if not note:
        print(Fore.YELLOW + "Empty note ignored.")
        return

    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    data = _load_user_vehicle(username)
    v = data["vehicles"].setdefault(reg, {"trips": [], "services": [], "notes": [], "knowledge": {}})
    v["notes"].append({
        "Timestamp": ts,
        "Text": note
    })
    _save_user_vehicle(username, data)

    print(Fore.GREEN + f"Note saved for {username} / {reg}.")


def knowledge_db():
    """Store facts about a vehicle (fluids, weights, tips, etc.) under the user's vehicle log."""
    username = input("Username (for your vehicle log): ").strip()
    reg = input("Registration (ABC123/ABC12A): ").strip().upper()
    if not _is_valid_reg(reg):
        print(Fore.RED + "Invalid registration format.")
        return

    print("Enter key/value pairs (e.g., 'Engine oil capacity' -> '5.7 L'). Leave key empty to stop.")
    data = _load_user_vehicle(username)
    v = data["vehicles"].setdefault(reg, {"trips": [], "services": [], "notes": [], "knowledge": {}})

    while True:
        key = input("Key: ").strip()
        if not key:
            break
        val = input("Value: ").strip()
        v["knowledge"][key] = val
        print(Fore.GREEN + f"Saved: {key} = {val}")

    _save_user_vehicle(username, data)
    print(Fore.BLUE + f"Knowledge DB updated for {username} / {reg}.")

def vehicles():
    while True:
        print("\n***Vehicle-menu***\n",
            "1. Add new vehicle\n",
            "2. Enter new service/repair\n",
            "3. Car details (mark as sold)\n",
            "4. Trip journal\n",
            "5. Add new note\n",
            "6. Knowledge database\n",
            "7. Exit to main menu\n")

        try:
            menuc = int(input("Input a number between 1-7: "))
        except ValueError:
            print("Please input an integer: ")
            continue

        if menuc == 1:
            Vehicle.add_new_vehicle()
        elif menuc == 2:
            add_new_service()
        elif menuc == 3:
            reg = input("Registration to mark SOLD (ABC123/ABC12A): ").strip().upper() #Manually mark a vehicle as SOLD, creates a new file if not exist.
            if _is_valid_reg(reg):
                mark_vehicle_sold(reg)
            else:
                print(Fore.RED + "Invalid registration format.")
        elif menuc == 4:
            add_new_trip()
        elif menuc == 5:
            add_new_note()
        elif menuc == 6:
            knowledge_db()
        elif menuc == 7:
            for i in range(3, 0, -1):
                print(i)
                time.sleep(0.5)
            print(Fore.BLUE + "Back to main menu...")
            try:
                import main
                main.run_app()
            except Exception:
                pass
            break
        else:
            print("Invalid input. Please enter a choice between 1-7")

if __name__ == "__main__":
    vehicles()