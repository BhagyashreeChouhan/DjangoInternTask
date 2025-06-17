# Django Internship Assignment Project

This project demonstrates a backend application built with **Django Rest Framework**, featuring **authentication using DRF's ObtainAuthToken**, **Celery with Redis**, and **Telegram bot integration**. It's structured for production-readiness and clean code management.

---

## 🚀 Features

- RESTful API with DRF (Django Rest Framework)
- Token-based authentication using DRF's ObtainAuthToken (via `/api/login/`)
- Celery task for background job (e.g., email sending)
- Telegram bot integration to collect usernames
- Environment variable-based configuration
- Secure Django settings for production
- Clean Git history and well-documented code

---

## 📁 Project Setup

### 1. Clone the repository

```bash
git clone https://github.com/BhagyashreeChouhan/DjangoInternTask.git
cd DjangoInternTask
```

### 2. Create and activate a virtual environment

#### On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### On Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory and add the following variables:

```env
DEBUG=False
SECRET_KEY=your_django_secret_key
ALLOWED_HOSTS=localhost,127.0.0.1

DATABASE_URL=postgres://user:password@localhost:5432/dbname

EMAIL_HOST=smtp.yourprovider.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_email_password
EMAIL_USE_TLS=True

TELEGRAM_BOT_TOKEN=your_telegram_bot_token
```

> You can use packages like `python-dotenv` to manage these in your code.

---

## 🧪 Running the Project Locally

### 1. Apply Migrations

```bash
python manage.py migrate
```

### 2. Create a Superuser (for admin access)

```bash
python manage.py createsuperuser
```

### 3. Run Django Server

```bash
python manage.py runserver
```

### 4. Run Celery Worker

```bash
celery -A DjangoInternTask worker -P solo -l info
```

### 5. Run Telegram Bot

```bash
python telegram_bot.py
```

---

## 🔐 Authentication

Uses **Token-based authentication** with DRF's `ObtainAuthToken`.

### Obtain Token via Login Endpoint

```http
POST /api/login/
Content-Type: application/json

{
  "username": "your_username",
  "password": "your_password"
}
```

### Use token in headers

```http
Authorization: Token your_token
```

---

## 📡 API Endpoints

| Endpoint            | Method | Access        | Description                  |
|---------------------|--------|---------------|------------------------------|
| `/api/public/`      | GET    | Public        | Public endpoint (no auth)    |
| `/api/protected/`   | GET    | Authenticated | Requires Token               |
| `/api/register/`    | POST   | Public        | Register a new user          |
| `/api/login/`       | POST   | Public        | Obtain token with credentials |

---

## 📬 Background Tasks (Celery)

When a user registers, a welcome email is sent asynchronously using Celery and Redis.

Make sure Redis is running locally:

```bash
redis-server.exe (on Windows)
```

---

## 🤖 Telegram Bot Integration

Users can start the bot by messaging `/start` to your bot.

The bot collects their Telegram username and stores it in the Django database.

---

## ✅ Code Quality & Structure

- Modular Django app structure
- Environment-safe settings
- Git-based version control with proper commit history
- Clean and readable code with comments

---

## 📞 Contact

For any questions or issues, please contact:

**Bhagyashree Chouhan** – chouhanbhagyashree123@gmail.com
