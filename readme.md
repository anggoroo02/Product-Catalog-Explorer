# Product Catalog Explorer

A web-based product catalog application built with Flask that consumes the FakeStore API. Users can browse products, manage favorites, and create personal notes after authentication.

---

## Features

- User Authentication (Register, Login, Logout)
- Browse Products from FakeStore API
- Product Detail
- Favorite Products
- Personal Product Notes
- Dashboard
- Error Handling
- Form Validation

---

## Tech Stack

Backend

- Python
- Flask
- SQLAlchemy
- Flask-Login
- Flask-WTF
- Requests

Database

- SQLite

Frontend

- HTML
- Bootstrap 5

External API

- FakeStore API

---

## Architecture

The project follows a modular Flask architecture using:

- Application Factory Pattern
- Blueprint
- Service Layer

Modules:

- Authentication
- Dashboard
- Products
- Favorites
- Notes

---

## Project Structure

```text
app/
├── auth/
├── dashboard/
├── favorites/
├── notes/
├── products/
├── services/
├── static/
├── templates/
├── __init__.py
├── extensions.py
└── models.py

instance/
migrations/

config.py
run.py
requirements.txt
```

---

## Database Schema

Users

- id
- username
- email
- password_hash
- role

Favorites

- id
- user_id
- product_id

Notes

- id
- user_id
- product_id
- title
- content

---

## Public API

FakeStore API

Used endpoints:

- GET /products
- GET /products/{id}
- GET /products/categories
- GET /products/category/{category}

---

## Installation

### Clone repository

```bash
git clone <repository-url>
cd product_catalog_explorer
```

### Create virtual environment

```bash
python -m venv .venv
```

### Activate virtual environment

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file:

```env
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///instance/app.db
FAKESTORE_API_BASE_URL=https://fakestoreapi.com
REQUEST_TIMEOUT=10
```

---

## Run Application

```bash
python run.py
```

Open:

```
http://127.0.0.1:5000
```

---

## Usage

1. Register
2. Login
3. Browse products
4. View product detail
5. Add favorite
6. Create personal notes

---

## Error Handling

- HTTP request exceptions
- Authentication validation
- Form validation
- 404 page
- 500 page

---

## Future Improvements

- Search products
- Pagination
- Admin dashboard
- Product caching
- Unit testing

---

## License

This project was developed for educational purposes.