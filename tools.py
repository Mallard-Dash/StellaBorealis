# Here we have other tools that can be useful.

import os
import json
import math
import colorama
from colorama import init, Fore, Style
init(autoreset=True)

def convert_units():  # Unit converter with submenus for different units
    print(
        "\n---Unit Converter---\n",
        "1. Length\n",
        "2. Weight\n",
        "3. Volume\n",
        "4. Temperature\n",
        "5. Back to tools menu\n"
    )
    try:
        choice = int(input("Enter a choice between 1-5: "))
    except (ValueError, EOFError, KeyboardInterrupt):
        print(Fore.RED + "Please enter an integer between 1-5.")
        return

    if choice == 1:
        print(
            "\n---Length---\n",
            "1. Meters to Kilometers\n",
            "2. Kilometers to Meters\n",
            "3. Centimeters to Meters\n",
            "4. Meters to Centimeters\n",
            "5. Inches to Centimeters\n",
            "6. Centimeters to Inches\n"
        )
        try:
            sub = int(input("Enter a choice between 1-6: "))
        except (ValueError, EOFError, KeyboardInterrupt):
            print(Fore.RED + "Please enter an integer between 1-6.")
            return

        if sub == 1:
            try:
                meters = float(input("Enter meters: "))
                print(f"{meters} meters = {meters / 1000} kilometers")
            except (ValueError, EOFError, KeyboardInterrupt):
                print(Fore.RED + "Please enter a valid number.")
        elif sub == 2:
            try:
                km = float(input("Enter kilometers: "))
                print(f"{km} kilometers = {km * 1000} meters")
            except (ValueError, EOFError, KeyboardInterrupt):
                print(Fore.RED + "Please enter a valid number.")
        elif sub == 3:
            try:
                cm = float(input("Enter centimeters: "))
                print(f"{cm} centimeters = {cm / 100} meters")
            except (ValueError, EOFError, KeyboardInterrupt):
                print(Fore.RED + "Please enter a valid number.")
        elif sub == 4:
            try:
                meters = float(input("Enter meters: "))
                print(f"{meters} meters = {meters * 100} centimeters")
            except (ValueError, EOFError, KeyboardInterrupt):
                print(Fore.RED + "Please enter a valid number.")
        elif sub == 5:
            try:
                inches = float(input("Enter inches: "))
                print(f"{inches} inches = {inches * 2.54} centimeters")
            except (ValueError, EOFError, KeyboardInterrupt):
                print(Fore.RED + "Please enter a valid number.")
        elif sub == 6:
            try:
                cm = float(input("Enter centimeters: "))
                print(f"{cm} centimeters = {cm / 2.54} inches")
            except (ValueError, EOFError, KeyboardInterrupt):
                print(Fore.RED + "Please enter a valid number.")
        else:
            print("Invalid choice, try a number between 1-6.")

    elif choice == 2:
        print(
            "\n---Weight---\n",
            "1. Grams to Kilograms\n",
            "2. Kilograms to Grams\n",
            "3. Pounds to Kilograms\n",
            "4. Kilograms to Pounds\n"
        )
        try:
            sub = int(input("Enter a choice between 1-4: "))
        except (ValueError, EOFError, KeyboardInterrupt):
            print(Fore.RED + "Please enter an integer between 1-4.")
            return

        if sub == 1:
            try:
                g = float(input("Enter grams: "))
                print(f"{g} grams = {g / 1000} kilograms")
            except (ValueError, EOFError, KeyboardInterrupt):
                print(Fore.RED + "Please enter a valid number.")
        elif sub == 2:
            try:
                kg = float(input("Enter kilograms: "))
                print(f"{kg} kilograms = {kg * 1000} grams")
            except (ValueError, EOFError, KeyboardInterrupt):
                print(Fore.RED + "Please enter a valid number.")
        elif sub == 3:
            try:
                lbs = float(input("Enter pounds: "))
                print(f"{lbs} pounds = {lbs * 0.453592} kilograms")
            except (ValueError, EOFError, KeyboardInterrupt):
                print(Fore.RED + "Please enter a valid number.")
        elif sub == 4:
            try:
                kg = float(input("Enter kilograms: "))
                print(f"{kg} kilograms = {kg * 2.20462} pounds")
            except (ValueError, EOFError, KeyboardInterrupt):
                print(Fore.RED + "Please enter a valid number.")
        else:
            print("Invalid choice, try a number between 1-4.")

    elif choice == 3:
        print(
            "\n---Volume---\n",
            "1. Liters to Milliliters\n",
            "2. Milliliters to Liters\n",
            "3. Gallons to Liters\n",
            "4. Liters to Gallons\n"
        )
        try:
            sub = int(input("Enter a choice between 1-4: "))
        except (ValueError, EOFError, KeyboardInterrupt):
            print(Fore.RED + "Please enter an integer between 1-4.")
            return

        if sub == 1:
            try:
                l = float(input("Enter liters: "))
                print(f"{l} liters = {l * 1000} milliliters")
            except (ValueError, EOFError, KeyboardInterrupt):
                print(Fore.RED + "Please enter a valid number.")
        elif sub == 2:
            try:
                ml = float(input("Enter milliliters: "))
                print(f"{ml} milliliters = {ml / 1000} liters")
            except (ValueError, EOFError, KeyboardInterrupt):
                print(Fore.RED + "Please enter a valid number.")
        elif sub == 3:
            try:
                gal = float(input("Enter gallons: "))
                print(f"{gal} gallons = {gal * 3.78541} liters")
            except (ValueError, EOFError, KeyboardInterrupt):
                print(Fore.RED + "Please enter a valid number.")
        elif sub == 4:
            try:
                l = float(input("Enter liters: "))
                print(f"{l} liters = {l / 3.78541} gallons")
            except (ValueError, EOFError, KeyboardInterrupt):
                print(Fore.RED + "Please enter a valid number.")
        else:
            print("Invalid choice, try a number between 1-4.")

    elif choice == 4:
        print(
            "\n---Temperature---\n",
            "1. Celsius to Fahrenheit\n",
            "2. Fahrenheit to Celsius\n",
            "3. Celsius to Kelvin\n",
            "4. Kelvin to Celsius\n"
        )
        try:
            sub = int(input("Enter a choice between 1-4: "))
        except (ValueError, EOFError, KeyboardInterrupt):
            print(Fore.RED + "Please enter an integer between 1-4.")
            return

        if sub == 1:
            try:
                c = float(input("Enter degrees Celsius: "))
                print(f"{c} °C = {c * 9 / 5 + 32} °F")
            except (ValueError, EOFError, KeyboardInterrupt):
                print(Fore.RED + "Please enter a valid number.")
        elif sub == 2:
            try:
                f = float(input("Enter degrees Fahrenheit: "))
                print(f"{f} °F = {(f - 32) * 5 / 9} °C")
            except (ValueError, EOFError, KeyboardInterrupt):
                print(Fore.RED + "Please enter a valid number.")
        elif sub == 3:
            try:
                c = float(input("Enter degrees Celsius: "))
                print(f"{c} °C = {c + 273.15} K")
            except (ValueError, EOFError, KeyboardInterrupt):
                print(Fore.RED + "Please enter a valid number.")
        elif sub == 4:
            try:
                k = float(input("Enter Kelvin: "))
                print(f"{k} K = {k - 273.15} °C")
            except (ValueError, EOFError, KeyboardInterrupt):
                print(Fore.RED + "Please enter a valid number.")
        else:
            print("Invalid choice, try a number between 1-4.")

    elif choice == 5:
        try:
            import main
            main.run_app()
        except Exception:
            # fall back to returning if main not available
            return
    else:
        print("Invalid choice, try a number between 1-5.")


def password_generator():  # Password generator
    import random
    import string

    try:
        length = int(input("Enter desired password length (minimum 6 characters): "))
    except (ValueError, EOFError, KeyboardInterrupt):
        print(Fore.RED + "Please enter a valid integer (≥ 6).")
        return
    if length < 6:
        print("Password length must be at least 6 characters.")
        return

    try:
        include_upper = input("Include uppercase letters? (y/n): ").lower().strip() == 'y'
        include_lower = input("Include lowercase letters? (y/n): ").lower().strip() == 'y'
        include_digits = input("Include digits? (y/n): ").lower().strip() == 'y'
        include_special = input("Include special characters? (y/n): ").lower().strip() == 'y'
    except (EOFError, KeyboardInterrupt):
        print("\n" + Fore.YELLOW + "Cancelled by user.")
        return

    if not (include_upper or include_lower or include_digits or include_special):
        print("You must select at least one character type.")
        return

    all_chars = ""
    upper = string.ascii_uppercase if include_upper else ""
    lower = string.ascii_lowercase if include_lower else ""
    digits = string.digits if include_digits else ""
    special = string.punctuation if include_special else ""
    all_chars = upper + lower + digits + special

    # Ensure at least one from each selected type (still minimal change)
    password_chars = []
    if include_upper:  password_chars.append(random.choice(upper))
    if include_lower:  password_chars.append(random.choice(lower))
    if include_digits: password_chars.append(random.choice(digits))
    if include_special:password_chars.append(random.choice(special))

    # Fill the rest
    try:
        remaining = max(0, length - len(password_chars))
        password_chars += [random.choice(all_chars) for _ in range(remaining)]
        random.shuffle(password_chars)
        password = ''.join(password_chars)
        print(f"Generated password: {password}")
    except Exception:
        print(Fore.RED + "Failed to generate password.")

def tool_menu():
    while True:
        print(
            "\n---Tools Menu---\n",
            "1. Convert units\n",
            "2. Password generator\n",
            "3. Back to main menu\n"
        )
        try:
            choice = int(input("Enter a choice between 1-3: "))
        except (ValueError, EOFError, KeyboardInterrupt):
            print(Fore.RED + "Please enter an integer between 1-3.")
            continue

        if choice == 1:
            convert_units()
        elif choice == 2:
            password_generator()
        elif choice == 3:
            print("Returning to main menu...")
            try:
                import main
                main.run_app()
            except Exception:
                return
            return
        else:
            print(Fore.RED + "Invalid choice, try a number between 1-3.")
            Fore.RESET

if __name__ == "__main__":
    tool_menu()
