# Here we have other tools that can be useful.

import os
import json
import math
import colorama
from colorama import init, Fore, Style


def convert_units():  # Unit converter with submenus for different units
    print(
        "\n---Unit Converter---\n",
        "1. Length\n",
        "2. Weight\n",
        "3. Volume\n",
        "4. Temperature\n",
        "5. Back to tools menu\n"
    )
    choice = int(input("Enter a choice between 1-5: "))
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
        sub = int(input("Enter a choice between 1-6: "))
        if sub == 1:
            meters = float(input("Enter meters: "))
            print(f"{meters} meters = {meters / 1000} kilometers")
        elif sub == 2:
            km = float(input("Enter kilometers: "))
            print(f"{km} kilometers = {km * 1000} meters")
        elif sub == 3:
            cm = float(input("Enter centimeters: "))
            print(f"{cm} centimeters = {cm / 100} meters")
        elif sub == 4:
            meters = float(input("Enter meters: "))
            print(f"{meters} meters = {meters * 100} centimeters")
        elif sub == 5:
            inches = float(input("Enter inches: "))
            print(f"{inches} inches = {inches * 2.54} centimeters")
        elif sub == 6:
            cm = float(input("Enter centimeters: "))
            print(f"{cm} centimeters = {cm / 2.54} inches")
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
        sub = int(input("Enter a choice between 1-4: "))
        if sub == 1:
            g = float(input("Enter grams: "))
            print(f"{g} grams = {g / 1000} kilograms")
        elif sub == 2:
            kg = float(input("Enter kilograms: "))
            print(f"{kg} kilograms = {kg * 1000} grams")
        elif sub == 3:
            lbs = float(input("Enter pounds: "))
            print(f"{lbs} pounds = {lbs * 0.453592} kilograms")
        elif sub == 4:
            kg = float(input("Enter kilograms: "))
            print(f"{kg} kilograms = {kg * 2.20462} pounds")
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
        sub = int(input("Enter a choice between 1-4: "))
        if sub == 1:
            l = float(input("Enter liters: "))
            print(f"{l} liters = {l * 1000} milliliters")
        elif sub == 2:
            ml = float(input("Enter milliliters: "))
            print(f"{ml} milliliters = {ml / 1000} liters")
        elif sub == 3:
            gal = float(input("Enter gallons: "))
            print(f"{gal} gallons = {gal * 3.78541} liters")
        elif sub == 4:
            l = float(input("Enter liters: "))
            print(f"{l} liters = {l / 3.78541} gallons")
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
        sub = int(input("Enter a choice between 1-4: "))
        if sub == 1:
            c = float(input("Enter degrees Celsius: "))
            print(f"{c} °C = {c * 9 / 5 + 32} °F")
        elif sub == 2:
            f = float(input("Enter degrees Fahrenheit: "))
            print(f"{f} °F = {(f - 32) * 5 / 9} °C")
        elif sub == 3:
            c = float(input("Enter degrees Celsius: "))
            print(f"{c} °C = {c + 273.15} K")
        elif sub == 4:
            k = float(input("Enter Kelvin: "))
            print(f"{k} K = {k - 273.15} °C")
        else:
            print("Invalid choice, try a number between 1-4.")

    elif choice == 5:
        import main
    else:
        print("Invalid choice, try a number between 1-5.")


def password_generator():  # Password generator
    import random
    import string

    length = int(input("Enter desired password length (minimum 6 characters): "))
    if length < 6:
        print("Password length must be at least 6 characters.")
        return

    include_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_special = input("Include special characters? (y/n): ").lower() == 'y'

    if not (include_upper or include_lower or include_digits or include_special):
        print("You must select at least one character type.")
        return

    all_chars = ""
    if include_upper:
        all_chars += string.ascii_uppercase
    if include_lower:
        all_chars += string.ascii_lowercase
    if include_digits:
        all_chars += string.digits
    if include_special:
        all_chars += string.punctuation

    password = ''.join(random.choice(all_chars) for _ in range(length))
    print(f"Generated password: {password}")


while True:
    print(
        "\n---Tools Menu---\n",
        "1. Convert units\n",
        "2. Password generator\n",
        "3. Back to main menu\n"
    )
    choice = int(input("Enter a choice between 1-3: "))
    if choice == 1:
        convert_units()
    elif choice == 2:
        password_generator()
    elif choice == 3:
        print("Returning to main menu...")
        Fore.RESET
        import main
    else:
        print(Fore.RED + "Invalid choice, try a number between 1-3.")
        Fore.RESET
