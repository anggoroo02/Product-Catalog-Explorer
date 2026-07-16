### 1. Tema Website

**Product Catalog Explorer**

Website yang menampilkan katalog produk dari **FakeStore API**, dengan fitur login, favorit, dan catatan pribadi untuk setiap produk.

---

## 2. Tujuan Aplikasi

Membangun aplikasi web menggunakan Flask yang:

* Mengambil data produk dari Public API menggunakan `requests`
* Menampilkan data secara dinamis menggunakan Jinja2
* Memiliki sistem Authentication dan Authorization
* Menyimpan data pengguna secara lokal menggunakan SQLite
* Memungkinkan pengguna menyimpan produk favorit dan catatan pribadi

---

## 3. Teknologi

| Teknologi   | Fungsi             |
| ----------- | ------------------ |
| Python      | Bahasa pemrograman |
| Flask       | Web Framework      |
| SQLAlchemy  | ORM Database       |
| Flask-Login | Authentication     |
| Flask-WTF   | Form & Validation  |
| Requests    | Mengambil data API |
| SQLite      | Database           |
| Bootstrap 5 | Tampilan           |
| HTML/CSS/JS | Front-End          |

---

# 4. Arsitektur

```
Browser
      │
      ▼
 Flask Application
      │
 ├──────────────┐
 │ Blueprints   │
 ├──────────────┤
 │ Auth         │
 │ Dashboard    │
 │ Products     │
 │ Favorites    │
 │ Notes        │
 └──────────────┘
      │
      ├────────► FakeStore API
      │
      ▼
SQLite Database
```

Blueprint membuat setiap fitur memiliki route, template, dan logika yang terpisah sehingga kode lebih mudah dipelajari dan dirawat.

---

# 5. Fitur

## Guest

* Login
* Register
* Error Page

---

## User Login

* Dashboard
* Melihat Produk
* Detail Produk
* Tambah Favorite
* Hapus Favorite
* Menulis Note
* Edit Note
* Hapus Note
* Logout

---

# 6. Halaman

Sesuai requirement tugas.

```
/
│
├── Login
├── Register
├── Dashboard
├── Products
├── Product Detail
├── Favorites
├── Notes
├── Profile
├── 404
└── 500
```

---

# 7. Database

## users

```
id
username
email
password_hash
role
created_at
```

---

## favorites

```
id
user_id
product_id
created_at
```

`product_id` mengacu pada ID produk dari FakeStore API (tidak perlu tabel produk lokal).

---

## notes

```
id
user_id
product_id
title
content
created_at
updated_at
```

Setiap pengguna dapat memiliki catatan sendiri untuk produk tertentu.

---

# 8. Authorization

```
Guest
    │
    ▼
Login
    │
    ▼
Dashboard
    │
    ├── Products
    ├── Favorites
    └── Notes
```

Guest tidak dapat mengakses Dashboard, Favorites, maupun Notes.

---

# 9. Validasi

### Register

* Username wajib diisi
* Username unik
* Email valid
* Email unik
* Password minimal 8 karakter
* Konfirmasi password harus sama

---

### Login

* Username/email harus ada
* Password harus benar

---

### Notes

* Judul wajib diisi
* Isi catatan tidak boleh kosong

---

# 10. Error Handling

Minimal:

* 400 Bad Request
* 401 Unauthorized
* 403 Forbidden
* 404 Not Found
* 500 Internal Server Error
* API Timeout
* API Connection Error

---

# 11. Struktur Folder

```
product_catalog_explorer/
│
├── app/
│   ├── auth/
│   │   ├── routes.py
│   │   ├── forms.py
│   │   └── __init__.py
│   │
│   ├── dashboard/
│   │   ├── routes.py
│   │   └── __init__.py
│   │
│   ├── products/
│   │   ├── routes.py
│   │   ├── services.py
│   │   └── __init__.py
│   │
│   ├── favorites/
│   │   ├── routes.py
│   │   └── __init__.py
│   │
│   ├── notes/
│   │   ├── routes.py
│   │   ├── forms.py
│   │   └── __init__.py
│   │
│   ├── errors/
│   │   ├── handlers.py
│   │   └── __init__.py
│   │
│   ├── models.py
│   ├── extensions.py
│   ├── config.py
│   │
│   ├── templates/
│   ├── static/
│   └── __init__.py
│
├── instance/
│   └── database.db
│
├── requirements.txt
├── run.py
├── .gitignore
└── README.md
```

---

# 12. Alur Aplikasi

```
User
   │
   ▼
Register
   │
   ▼
Login
   │
   ▼
Dashboard
   │
   ▼
Products
   │
   ├──────────────► FakeStore API
   │
   ▼
Detail Produk
   │
   ├── Favorite
   └── Note
            │
            ▼
        SQLite
```

note: app ini dibuat untuk menyelesaikan tugas kuliah Pemrograman Back-End
