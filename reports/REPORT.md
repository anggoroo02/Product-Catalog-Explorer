# Product Catalog Explorer

## Pembuatan Aplikasi Back-End Menggunakan Flask dengan Data dari Public API (FakeStore API)

---

# 1. Latar Belakang

Perkembangan teknologi web mendorong banyak aplikasi untuk mengintegrasikan data dari berbagai layanan melalui Application Programming Interface (API). Dengan memanfaatkan API, sebuah aplikasi tidak perlu menyimpan seluruh data secara lokal, tetapi dapat mengambil informasi secara langsung dari layanan eksternal yang menyediakan data tersebut. Pendekatan ini membuat aplikasi menjadi lebih fleksibel, ringan, dan mudah dikembangkan.

Flask merupakan salah satu framework web berbasis Python yang banyak digunakan dalam pengembangan aplikasi back-end karena memiliki struktur yang sederhana, fleksibel, dan mudah dikembangkan menjadi aplikasi yang lebih kompleks. Selain itu, Flask menyediakan berbagai ekstensi yang mendukung implementasi autentikasi pengguna, validasi form, pengelolaan database, serta pengembangan aplikasi dengan arsitektur modular.

Pada proyek ini dikembangkan sebuah aplikasi web bernama **Product Catalog Explorer** yang memanfaatkan **FakeStore API** sebagai sumber data utama produk. Data produk tidak disimpan di database lokal, melainkan diambil secara dinamis menggunakan library **Requests** setiap kali diperlukan. Sementara itu, data yang berkaitan dengan pengguna seperti akun, daftar produk favorit, dan catatan pribadi disimpan pada database **SQLite** menggunakan **SQLAlchemy** sebagai Object Relational Mapper (ORM).

Aplikasi ini juga menerapkan konsep dasar pengembangan aplikasi back-end modern, seperti **Authentication**, **Authorization**, **Validation**, **Error Handling**, serta pemisahan tanggung jawab menggunakan **Blueprint** dan **Service Layer**. Dengan penerapan konsep tersebut, struktur kode menjadi lebih terorganisir, mudah dipelihara, serta lebih mudah dikembangkan pada masa mendatang.

---

# 2. Tujuan

Adapun tujuan dari pengembangan aplikasi **Product Catalog Explorer** adalah sebagai berikut:

1. Membangun aplikasi web berbasis Flask yang memanfaatkan data dari Public API.
2. Mengimplementasikan proses pengambilan data menggunakan library **Requests**.
3. Menampilkan data produk secara dinamis menggunakan template HTML Flask.
4. Mengimplementasikan sistem autentikasi pengguna berupa Register, Login, dan Logout.
5. Menerapkan sistem otorisasi sehingga setiap pengguna hanya dapat mengakses data miliknya sendiri.
6. Menyimpan data lokal berupa akun pengguna, daftar produk favorit, dan catatan produk menggunakan database SQLite.
7. Menerapkan validasi input dan penanganan kesalahan (error handling) agar aplikasi lebih aman dan stabil.
8. Menggunakan arsitektur modular berbasis Blueprint dan Service Layer untuk meningkatkan kualitas kode dan mempermudah proses pengembangan.

---

# 3. Teknologi yang Digunakan

Aplikasi dikembangkan menggunakan beberapa teknologi dan library yang saling terintegrasi untuk membangun sistem back-end maupun antarmuka web.

| Teknologi    | Fungsi                                                                      |
| ------------ | --------------------------------------------------------------------------- |
| Python       | Bahasa pemrograman utama aplikasi.                                          |
| Flask        | Framework web untuk membangun aplikasi back-end.                            |
| SQLAlchemy   | Object Relational Mapper (ORM) untuk mengelola database SQLite.             |
| Flask-Login  | Mengelola proses autentikasi pengguna dan sesi login.                       |
| Flask-WTF    | Membuat serta memvalidasi form pengguna.                                    |
| Requests     | Mengambil data produk dari FakeStore API.                                   |
| SQLite       | Database lokal untuk menyimpan data pengguna, favorit, dan catatan.         |
| Bootstrap 5  | Framework CSS untuk membangun antarmuka yang responsif dan mudah digunakan. |
| Jinja2       | Template engine yang digunakan Flask untuk menampilkan data secara dinamis. |
| HTML5 & CSS3 | Membangun struktur dan tampilan halaman web.                                |

---

# 4. Public API yang Digunakan

Aplikasi menggunakan **FakeStore API** sebagai sumber data utama katalog produk. FakeStore API merupakan layanan REST API publik yang menyediakan data produk fiktif lengkap dengan gambar, harga, kategori, deskripsi, serta informasi rating.

Seluruh data produk ditampilkan secara dinamis melalui proses permintaan HTTP menggunakan library **Requests**. Data yang diterima dari API dikonversi ke format **JSON**, kemudian diproses oleh service layer sebelum diteruskan ke template Flask untuk ditampilkan kepada pengguna.

Endpoint yang digunakan pada aplikasi antara lain:

| Endpoint                            | Fungsi                                          |
| ----------------------------------- | ----------------------------------------------- |
| `GET /products`                     | Mengambil seluruh daftar produk.                |
| `GET /products/{id}`                | Mengambil detail sebuah produk berdasarkan ID.  |
| `GET /products/categories`          | Mengambil daftar kategori produk.               |
| `GET /products/category/{category}` | Mengambil produk berdasarkan kategori tertentu. |

Perlu diperhatikan bahwa aplikasi **tidak menyimpan data produk ke dalam database lokal**. Database SQLite hanya digunakan untuk menyimpan data yang berkaitan dengan pengguna, yaitu akun, daftar favorit, dan catatan pribadi. Pendekatan ini menjaga agar data produk selalu mengikuti informasi terbaru yang disediakan oleh FakeStore API tanpa perlu melakukan sinkronisasi database.

# 5. Arsitektur Aplikasi

Aplikasi **Product Catalog Explorer** dikembangkan menggunakan **Application Factory Pattern** dan **Blueprint** yang disediakan oleh Flask. Pendekatan ini membuat setiap fitur dipisahkan ke dalam modul tersendiri sehingga kode lebih terorganisir, mudah dipelajari, dan mudah dikembangkan.

Selain menggunakan Blueprint, aplikasi juga menerapkan **Service Layer** untuk memisahkan logika bisnis dari route Flask. Route hanya bertugas menerima request, memanggil service yang sesuai, kemudian mengirimkan hasilnya ke template HTML. Dengan demikian, akses database maupun pemanggilan API tidak dilakukan secara langsung di dalam route.

Alur kerja aplikasi secara umum dapat digambarkan sebagai berikut:

```text
+----------------------+
|      Web Browser     |
+----------+-----------+
           |
           | HTTP Request
           v
+----------------------+
|   Flask Application  |
+----------+-----------+
           |
           v
+----------------------+
|      Blueprint       |
|----------------------|
| Auth                 |
| Dashboard            |
| Products             |
| Favorites            |
| Notes                |
+----------+-----------+
           |
           v
+----------------------+
|    Service Layer     |
+----------+-----------+
           |
   +-------+--------+
   |                |
   v                v
SQLite Database   FakeStore API
```

Pemisahan tanggung jawab tersebut memberikan beberapa keuntungan, antara lain:

* Struktur kode menjadi lebih rapi.
* Logika bisnis dapat digunakan kembali oleh beberapa route.
* Mempermudah proses pengujian dan pemeliharaan aplikasi.
* Memudahkan pengembangan fitur baru tanpa memengaruhi modul lain.

---

# 6. Struktur Project

Project disusun menggunakan struktur folder modular agar setiap komponen aplikasi memiliki tanggung jawab yang jelas.

```text
product_catalog_explorer/
│
├── app/
│   ├── auth/
│   ├── dashboard/
│   ├── favorites/
│   ├── notes/
│   ├── products/
│   ├── services/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── extensions.py
│   └── models.py
│
├── instance/
├── migrations/
│
├── .env
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

Penjelasan setiap folder:

| Folder/File     | Fungsi                                                           |
| --------------- | ---------------------------------------------------------------- |
| `app/auth`      | Modul autentikasi pengguna (Register, Login, Logout).            |
| `app/dashboard` | Halaman utama setelah pengguna berhasil login.                   |
| `app/products`  | Menampilkan daftar produk dan detail produk dari FakeStore API.  |
| `app/favorites` | Mengelola daftar produk favorit milik pengguna.                  |
| `app/notes`     | Mengelola CRUD catatan pribadi untuk setiap produk.              |
| `app/services`  | Berisi business logic dan akses database maupun API.             |
| `app/templates` | Template HTML menggunakan Jinja2.                                |
| `app/static`    | Menyimpan file CSS, JavaScript, dan aset statis lainnya.         |
| `models.py`     | Mendefinisikan model database menggunakan SQLAlchemy.            |
| `extensions.py` | Inisialisasi extension Flask seperti SQLAlchemy dan Flask-Login. |
| `config.py`     | Konfigurasi aplikasi.                                            |
| `instance/`     | Menyimpan database SQLite.                                       |
| `migrations/`   | Menyimpan riwayat migrasi database menggunakan Flask-Migrate.    |

---

# 7. Struktur Database

Aplikasi menggunakan database **SQLite** untuk menyimpan seluruh data lokal yang berkaitan dengan pengguna. Data produk tidak disimpan pada database karena seluruh informasi produk diperoleh secara langsung dari FakeStore API.

Database terdiri dari tiga tabel utama, yaitu:

* Users
* Favorites
* Notes

Hubungan antar tabel dapat digambarkan sebagai berikut:

```text
                 +------------------+
                 |      Users       |
                 +------------------+
                 | id               |
                 | username         |
                 | email            |
                 | password_hash    |
                 | role             |
                 | created_at       |
                 | updated_at       |
                 +---------+--------+
                           |
            +--------------+--------------+
            |                             |
            | 1                         1 |
            |                             |
            | *                           *
+-------------------------+     +-------------------------+
|       Favorites         |     |         Notes           |
+-------------------------+     +-------------------------+
| id                      |     | id                      |
| user_id (FK)            |     | user_id (FK)            |
| product_id              |     | product_id              |
| created_at              |     | title                   |
+-------------------------+     | content                 |
                                | created_at              |
                                | updated_at              |
                                +-------------------------+
```

### Tabel Users

Tabel **Users** menyimpan informasi akun pengguna yang digunakan untuk proses autentikasi.

| Field         | Keterangan                     |
| ------------- | ------------------------------ |
| id            | Primary Key                    |
| username      | Username unik pengguna         |
| email         | Email unik pengguna            |
| password_hash | Password yang telah dienkripsi |
| role          | Hak akses pengguna             |
| created_at    | Waktu pembuatan akun           |
| updated_at    | Waktu terakhir diperbarui      |

---

### Tabel Favorites

Tabel **Favorites** menyimpan daftar produk favorit yang dipilih oleh masing-masing pengguna.

| Field      | Keterangan                          |
| ---------- | ----------------------------------- |
| id         | Primary Key                         |
| user_id    | Foreign Key ke tabel Users          |
| product_id | ID produk dari FakeStore API        |
| created_at | Waktu produk ditambahkan ke favorit |

Setiap pengguna dapat memiliki banyak data favorit, sedangkan satu data favorit hanya dimiliki oleh satu pengguna.

---

### Tabel Notes

Tabel **Notes** digunakan untuk menyimpan catatan pribadi pengguna terhadap suatu produk.

| Field      | Keterangan                   |
| ---------- | ---------------------------- |
| id         | Primary Key                  |
| user_id    | Foreign Key ke tabel Users   |
| product_id | ID produk dari FakeStore API |
| title      | Judul catatan                |
| content    | Isi catatan                  |
| created_at | Waktu pembuatan catatan      |
| updated_at | Waktu terakhir diperbarui    |

Relasi ini memungkinkan setiap pengguna memiliki banyak catatan pada berbagai produk tanpa memengaruhi data pengguna lain. Validasi kepemilikan data dilakukan melalui service layer sehingga pengguna hanya dapat melihat, mengubah, dan menghapus catatan miliknya sendiri.

# 8. Authentication

Authentication merupakan mekanisme untuk memverifikasi identitas pengguna sebelum dapat mengakses fitur-fitur utama aplikasi. Pada **Product Catalog Explorer**, proses autentikasi diimplementasikan menggunakan ekstensi **Flask-Login**.

Aplikasi menyediakan tiga fitur autentikasi utama, yaitu:

* Register
* Login
* Logout

### Register

Pengguna baru dapat membuat akun dengan mengisi username, email, password, dan konfirmasi password. Setelah data berhasil divalidasi, password tidak disimpan dalam bentuk teks biasa (plain text), tetapi diubah menjadi hash menggunakan fungsi yang disediakan oleh Werkzeug sebelum disimpan ke database SQLite.

Tahapan proses registrasi adalah sebagai berikut:

```text
User
   │
   ▼
Register Form
   │
   ▼
Flask-WTF Validation
   │
   ▼
auth_service.register_user()
   │
   ▼
SQLAlchemy
   │
   ▼
SQLite
```

### Login

Pengguna dapat masuk menggunakan username atau email beserta password. Data yang dimasukkan akan diperiksa melalui `auth_service`, kemudian password diverifikasi dengan metode `check_password()`.

Apabila autentikasi berhasil, Flask-Login akan membuat sesi login sehingga pengguna dapat mengakses halaman yang memerlukan autentikasi.

### Logout

Logout dilakukan menggunakan fungsi `logout_user()` dari Flask-Login. Setelah logout, sesi pengguna akan dihapus dan pengguna harus login kembali untuk mengakses halaman yang dilindungi.

---

# 9. Authorization

Authorization merupakan mekanisme untuk menentukan hak akses pengguna terhadap suatu fitur atau data.

Pada aplikasi ini, seluruh halaman utama seperti Dashboard, Products, Favorites, dan Notes hanya dapat diakses oleh pengguna yang telah login melalui decorator:

```python
@login_required
```

Selain pembatasan akses halaman, aplikasi juga menerapkan pembatasan kepemilikan data.

Setiap pengguna hanya dapat mengakses data miliknya sendiri, antara lain:

* Daftar Favorite milik sendiri.
* Catatan (Notes) milik sendiri.
* Melakukan edit dan hapus hanya pada catatan yang dimiliki.

Validasi kepemilikan data dilakukan melalui **Service Layer**, sehingga Blueprint tidak melakukan akses database secara langsung. Pendekatan ini membuat logika bisnis lebih terpusat, mudah dipelihara, dan mengurangi kemungkinan pengguna mengakses data milik pengguna lain.

---

# 10. Validation

Aplikasi menerapkan validasi pada setiap proses input menggunakan **Flask-WTF**.

## Validasi Register

Pada halaman Register dilakukan beberapa validasi, antara lain:

* Username wajib diisi.
* Email wajib diisi.
* Format email harus valid.
* Password wajib diisi.
* Konfirmasi password harus sesuai.
* Username tidak boleh digunakan oleh pengguna lain.
* Email tidak boleh digunakan oleh pengguna lain.

Apabila terdapat kesalahan, aplikasi akan menampilkan pesan (flash message) sehingga pengguna dapat memperbaiki input yang diberikan.

---

## Validasi Login

Pada proses Login dilakukan validasi sebagai berikut:

* Username atau email wajib diisi.
* Password wajib diisi.
* Username/email dan password harus sesuai dengan data pada database.

Jika proses autentikasi gagal, pengguna akan memperoleh informasi bahwa username/email atau password yang dimasukkan tidak benar.

---

## Validasi Notes

Pada fitur Notes diterapkan validasi agar data yang disimpan memiliki informasi yang lengkap.

Validasi meliputi:

* Judul catatan wajib diisi.
* Isi catatan wajib diisi.
* Pengguna hanya dapat mengubah atau menghapus catatan miliknya sendiri.

Dengan adanya validasi tersebut, integritas data tetap terjaga dan mencegah penyimpanan data yang tidak lengkap.

---

# 11. Error Handling

Penanganan kesalahan (Error Handling) diterapkan untuk meningkatkan stabilitas aplikasi ketika terjadi kondisi yang tidak diharapkan.

## Error pada Public API

Seluruh komunikasi dengan FakeStore API dilakukan melalui `product_service`. Proses ini dilengkapi dengan penanganan berbagai kemungkinan kesalahan, antara lain:

* Timeout koneksi.
* Connection Error.
* HTTP Error.
* Request Exception.

Jika terjadi kesalahan saat mengambil data dari API, aplikasi tidak langsung berhenti, tetapi memberikan respons yang sesuai sehingga pengguna memperoleh informasi bahwa data tidak dapat dimuat.

---

## Error Halaman

Aplikasi menyediakan halaman kesalahan sederhana untuk kondisi seperti:

* Halaman tidak ditemukan (404 Not Found).
* Kesalahan internal aplikasi (500 Internal Server Error), apabila dikonfigurasi.

Dengan adanya halaman error khusus, pengguna memperoleh informasi yang lebih jelas dibandingkan pesan kesalahan bawaan dari framework.

---

## Flash Message

Selain halaman error, aplikasi juga menggunakan **Flash Message** untuk memberikan umpan balik kepada pengguna setelah melakukan suatu aksi.

Contoh penggunaan Flash Message antara lain:

* Registrasi berhasil.
* Login berhasil.
* Login gagal.
* Favorite berhasil ditambahkan.
* Favorite berhasil dihapus.
* Catatan berhasil ditambahkan.
* Catatan berhasil diperbarui.
* Catatan berhasil dihapus.

Flash Message membantu pengguna memahami hasil dari setiap tindakan yang dilakukan pada aplikasi.

---

# 12. Middleware

Pada proyek ini tidak digunakan middleware khusus seperti middleware logging, rate limiting, maupun middleware pihak ketiga.

Sebagai pengganti, aplikasi memanfaatkan mekanisme yang telah disediakan oleh Flask dan Flask-Login, antara lain:

* `@login_required` untuk membatasi akses halaman yang memerlukan autentikasi.
* Session Management dari Flask-Login untuk mengelola status login pengguna.
* Application Factory Pattern untuk menginisialisasi seluruh komponen aplikasi secara terpusat.

Pendekatan tersebut sudah memenuhi kebutuhan aplikasi sesuai ruang lingkup proyek serta menjaga struktur aplikasi tetap sederhana dan mudah dipahami.

# 13. Implementasi Fitur

Aplikasi **Product Catalog Explorer** dikembangkan secara bertahap menggunakan pendekatan modular. Setiap fitur dipisahkan ke dalam Blueprint dan didukung oleh Service Layer agar logika bisnis tidak bercampur dengan route Flask.

Berikut merupakan fitur-fitur utama yang telah diimplementasikan.

---

## 13.1 Authentication

Fitur autentikasi memungkinkan pengguna membuat akun dan masuk ke dalam aplikasi.

Fitur yang tersedia meliputi:

* Registrasi akun baru.
* Login menggunakan username atau email.
* Logout.
* Penyimpanan password dalam bentuk hash.
* Pengelolaan session menggunakan Flask-Login.

Seluruh proses autentikasi dipusatkan pada **auth_service**, sedangkan Blueprint hanya menangani request, response, dan tampilan.

---

## 13.2 Dashboard

Dashboard merupakan halaman utama setelah pengguna berhasil login.

Halaman ini berfungsi sebagai pusat navigasi menuju fitur-fitur utama aplikasi, yaitu:

* Products
* Favorites
* Notes

Dashboard juga menampilkan informasi pengguna yang sedang login sehingga pengguna mengetahui bahwa proses autentikasi berhasil dilakukan.

---

## 13.3 Product Catalog

Fitur Product Catalog mengambil data secara langsung dari **FakeStore API** menggunakan library **Requests**.

Fitur yang tersedia meliputi:

* Menampilkan seluruh produk.
* Menampilkan detail produk.
* Menampilkan kategori produk.
* Menampilkan produk berdasarkan kategori.

Seluruh komunikasi dengan API dipusatkan pada **product_service**, sehingga Blueprint tidak berhubungan langsung dengan proses HTTP Request.

---

## 13.4 Favorite

Fitur Favorite memungkinkan pengguna menyimpan produk yang dianggap menarik.

Fitur ini meliputi:

* Menambahkan produk ke daftar favorit.
* Menghapus produk dari daftar favorit.
* Menampilkan seluruh daftar favorit pengguna.

Data favorit disimpan pada database SQLite sehingga setiap pengguna memiliki daftar favorit yang berbeda.

Untuk menjaga konsistensi data, tabel Favorites menerapkan constraint unik sehingga satu produk tidak dapat disimpan lebih dari satu kali oleh pengguna yang sama.

---

## 13.5 Notes

Fitur Notes memungkinkan pengguna menyimpan catatan pribadi pada suatu produk.

Operasi yang tersedia meliputi:

* Create Note
* Read Note
* Update Note
* Delete Note

Setiap catatan memiliki hubungan dengan:

* User
* Product ID

Dengan demikian, satu pengguna dapat memiliki beberapa catatan pada berbagai produk.

Validasi kepemilikan dilakukan melalui **note_service**, sehingga pengguna hanya dapat mengubah maupun menghapus catatan miliknya sendiri.

---

# 14. Pengujian Aplikasi

Setelah seluruh fitur selesai diimplementasikan, dilakukan pengujian secara manual terhadap fungsi-fungsi utama aplikasi.

Hasil pengujian ditunjukkan pada tabel berikut.

| No | Fitur                       | Hasil    |
| -- | --------------------------- | -------- |
| 1  | Register User               | Berhasil |
| 2  | Login User                  | Berhasil |
| 3  | Logout User                 | Berhasil |
| 4  | Dashboard                   | Berhasil |
| 5  | Menampilkan Daftar Produk   | Berhasil |
| 6  | Detail Produk               | Berhasil |
| 7  | Menampilkan Kategori Produk | Berhasil |
| 8  | Menambah Favorite           | Berhasil |
| 9  | Menghapus Favorite          | Berhasil |
| 10 | Menampilkan Daftar Favorite | Berhasil |
| 11 | Menambah Note               | Berhasil |
| 12 | Mengubah Note               | Berhasil |
| 13 | Menghapus Note              | Berhasil |
| 14 | Menampilkan Daftar Note     | Berhasil |
| 15 | Halaman Error 404           | Berhasil |

Selain pengujian fungsional, dilakukan pula beberapa pengujian terhadap validasi dan keamanan aplikasi, antara lain:

* Pengguna yang belum login tidak dapat mengakses halaman yang dilindungi.
* Username dan email tidak dapat didaftarkan lebih dari satu kali.
* Password disimpan dalam bentuk hash.
* Pengguna hanya dapat mengakses data Favorite miliknya sendiri.
* Pengguna hanya dapat mengubah dan menghapus Note miliknya sendiri.
* Penanganan kesalahan pada proses komunikasi dengan FakeStore API berjalan dengan baik.

Berdasarkan hasil pengujian tersebut, seluruh fitur utama aplikasi dapat berjalan sesuai dengan kebutuhan yang telah ditentukan.

---

# 15. Kendala dan Solusi

Selama proses pengembangan aplikasi, terdapat beberapa kendala yang berhasil diselesaikan melalui proses refactor dan perbaikan struktur kode.

| Kendala                                                  | Solusi                                                                                                                              |
| -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Business Logic berada pada Blueprint.                    | Logika bisnis dipindahkan ke Service Layer sehingga Blueprint hanya menangani request dan response.                                 |
| Duplikasi fungsi `_request()` pada `product_service`.    | Fungsi dirapikan menjadi satu implementasi dengan error handling yang lebih lengkap.                                                |
| Integrasi Notes belum muncul pada halaman Detail Produk. | Halaman Product Detail diintegrasikan dengan `note_service` sehingga catatan pengguna dapat ditampilkan sesuai produk yang dipilih. |
| Potensi penyimpanan Favorite ganda.                      | Ditambahkan Unique Constraint pada kombinasi `user_id` dan `product_id`.                                                            |
| Struktur project semakin besar seiring penambahan fitur. | Aplikasi disusun menggunakan Blueprint agar setiap modul memiliki tanggung jawab yang jelas.                                        |

Proses perbaikan tersebut menghasilkan struktur aplikasi yang lebih modular, mudah dipelihara, dan lebih sesuai dengan praktik pengembangan aplikasi Flask.

---

# 16. Pengembangan Selanjutnya

Walaupun aplikasi telah memenuhi kebutuhan tugas, masih terdapat beberapa fitur yang dapat dikembangkan pada versi berikutnya.

Beberapa pengembangan yang dapat dilakukan antara lain:

* Menambahkan fitur pencarian (Search Product).
* Menambahkan Pagination pada daftar produk.
* Menambahkan filter dan pengurutan produk.
* Menambahkan Dashboard Admin.
* Menambahkan Unit Testing dan Integration Testing.
* Menggunakan Redis untuk caching data API.
* Menambahkan Docker agar proses deployment menjadi lebih mudah.
* Mengintegrasikan Continuous Integration (CI) menggunakan GitHub Actions.
* Mengimplementasikan Role-Based Access Control (RBAC) yang lebih lengkap.

Pengembangan tersebut diharapkan dapat meningkatkan performa, skalabilitas, serta kualitas aplikasi apabila digunakan pada lingkungan yang lebih luas.

---

# 17. Kesimpulan

Berdasarkan hasil implementasi dan pengujian yang telah dilakukan, dapat disimpulkan bahwa aplikasi **Product Catalog Explorer** berhasil dikembangkan menggunakan framework Flask dengan memanfaatkan **FakeStore API** sebagai sumber data utama produk.

Aplikasi telah memenuhi kebutuhan utama tugas, yaitu mengambil data dari Public API menggunakan library Requests, menampilkan data secara dinamis melalui template Flask, serta mengintegrasikan fitur back-end seperti Authentication, Authorization, Validation, dan Error Handling.

Penerapan Blueprint dan Service Layer menghasilkan struktur aplikasi yang lebih modular sehingga memudahkan proses pemeliharaan dan pengembangan di masa mendatang. Selain itu, penggunaan SQLite untuk menyimpan data pengguna, favorit, dan catatan memungkinkan aplikasi menggabungkan data eksternal dari API dengan data lokal secara efektif.

Secara keseluruhan, proyek ini memberikan pengalaman dalam membangun aplikasi web berbasis Flask yang mengintegrasikan layanan Public API dengan database lokal serta menerapkan praktik pengembangan perangkat lunak yang terstruktur.
