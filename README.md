# Password_Manager
## 🔐 Secure Password Manager (Python)

A simple and secure command-line Password Manager built using Python.
This application allows users to store and retrieve passwords securely using encryption.

# 🚀 Features

🔒 Encrypts passwords using Fernet symmetric encryption

🗄 Stores encrypted passwords in SQLite database

🔑 Auto-generates encryption key (secret.key)

🧠 Strong password generator

👤 Hidden password input using getpass

💾 Persistent local storage

# 🛠 Tech Stack

Python 3

SQLite3

Cryptography Library (Fernet)

OS Module

getpass Module

# 📦 Installation
## 1️⃣ Clone the repository
git clone https://github.com/yourusername/password-manager.git
cd password-manager
## 2️⃣ Install dependencies
pip install cryptography
## ▶️ How to Run
python passwordmanager.py

# 📋 Usage
## 🔹 Add New Password

Enter website name

Enter username

Choose to generate strong password OR enter manually

Password is encrypted before storing

## 🔹 View Password

Enter website name

Stored password is decrypted and displayed

# 🔐 How Security Works

A unique encryption key is generated and stored in secret.key

Passwords are encrypted using Fernet symmetric encryption

Only encrypted data is stored in passwords.db

Password input is hidden using getpass

# 📂 Project Structure
password-manager/
│
├── passwordmanager.py
├── passwords.db
├── secret.key
└── README.md

# ⚠️ Important Notes

Do NOT share your secret.key file.

If secret.key is lost, stored passwords cannot be decrypted.

This is a local password manager (no cloud sync).

# 💡 Future Improvements

Master password authentication

Argon2 / PBKDF2 key derivation

GUI version (Tkinter / PyQt)

Web version (FastAPI / Flask)

Auto-lock after inactivity

Password strength checker
