# Proxy888

Proxy888 adalah sebuah skrip Python untuk membaca, memvalidasi, dan memformat daftar proxy dari sebuah file teks. Skrip ini memungkinkan pengguna untuk memilih format proxy yang diinginkan (HTTP, HTTPS, atau SOCKS) dan menambahkan prefix yang sesuai ke setiap proxy dalam daftar.

## Fitur

- Membaca daftar proxy dari file teks.
- Memvalidasi format proxy (IP:PORT).
- Menambahkan prefix yang ditentukan oleh pengguna (http://, https://, atau socks5://).
- Menyimpan daftar proxy yang telah diformat ke dalam file teks baru.

## Prasyarat

Pastikan Anda telah menginstal Python 3.x di sistem Anda. Anda dapat mengunduh Python dari [situs resmi Python](https://www.python.org/).

## Instalasi

1. Clone repositori ini ke komputer Anda:

    ```bash
    git clone https://github.com/marioatmajanugraha/Proxy888.git
    cd Proxy888
    ```

2. Pastikan Anda memiliki file `input_proxies.txt` yang berisi daftar proxy yang ingin diformat.

## Penggunaan

1. Jalankan skrip `main.py`:

    ```bash
    python main.py
    ```

2. Anda akan diminta untuk memilih format proxy yang diinginkan:
    ```
    Choose the proxy format:
    1. HTTP
    2. HTTPS
    3. SOCKS
    ```

3. Masukkan nomor yang sesuai dengan pilihan Anda dan tekan Enter.

4. Skrip akan membaca proxy dari `input_proxies.txt`, memvalidasi formatnya, menambahkan prefix yang sesuai, dan menyimpan daftar proxy yang telah diformat ke dalam file `formatted_proxies.txt`.

## Contoh

Contoh format file `input_proxies.txt`:

192.168.0.1:8080,
10.0.0.1:3128,
172.16.0.1:1080,

Setelah menjalankan skrip dan memilih format HTTPS, file `formatted_proxies.txt` akan berisi:

https://192.168.0.1:8080,
https://10.0.0.1:3128,
https://172.16.0.1:1080,

## Kontribusi

Jika Anda ingin berkontribusi pada proyek ini, silakan fork repositori ini, buat branch baru untuk fitur atau perbaikan Anda, dan buat pull request. Kami akan dengan senang hati meninjau dan menggabungkan kontribusi Anda.

## Lisensi

Proyek ini dilisensikan di bawah lisensi MIT. Lihat file [LICENSE](LICENSE) untuk informasi lebih lanjut.

## Kontak

Jika Anda memiliki pertanyaan atau saran, jangan ragu untuk menghubungi saya melalui [profil GitHub saya](https://github.com/marioatmajanugraha).
