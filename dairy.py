#Dairy

import os
import datetime
from colorama import init, Fore, Style
import time
import json
init(autoreset=True)
BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = os.path.join(BASE_DIR, "Diary")
os.makedirs(BASE_PATH, exist_ok=True)

def _file_path(name: str) -> str:
    if not name.endswith(".json"):
        name += ".json"
    return os.path.join(BASE_PATH, name)

def new_dairy(): #Write new dairy, if it does not exist a new one is created
        name=input("Enter your username: \n").strip()
        cont=input("Write dairy inquiry: \n")
        x=datetime.datetime.now()
        ts= x.now().strftime("%b-%d-%Y--%H:%M")

        path = _file_path(name)

        data = []
        if os.path.exists(path):
            try:
              with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if not isinstance(data, list):
                    data = []
            except json.JSONDecodeError:
             data = []

    # Append inquiry
        data.append({"timestamp": ts, "content": cont})

    # Write as Json
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(Fore.GREEN + f"Entry saved → {os.path.basename(path)}")

def open_d():
    print("Available diaries:")
    files = [f for f in os.listdir(BASE_PATH) if f.endswith(".json")]
    if not files:
        print(Fore.YELLOW + "(no diaries yet)")
    else:
        for f in files:
            print(Fore.YELLOW + f)

    while True:
        try:
            dairy = input(Fore.RESET + "Enter diary filename (with or without .json): ").strip()
            path = _file_path(dairy)
            if os.path.exists(path):
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    if not data:
                        print(Fore.YELLOW + "(empty diary)")
                    else:
                        for i, entry in enumerate(data, 1):
                            ts = entry.get("timestamp", "?")
                            ct = entry.get("content", "")
                            print("--------------------------------------------------------------------")
                            print(f"{i:02d}. [{ts}] {ct}", end="")
                            print("\n--------------------------------------------------------------------")
                except json.JSONDecodeError:
                    print(Fore.RED + "Corrupted/invalid JSON file.")
                break
            else:
                print(Fore.RED + "The file does not exist, try again.")
        except KeyboardInterrupt:
            print("\nCancelled by user.")
            break

def remove_d():
        namn = input("Enter your username: ").strip() # Delete dairy
        file = os.path.join(BASE_PATH, f"{namn}.json")

        if os.path.exists(file):
                os.remove(file)
                print(Fore.GREEN+("Dairy deleted.."))
                Fore.RESET
        else:
                print(Fore.RED+("File not found..."))
                Fore.RESET
                         
while True:
        print("\n---Dairy---\n", #Dairy-menu
        "1. New dairy-inquiry\n",
        "2. Open dairy\n",
        "3. Delete dairy\n",
        "4. Exit to main-menu\n")
        try:
            val=int(input("Enter a choice between 1-4: "))
        except ValueError:
             print("Only integers are allowed.")
        if val==1:
                new_dairy()

        elif val==2:
                open_d()

        elif val==3:
                remove_d()

        elif val==4:
                for i in range(3, 0, -1):
                    print(i)
                    time.sleep(0.5)
                print(Fore.BLUE + "Returning to main menu...")
                Fore.RESET
                import main
        else:
            print("Invalid input. Please enter a choice between 1-7")
    

             
             
                     