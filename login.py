# login.py — StellaBorealis login (simple + robust)

import os
import sqlite3
import getpass
from colorama import init, Fore, Style
from banner import show_banner

init(autoreset=True)

# -------------------- DB globals --------------------
_conn = None
_cur  = None

def init_db():
    """Open DB if needed and ensure schema exists."""
    global _conn, _cur
    if _conn is None:
        _conn = sqlite3.connect("users.db")
        _cur = _conn.cursor()
        _cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
        """)
        _conn.commit()

def close_db():
    """Close DB connection if open."""
    global _conn
    if _conn is not None:
        _conn.close()
        _conn = None

# -------------------- Validation --------------------
def check_username(user: str):
    user = (user or "").strip()
    if not user: return False, "Username cannot be empty."
    if len(user) < 4: return False, "Username must be at least 4 characters."
    if any(ch.isspace() for ch in user): return False, "Username cannot contain spaces."
    if len(user) > 25: return False, "Username max length is 25."
    return True, ""

def check_password(pw: str):
    if not pw: return False, "Password cannot be empty."
    if any(ch.isspace() for ch in pw): return False, "Password cannot contain spaces."
    if not (4 <= len(pw) <= 25): return False, "Password must be 4-25 characters."
    return True, ""

# -------------------- Actions --------------------
def new_user():
    """Interactive account creation. Loops until success or Ctrl+C."""
    init_db()
    while True:
        try:
            user = input("Choose username (4-25 chars): ").strip()
            ok, msg = check_username(user)
            if not ok:
                print(Fore.RED + msg); continue

            pw = getpass.getpass("Choose a password (4-25 chars): ")
            ok, msg = check_password(pw)
            if not ok:
                print(Fore.RED + msg); continue

            pw2 = getpass.getpass("Repeat password: ")
            if pw != pw2:
                print(Fore.RED + "Passwords do not match."); continue

            try:
                _cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user, pw))
                _conn.commit()
                print(Fore.GREEN + "User created!")
                return True
            except sqlite3.IntegrityError:
                print(Fore.YELLOW + "That username is taken. Try another.")
        except KeyboardInterrupt:
            print("\nCancelled by user.")
            return False

def login():
    """Interactive login. Returns True on success, False on failure."""
    init_db()
    user = input("Username: ")
    pw   = getpass.getpass("Password: ")
    _cur.execute("SELECT 1 FROM users WHERE username=? AND password=?", (user, pw))
    if _cur.fetchone():
        print(Fore.GREEN + "Logged in!")
        return True
    else:
        print(Fore.RED + "Wrong username and/or password.")
        return False

# -------------------- Menu --------------------
def login_menu():
    """Show the login menu. Returns True if user logged in, False to exit."""
    while True:
        print(Style.BRIGHT + "*** WELCOME ***")
        print("1. Log in")
        print("2. Create account")
        print("3. Exit")
        choice = input("Enter 1-3: ").strip()

        if choice == "1":
            if login():
                return True
        elif choice == "2":
            new_user()  # stays in menu afterwards
        elif choice == "3":
            print(Fore.BLUE + "Bye!"); return False
        else:
            print(Fore.RED + "Please enter 1, 2, or 3.")

# -------------------- Entry point --------------------
def main():
    """Show banner then run the login menu; return True if logged in."""
    show_banner(animate=True, twinkle_frames=20, fps=9)
    return login_menu()

if __name__ == "__main__":
    try:
        ok = main()
        # If you want to jump into main app when running login.py directly:
        if ok:
            try:
                import main as app_main
                app_main.main()
            except Exception:
                pass
    finally:
        close_db()
