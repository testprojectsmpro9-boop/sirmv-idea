# MV Visvesvaraya Tribute & Ideathon

A Django web application honoring Sir M. Visvesvaraya and hosting the Visvesvaraya Ideathon platform.

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create MySQL database:
```sql
CREATE DATABASE visvesvaraya_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

4. Copy `.env.example` to `.env` and update with your database credentials:
```bash
cp .env.example .env
```

5. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create superuser:
```bash
python manage.py createsuperuser
```

7. Collect static files:
```bash
python manage.py collectstatic
```

8. Run the development server:
```bash
python manage.py runserver
```

Visit http://localhost:8000 to view the application.

## Features

- Home page with hero section and featured innovations
- About Sir MV page with timeline
- Ideathon page with idea gallery
- Idea submission form
- Contact page with contact form
- Collaboration page for partnerships
- Admin panel for managing submissions
