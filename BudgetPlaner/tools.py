#Här har vi övriga verktyg som kan vara bra att ha.

import os
import json
import math
import colorama 
from colorama import init, Fore, Style

def konvertera_enheter(): #Enhetskonverterare med flera menyer för de olika enheterna
    print("\n---Enhetskonverterare---\n",
          "1. Längd\n",
          "2. Vikt\n",
          "3. Volym\n",
          "4. Temperatur\n",
          "5. Tillbaka till verktygsmenyn\n")
    val=int(input("Ange ett menyval mellan 1-5: "))
    if val==1:
        print("\n---Längd---\n",
              "1. Meter till Kilometer\n",
              "2. Kilometer till Meter\n",
              "3. Centimeter till Meter\n",
              "4. Meter till Centimeter\n",
              "5. Tum till Centimeter\n",
              "6. Centimeter till Tum\n")
        val=int(input("Ange ett menyval mellan 1-6: "))
        if val==1:
            meter=float(input("Ange meter: "))
            print(f"{meter} meter är {meter/1000} kilometer")
        elif val==2:
            kilometer=float(input("Ange kilometer: "))
            print(f"{kilometer} kilometer är {kilometer*1000} meter")
        elif val==3:
            centimeter=float(input("Ange centimeter: "))
            print(f"{centimeter} centimeter är {centimeter/100} meter")
        elif val==4:
            meter=float(input("Ange meter: "))
            print(f"{meter} meter är {meter*100} centimeter")
        elif val==5:
            tum=float(input("Ange tum: "))
            print(f"{tum} tum är {tum*2.54} centimeter")
        elif val==6:
            centimeter=float(input("Ange centimeter: "))
            print(f"{centimeter} centimeter är {centimeter/2.54} tum")
        else:
            print("Felaktigt val, försök med en siffra mellan 1-6.")
    elif val==2:
        print("\n---Vikt---\n",
              "1. Gram till Kilogram\n",
              "2. Kilogram till Gram\n",
              "3. Pund till Kilogram\n",
              "4. Kilogram till Pund\n")
        val=int(input("Ange ett menyval mellan 1-4: "))
        if val==1:
            gram=float(input("Ange gram: "))
            print(f"{gram} gram är {gram/1000} kilogram")
        elif val==2:
            kilogram=float(input("Ange kilogram: "))
            print(f"{kilogram} kilogram är {kilogram*1000} gram")
        elif val==3:
            pund=float(input("Ange pund: "))
            print(f"{pund} pund är {pund*0.453592} kilogram")
        elif val==4:
            kilogram=float(input("Ange kilogram: "))
            print(f"{kilogram} kilogram är {kilogram*2.20462} pund")
        else:
            print("Felaktigt val, försök med en siffra mellan 1-4.")
    elif val==3:
        print("\n---Volym---\n",
              "1. Liter till Milliliter\n",
              "2. Milliliter till Liter\n",
              "3. Gallon till Liter\n",
              "4. Liter till Gallon\n")
        val=int(input("Ange ett menyval mellan 1-4: "))
        if val==1:
            liter=float(input("Ange liter: "))
            print(f"{liter} liter är {liter*1000} milliliter")
        elif val==2:
            milliliter=float(input("Ange milliliter: "))
            print(f"{milliliter} milliliter är {milliliter/1000} liter")
        elif val==3:
            gallon=float(input("Ange gallon: "))
            print(f"{gallon} gallon är {gallon*3.78541} liter")
        elif val==4:
            liter=float(input("Ange liter: "))
            print(f"{liter} liter är {liter/3.78541} gallon")
        else:
            print("Felaktigt val, försök med en siffra mellan 1-4.")
    elif val==4:
        print("\n---Temperatur---\n",
              "1. Celsius till Fahrenheit\n",
              "2. Fahrenheit till Celsius\n",
              "3. Celsius till Kelvin\n",
              "4. Kelvin till Celsius\n")
        val=int(input("Ange ett menyval mellan 1-4: "))
        if val==1:
            celsius=float(input("Ange grader Celsius: "))
            print(f"{celsius} grader Celsius är {celsius*9/5 + 32} grader Fahrenheit")
        elif val==2:
            fahrenheit=float(input("Ange grader Fahrenheit: "))
            print(f"{fahrenheit} grader Fahrenheit är {(fahrenheit - 32) * 5/9} grader Celsius")
        elif val==3:
            celsius=float(input("Ange grader Celsius: "))
            print(f"{celsius} grader Celsius är {celsius + 273.15} Kelvin")
        elif val==4:
            kelvin=float(input("Ange Kelvin: "))
            print(f"{kelvin} Kelvin är {kelvin - 273.15} grader Celsius")
        else:
            print("Felaktigt val, försök med en siffra mellan 1-4.")
    elif val==5:
        import main
    else:
        print("Felaktigt val, försök med en siffra mellan 1-5.")

def password_generator():  #Lösenordsgenerator
    import random
    import string

    length = int(input("Ange önskad längd på lösenordet (minst 6 tecken): "))
    if length < 6:
        print("Lösenordslängden måste vara minst 6 tecken.")
        return

    include_upper = input("Inkludera stora bokstäver? (j/n): ").lower() == 'j'
    include_lower = input("Inkludera små bokstäver? (j/n): ").lower() == 'j'
    include_digits = input("Inkludera siffror? (j/n): ").lower() == 'j'
    include_special = input("Inkludera specialtecken? (j/n): ").lower() == 'j'

    if not (include_upper or include_lower or include_digits or include_special):
        print("Du måste välja minst en teckentyp att inkludera.")
        return

    all_characters = ""
    if include_upper:
        all_characters += string.ascii_uppercase
    if include_lower:
        all_characters += string.ascii_lowercase
    if include_digits:
        all_characters += string.digits
    if include_special:
        all_characters += string.punctuation

    password = ''.join(random.choice(all_characters) for _ in range(length))
    print(f"Genererat lösenord: {password}")

while True:
    print("\n---Verktygsmeny---\n",
          "1. Konvertera enheter\n",
          "2. Lösenordsgenerator\n",
          "3. Tillbaka till huvudmenyn\n")
    val=int(input("Ange ett menyval mellan 1-3: "))
    if val==1:
        konvertera_enheter()
    elif val==2:
        password_generator()   
    elif val==3:
        print("Återvänder till huvudmenyn...")
        Fore.RESET
        import main
    else:
        print(Fore.RED + ("Felaktigt val, försök med en siffra mellan 1-3."))
        Fore.RESET    