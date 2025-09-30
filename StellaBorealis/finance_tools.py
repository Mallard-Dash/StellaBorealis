import colorama
import math
import json
import os
from colorama import init, Fore, Style

BASE_PATH = os.path.join(os.getcwd(), "Budget-")
os.makedirs(BASE_PATH, exist_ok=True)


def compound_interest():
    print(
        "Compound interest is a financial effect with great potential. "
        "The idea is that money growing with interest gets larger, "
        "and then the money + interest grows even bigger. It is often compared "
        "to a snowball rolling down a hill. At first, it is just a small snowball, "
        "but the further down the hill it rolls, the larger it becomes."
    )

    principal = int(input("Enter the starting capital: "))
    rate = float(input("Enter the interest rate in percent: "))
    years = int(input("Enter the number of years: "))

    final_amount = principal * (1 + rate / 100) ** years
    print(
        f"\nYou entered the following:\n"
        f"Starting capital = {principal} SEK\n"
        f"Interest rate = {rate} %\n"
        f"Years = {years}\n"
        f"Final amount = {final_amount:.2f} SEK\n"
    )
    return final_amount


def savings_goal():
    username = input("Enter your username: ")
    goal_name = input("Enter your savings goal (e.g., new car, trip, buffer): ")
    goal_amount = int(input("Enter your target amount: "))
    monthly_saving = int(input("Enter your monthly saving amount: "))

    with open(BASE_PATH + f"{username}_savings_goal.json", "a", encoding="utf-8") as f:
        f.write(json.dumps(f"Savings goal: {goal_name}", ensure_ascii=False) + "\n")
        f.write(json.dumps(f"Target amount: {goal_amount} SEK", ensure_ascii=False) + "\n")
        f.write(json.dumps(f"Monthly saving: {monthly_saving} SEK", ensure_ascii=False) + "\n")
        f.write(json.dumps(f"You will reach your goal in {goal_amount / monthly_saving:.1f} months", ensure_ascii=False) + "\n")
        f.write(json.dumps(f"That is approximately {goal_amount / monthly_saving / 12:.1f} years", ensure_ascii=False) + "\n")
        print(Fore.GREEN + "Savings goal created..")
        Fore.RESET


def calculator():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number (or write 0): "))
    opr = input("Choose an operation (+, -, *, /, x**y, root): ")

    if opr == "+":
        print("Answer: ", x + y)
    elif opr == "-":
        print("Answer: ", x - y)
    elif opr == "*":
        print("Answer: ", x * y)
    elif opr == "/":
        print("Answer: ", x / y)
    elif opr == "x**y":
        print("Answer: ", x ** y)
    elif opr == "root":
        print("Answer: ", math.sqrt(x))


while True:
    print(
        "\n***Finance Menu***\n"
        "1. Calculate compound interest\n"
        "2. Set a savings goal\n"
        "3. Open the calculator\n"
        "4. Back to main menu\n"
    )
    menu_choice = int(input("Enter a menu choice between 1-4: "))

    if menu_choice == 1:
        compound_interest()
    elif menu_choice == 2:
        savings_goal()
    elif menu_choice == 3:
        calculator()
    elif menu_choice == 4:
        import main
