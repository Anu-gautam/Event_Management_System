# Event Management System

A Django-based web application for managing event vendor operations, user orders, and admin-level membership/transaction tracking.

## Project Summary (Recruiter-Friendly)

This project demonstrates a full-stack Django application with:
- **Role-based modules** for vendors, users, and administrators
- **Data modeling** for shops, items, orders, memberships, and transactions
- **Server-rendered UI** using Django templates
- **Production-ready basics** such as environment-based configuration and static file middleware

It reflects practical backend development skills in Python, Django, relational data design, and multi-module app structure.

## Core Features

- Vendor onboarding and dashboard
- Vendor item creation and listing
- User dashboard with order history
- Add-to-cart flow (order creation)
- Admin dashboard for memberships and transactions
- Django admin support

## Tech Stack

- **Backend:** Python, Django 5
- **Database (default):** SQLite3
- **Frontend:** Django Templates (HTML)
- **Static file handling:** WhiteNoise

## Repository Structure

```text
Event_Management_System/
├── README.md
└── EventManagementSystem/
    ├── manage.py
    ├── requirements.txt
    ├── db.sqlite3
    ├── EventManagementSystem/   # project settings/urls
    ├── vendors/                 # vendor module
    ├── user/                    # user module
    └── admin_dashboard/         # admin module
```

## How to Run Locally

### 1) Clone and go to the Django project folder

```bash
git clone <your-repo-url>
cd Event_Management_System/EventManagementSystem
```

### 2) Create and activate a virtual environment

**Linux/macOS**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell)**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Apply migrations

```bash
python manage.py migrate
```

### 5) Start development server

```bash
python manage.py runserver
```

Open: `http://127.0.0.1:8000/`

## Useful Routes

- `/` or `/vendor/` → Vendor dashboard
- `/vendor/add_item/` → Add item
- `/vendor/create_vendor/` → Create vendor profile
- `/user/` → User dashboard
- `/admin_dashboard/` → Admin dashboard
- `/admin/` → Django admin panel

## Environment Notes

- `SECRET_KEY` is read from environment variable (fallback exists for development only).
- **Production requirement:** always set a strong `SECRET_KEY` via environment variable and do not rely on fallback values.
- `DEBUG` can be controlled with environment variable (`False` disables debug mode).

## Validation Commands

```bash
python manage.py check
python manage.py test
```
