# 🔐 Secure Messaging Prototype (Flask + JWT + Encryption)

A secure messaging prototype API that demonstrates modern security practices including **JWT authentication**, **password hashing**, and **symmetric message encryption using Fernet (AES-128 CBC + HMAC)**.

This project simulates how a backend service could encrypt and decrypt user messages while ensuring authentication and controlled access. It is ideal for DevOps, Security, and Backend engineering portfolios.

---

## 🚀 Features

### 🔑 Authentication & Authorization
- User registration with **bcrypt password hashing**
- Login endpoint returning a **JWT access token**
- Protected routes using `@jwt_required` decorator

### 🛡️ Encryption Services
- Symmetric encryption using **Fernet**
- Ability to encrypt with:
  - A **default system key**, or
  - A **user-provided custom key**
- Secure decryption endpoint
- Validation for invalid or expired tokens

### 🗄️ SQLite Data Storage
- Lightweight database storing:
  - Users
  - Password hashes

---

## 📁 Project Structure

secure-messaging-prototype/
│── app/
│ ├── app.py # Flask app factory
│ ├── db.py # SQLite DB initialization
│ └── routes/
│ ├── auth.py # Login + registration + JWT
│ └── encrypt.py # Encryption / decryption API
│
│── secure_messages.db # SQLite database
│── run.py # Application entrypoint
│── requirements.txt
│── README.md

yaml
Copy code

---

## 🧪 API Usage

Use **Postman**, **Insomnia**, or **curl**.

---

### 1️⃣ Register a New User

**POST** `/register`

```json
{
  "username": "luther",
  "password": "mypassword"
}
2️⃣ Login to Get JWT Token
POST /login

Response Example:

json
Copy code
{
  "token": "eyJhbGciOiJIUzI1..."
}
You MUST include this token for encryption or decryption:

makefile
Copy code
Authorization: Bearer <your_token>
3️⃣ Encrypt a Message
POST /encrypt

json
Copy code
{
  "message": "Hello World"
}
Optional custom key:

json
Copy code
{
  "message": "Hello",
  "key": "xXxYourFernetKeyHerexXx"
}
4️⃣ Decrypt a Message
POST /decrypt

json
Copy code
{
  "token": "<encrypted_value_here>"
}
🧰 Installation & Setup
1. Clone the Repo
bash
Copy code
git clone https://github.com/lutherdpage/secure-messaging-prototype.git
cd secure-messaging-prototype
2. Create Virtual Environment
bash
Copy code
python -m venv .venv
.venv\Scripts\activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Initialize Database
Automatically runs when the app starts.

▶️ Run the App
bash
Copy code
python run.py
Server starts at:

cpp
Copy code
http://127.0.0.1:5000
