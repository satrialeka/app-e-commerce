1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)

1.Buat proyek Django baru.
2.Buat direktori baru bernama app-e-commerce sebagai local directory.
3.Buat repository GitHub baru bernama app-e-commerce.
4.Buat dan edit file README.md menggunakan VSCode.
5.Inisialisasi Git di app-e-commerce 
6.git init, git branch -M main, git remote add origin (link git kita), git push -u origin main.
7.Buat virtual environment dengan python -m venv env dan aktifkan dengan source env/bin/activate.
8.Buat requirements.txt dan isi dengan dependencies yang diperlukan, lalu install dengan pip install -r requirements.txt.
9.Inisialisasi proyek Django dengan django-admin startproject app-e-commerce
10.Edit settings.py: ubah ALLOWED_HOSTS = [] menjadi ALLOWED_HOSTS = ["localhost", "127.0.0.1"].
11.Buat file .gitignore untuk mengabaikan file yang tidak perlu ditrack Git.
12.Buat aplikasi Django baru bernama main dengan python manage.py startapp main.
13.Tambahkan 'main' ke INSTALLED_APPS di settings.py.
14.Buat folder templates di dalam direktori main untuk menyimpan file main.html.
15.Buat file main.html dengan konten yang diperlukan.
16.Atur routing URL dengan mengedit urls.py di app-e-commerce
17.Buat model Item di models.py
18.Edit views.py untuk menghubungkan Views dan Templates
19.Edit urls.py di main
20.update repository 

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

Client -> Internet -> Python/Django -> urls.py -> views.py (proses URL) -> models.py (read/write data) -> Database -> templates (input/display data) -> Return HTML (merge dengan value) -> Internet -> device client.

3. Jelaskan fungsi git dalam pengembangan perangkat lunak!

-Pengelolaan Perubahan Kode: Git mencatat setiap perubahan kode yang dilakukan oleh pengembang, memungkinkan mereka melacak versi sebelumnya, mengetahui siapa yang membuat perubahan, dan memahami alasan di balik perubahan tersebut.

-Kerja Sama Tim: Git memfasilitasi kolaborasi antar anggota tim dengan memungkinkan mereka bekerja secara terpisah pada cabang (branch) masing-masing tanpa mengganggu pekerjaan satu sama lain. Setelah pengembangan atau perbaikan selesai, cabang ini dapat digabung kembali ke kode utama.

-pemulihan dan Penyelesaian Konflik: Git memungkinkan pengembang untuk kembali ke versi kode yang stabil jika terjadi kesalahan, serta membantu menyelesaikan konflik saat beberapa orang mengedit bagian kode yang sama.

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

- Django sering dipilih sebagai framework pertama dalam pembelajaran pengembangan perangkat lunak karena memiliki beberapa keunggulan yang membuatnya cocok untuk pemula. Pertama, Django sudah dilengkapi dengan banyak fitur bawaan, seperti autentikasi pengguna, manajemen database, dan URL routing, sehingga kita tidak perlu membangun semuanya dari nol. Ini membantu pengembang baru untuk lebih fokus pada logika aplikasi daripada hal-hal teknis yang rumit.

- Selain itu, Django mengikuti prinsip "batteries included", yang berarti banyak kebutuhan pengembangan umum sudah tersedia dan siap pakai. Ini membuat proses belajar lebih mudah karena pengembang tidak harus mencari atau mengatur banyak alat tambahan.

- Django juga mengedepankan praktik pengembangan yang baik, seperti pembagian tugas antara bagian yang mengatur logika (views), data (models), dan tampilan (templates) melalui arsitektur Model-View-Template (MVT). Dengan pendekatan ini, pengembang belajar cara mengorganisasi kode dengan baik dari awal.

5. Mengapa model pada Django disebut sebagai ORM?
    1. Mudah Dipelajari dan Dipakai:
    Django memiliki dokumentasi yang sangat lengkap dan terstruktur dengan baik, sehingga memudahkan pemula memahami konsep-konsep dasar pengembangan web. Selain itu, Django juga memiliki banyak tutorial dan komunitas yang besar    

    2. Praktik Terbaik dan Struktur yang Jelas:
    Django dirancang dengan prinsip "konvensi lebih baik daripada konfigurasi" dan "don't repeat yourself (DRY)." Ini berarti framework ini memberikan struktur proyek yang jelas dan mendorong praktik pengkodean yang baik. 