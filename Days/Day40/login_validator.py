import json
import hashlib
import os

DB_FILE = "users.json"


# ---------- Helpers ----------

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def load_users():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        return json.load(f)


def save_users(users):
    with open(DB_FILE, "w") as f:
        json.dump(users, f, indent=4)


# ---------- Core Logic ----------

def register():
    users = load_users()

    username = input("Choose username: ").strip()
    if username in users:
        print("User already exists.")
        return

    password = input("Choose password: ").strip()
    users[username] = hash_password(password)

    save_users(users)
    print("Registration successful.")


def login():
    users = load_users()

    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username not in users:
        print("User not found.")
        return

    if users[username] == hash_password(password):
        print("Login successful.")
    else:
        print("Wrong password.")


# ---------- App Loop ----------

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Select: ").strip()

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid option.")
