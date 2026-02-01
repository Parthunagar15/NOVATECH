
# NovaTech — Django Web Application

A full-stack dynamic website built with **Django + SQLite**, featuring authentication, signup with validation, and a contact form that persists messages to the database.

---

## 📁 Project Structure

```
novatech/
├── manage.py                  ← Django CLI entry point
├── setup.sh                   ← One-command setup & run script
├── requirements.txt           ← Python dependencies (Django)
│
├── novatech/                  ← Project package
│   ├── settings.py            ← All Django settings (SQLite, apps, static)
│   ├── urls.py                ← Root URL dispatcher
│   └── wsgi.py                ← WSGI entry (production)
│
├── core/                      ← Main application
│   ├── models.py              ← ContactMessage model (saved to SQLite)
│   ├── forms.py               ← SignupForm + ContactForm with full validation
│   ├── views.py               ← All page views (login, signup, home, about, contact)
│   ├── urls.py                ← App-level URL routes
│   ├── admin.py               ← Registers ContactMessage in Django Admin
│   └── migrations/
│       └── 0001_initial.py    ← Creates the ContactMessage table
│
├── templates/                 ← HTML templates (Django template engine)
│   ├── base.html              ← Shared layout: navbar, toast, blocks
│   ├── login.html             ← Login page
│   ├── signup.html            ← Signup page (with strength meter)
│   ├── home.html              ← Home / Hero page
│   ├── about.html             ← About Us page
│   └── contact.html           ← Contact page (form + success overlay)
│
├── static/
│   ├── css/
│   │   └── style.css          ← Full stylesheet (dark theme, responsive)
│   └── js/
│       └── main.js            ← Navbar scroll, toast, password toggle & strength
│
└── db.sqlite3                 ← SQLite database (created on first migrate)
```

---

## 🚀 Quick Start

### Option A — Automatic (recommended)
```bash
bash setup.sh
```
This creates a virtual environment, installs Django, runs migrations, and starts the server.

### Option B — Manual
```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open **http://127.0.0.1:8000** in your browser.

---

## 🗺 Routes

| URL            | Page         | Auth Required |
|----------------|--------------|---------------|
| `/login/`      | Login        | No            |
| `/signup/`     | Sign Up      | No            |
| `/`            | Home         | ✓ Yes         |
| `/about/`      | About Us     | ✓ Yes         |
| `/contact/`    | Contact Us   | ✓ Yes         |
| `/logout/`     | Logout       | ✓ Yes         |
| `/admin/`      | Django Admin | ✓ Superuser   |

---

## ✅ Feature Checklist

- **Login** — email + password authentication, toggle visibility, credential error handling
- **Signup** — name, email, password, confirm password; duplicate-email check; live password strength meter (Weak / Fair / Strong); per-field inline errors
- **Home** — personalized hero greeting, animated badge, four feature cards
- **About** — story + mission sections, stats row, responsive team grid
- **Contact** — two-column layout with info cards; validated form (all fields required, email format, message min-length); messages saved to SQLite; success overlay with "Send Another" reset
- **Auth guards** — unauthenticated users are redirected to `/login/`
- **Toast notifications** — success / error / info messages appear at the bottom of the screen
- **Responsive** — full mobile layout at ≤ 700 px
- **Django Admin** — view all contact messages at `/admin/` (create a superuser during setup)
