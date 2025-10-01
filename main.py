# StellaBorealis — main.py

from colorama import init, Fore
init(autoreset=True)

from banner import show_banner
import login

def print_main_menu():
    print(
        "\n*** Main menu ***\n"
        "1. Budget\n"
        "2. Financial tools\n"
        "3. Vehicles\n"
        "4. Diary\n"
        "5. Misc tools\n"
        "6. Log off\n"
    )

def run_app():
    """Inner app loop shown after a successful login."""
    while True:
        print_main_menu()
        choice = input("Please enter a menu choice (1-6): ").strip()

        if choice == "1":
            try:
                import Budget
                Budget.budget_menu()
            except Exception as e:
                print(Fore.RED + f"Budget module error: {e}")

        elif choice == "2":
            try:
                import finance_tools
                finance_tools.fin_tools_menu()
            except Exception as e:
                print(Fore.RED + f"Finance tools error: {e}")

        elif choice == "3":
            try:
                import vehicle
                vehicle.vehicles()
            except Exception as e:
                print(Fore.RED + f"Vehicle module error: {e}")

        elif choice == "4":
            try:
                import diary
                diary.run_diary()
            except Exception as e:
                print(Fore.RED + f"Diary module error: {e}")

        elif choice == "5":
            try:
                import tools
                tools.tool_menu()
            except Exception as e:
                print(Fore.RED + f"Tools module error: {e}")

        elif choice == "6":
            print(Fore.BLUE + "Logging off... Bye :)")
            # Return to caller so we can re-run login if desired
            return

        else:
            print(Fore.RED + "Please enter a number from 1-6.")

def main():
    # 1) Show banner immediately on app start
    show_banner(animate=True, twinkle_frames=20, fps=9)

    # 2) Outer loop: login → app → logoff → (optionally login again)
    while True:
        logged_in = login.login_menu()   # login.py handles the menu; returns True/False
        if not logged_in:
            print("Goodbye.")
            login.close_db()
            break

        # Run the main app loop; returns when user chooses "Log off"
        run_app()

        # After logoff, ask if user wants to login again
        again = input("Log in again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Goodbye.")
            login.close_db()
            break

if __name__ == "__main__":
    main()
