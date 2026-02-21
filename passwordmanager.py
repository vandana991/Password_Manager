import sqlite3
import os
import string
import random
from cryptography.fernet import Fernet
from getpass import getpass

# ---------------- KEY MANAGEMENT ---------------- #

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

if not os.path.exists("secret.key"):
    generate_key()

key = load_key()
cipher = Fernet(key)

# ---------------- DATABASE ---------------- #

conn = sqlite3.connect("passwords.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS passwords (
    id INTEGER PRIMARY KEY,
    website TEXT,
    username TEXT,
    password BLOB
)
""")
conn.commit()

# ---------------- PASSWORD FUNCTIONS ---------------- #

def encrypt_password(password):
    return cipher.encrypt(password.encode())

def decrypt_password(password):
    return cipher.decrypt(password).decode()

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

# ---------------- FEATURES ---------------- #

def add_password():
    website = input("Website: ")
    username = input("Username: ")
    choice = input("Generate strong password? (y/n): ")

    if choice.lower() == "y":
        password = generate_password()
        print("Generated Password:", password)
    else:
        password = getpass("Enter password: ")

    encrypted = encrypt_password(password)

    cursor.execute(
        "INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)",
        (website, username, encrypted)
    )
    conn.commit()
    print("✅ Password saved successfully")

def view_password():
    website = input("Enter website name: ")

    cursor.execute("SELECT username, password FROM passwords WHERE website=?", (website,))
    result = cursor.fetchone()

    if result:
        username, encrypted_password = result
        print("Username:", username)
        print("Password:", decrypt_password(encrypted_password))
    else:
        print("❌ No password found")

# ---------------- MAIN MENU ---------------- #

def main():
    while True:
        print("\n Password Manager")
        print("1. Add new password")
        print("2. View password")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_password()
        elif choice == "3":
            print("Goodbye ")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()