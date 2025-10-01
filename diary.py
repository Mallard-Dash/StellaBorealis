# Diary

import os
import datetime
import time
import json
from colorama import init, Fore, Style
init(autoreset=True)

BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = os.path.join(BASE_DIR, "Diary")
os.makedirs(BASE_PATH, exist_ok=True)

def _file_path(name: str) -> str:
    name = (name or "").strip()
    if not name.endswith(".json"):
        name += ".json"
    return os.path.join(BASE_PATH, name)

def new_diary():
    """Write a new diary entry. Creates the diary file if it doesn't exist."""
    username = input("Enter your username: ").strip()
    content  = input("Write diary entry: \n")

    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    path = _file_path(username)

    data = []
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if not isinstance(data, list):
                    data = []
        except json.JSONDecodeError:
            data = []

    # Append entry
    data.append({"timestamp": ts, "content": content})

    # Write as JSON
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(Fore.GREEN + f"Entry saved → {os.path.basename(path)}")

def open_diary():
    """List available diaries and open one to read."""
    print("Available diaries:")
    files = sorted(f for f in os.listdir(BASE_PATH) if f.endswith(".json"))
    if not files:
        print(Fore.YELLOW + "(no diaries yet)")
    else:
        for f in files:
            print(Fore.YELLOW + f)

    while True:
        try:
            name = input(Fore.RESET + "Enter diary filename (with or without .json): ").strip()
            path = _file_path(name)
            if os.path.exists(path):
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    if not data:
                        print(Fore.YELLOW + "(empty diary)")
                    else:
                        print(Style.BRIGHT + f"\n--- {os.path.basename(path)} ---")
                        for i, entry in enumerate(data, 1):
                            ts = entry.get("timestamp", "?")
                            ct = entry.get("content", "")
                            print("--------------------------------------------------------------------")
                            print(f"{i:02d}. [{ts}] {ct}")
                        print("--------------------------------------------------------------------")
                except json.JSONDecodeError:
                    print(Fore.RED + "Corrupted/invalid JSON file.")
                break
            else:
                print(Fore.RED + "The file does not exist, try again.")
        except KeyboardInterrupt:
            print("\nCancelled by user.")
            break

def remove_diary():
    """Delete a diary file by username."""
    username = input("Enter your username: ").strip()
    path = _file_path(username)

    if os.path.exists(path):
        os.remove(path)
        print(Fore.GREEN + "Diary deleted.")
    else:
        print(Fore.RED + "File not found.")

def run_diary():
    while True:
        print("\n--- Diary ---\n"
              "1. New diary entry\n"
              "2. Open diary\n"
              "3. Delete diary\n"
              "4. Exit to main menu\n")
        try:
            choice = int(input("Enter a choice between 1-4: "))
        except ValueError:
            print(Fore.RED + "Only integers are allowed.")
            continue

        if choice == 1:
            new_diary()
        elif choice == 2:
            open_diary()
        elif choice == 3:
            remove_diary()
        elif choice == 4:
            for i in range(3, 0, -1):
                print(i)
                time.sleep(0.5)
            print(Fore.BLUE + "Returning to main menu...")
            try:
                import main
                main.run_app()  # call main menu
            except Exception:
                pass
            break
        else:
            print(Fore.RED + "Invalid input. Please enter a choice between 1-4.")

if __name__ == "__main__":
    run_diary()
