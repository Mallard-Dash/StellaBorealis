#Vehicle

import os
import json
import re
from colorama import init, Fore, Style
import datetime
import time
init(autoreset=True)
BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = os.path.join(BASE_DIR, "Vehicles")
os.makedirs(BASE_PATH, exist_ok=True)


def _file_path(name: str) -> str:
    name = re.sub(r"\s+", "", (name or "").upper())
    if not name.endswith(".json"):
        name += ".json"
    return os.path.join(BASE_PATH, name)

def _is_valid_year(year: int) -> bool:
    return 1900 <= year <= 2028

def _is_valid_reg(registration: str):
        registration = re.sub(r"\s+", "", (registration or "").upper())
        return bool(re.fullmatch(r"[A-Z]{3}\d{3}", registration) or re.fullmatch(r"[A-Z]{3}\d{2}[A-Z]", registration))


class Vehicle:
    def __init__(self, vehicle_type, brand, model, year, registration, fuel, odometer_km):
        self.vehicle_type = vehicle_type #Is it a motorbike, car or prehaps even a boat?
        self.brand = brand 
        self.model = model
        self.year = year  #Registration year
        self.registration = registration.upper() #Registration number
        self.fuel = fuel #What kind of fuel drives this vehicle?
        self.odometer_km = odometer_km (float, odometer_km > 0) #How many kilometers has this vehicle traveled in it's lifetime?

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
            if odo < 0: raise ValueError
        except Exception:
            raise ValueError(Fore.RED + "Odometer must be a non-negative number.")
        self.odometer_km = odo

    def add_new_vehicle():
        while True:
            vehicle_type = input("What type of vehicle? [Car/Motorcycle/Scooter/Boat]: ").strip().title()
            brand = input(f"What brand is your {vehicle_type}? ").strip().title()
            model = input(f"Okay you have a {brand}. What model? ").strip().title()

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
                check_q = input("Runs on air? (y/n): ").strip().lower()
                if check_q in {"y", "yes"} and vehicle_type.lower() == "boat":
                    print("A sailboat? Okay, I believe you.")
                elif check_q in {"n", "no"}:
                    fuel = input("Try again (Gasoline/Diesel/Electricity): ").strip().lower()
                else:
                    # default to gas if answer is weird
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

            # Append post
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
    pass
def add_new_service():
    pass
def add_new_note():
    pass
def knowledge_db(): 
    pass 
    
    
while True:
    print("\n***Vehicle-menu***\n",
    "1. Add new vehicle\n", 
    "2. Enter new serviceline\n", 
    "3. Car details\n",  
    "4. Trip journal\n", 
    "5. Add new note\n",      
    "6. Knowledge database\n",  
    "7. Exit to main menu\n")

    try:
        menuc=int(input("Input a number between 1-7: "))
    except ValueError:
        print("Please input an integer: ")
    
    if menuc==1:
        Vehicle.add_new_vehicle()
    elif menuc==2:
        pass
    elif menuc==3:
        pass
    elif menuc==4:
        pass
    elif menuc==5:
        pass
    elif menuc==6:
        pass
    elif menuc==7:
            for i in range(3, 0, -1):
                print(i)
                time.sleep(0.5)
            print(Fore.BLUE + "Back to main menu...")
            import main
    else:
        print("Invalid input. Please enter a choice between 1-7")
