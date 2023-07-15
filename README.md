# Super Self-Cashier 

Super Self-Cashier dibuat untuk melakukan perbaikan proses bisnis pada supermarket. Dengan menggunakan sistem ini, pelanggan bisa langsung memasukkan item, harga dan fitur lainnya.

## Latar Belakang Problems
Andi adalah seorang pemilik supermarket besar di salah datu kota di Indonesia. Andi akan membuat sistem kasir yang self-service di supermarket miliknya. Sehingga customer bisa langsung memasukan item yang dibeli, jumlah item yang dibeli, dan harga item yang dibeli dan fitur yang lain. 

## Feature Requirements
Sistem yang dibuat mengacu pada Journey Customer Supermarket yang terdiri atas: 
1. Customer membuat ID Transaksi customer
2. Customer memasukkan nama item, jumlah item, dan harga barang
3. Jika ternyata ada kesalahan dalam memasukan nama item dan harga item tetapi tidak ingin menghapus itemnya, customer dapat melakukan editing
4. Jika batal membeli item belanjaan customer bisa melakukan penghapusan/reset transaksi
5. Customer yang berbelanja online juga bisa melakukan editing yang sama.
6. Pada supermarket ini terdapat ketentuan diskon.
    - Jika belanjaan diatas 200.000 maka akan mendapatkan diskon 5%
    - Jika belanjaan diatas 300.000 maka akan mendapatkan diskon 8%
    - Jika belanjaan diatas 500.000 maka akan mendapatkan diskon 10%

Melihat Journey Customer yang telah ditentukan, maka kita dapat membuat Flowchart sebagai berikut:
![Diagram Self Super Cashier Project Python Pacmann](https://github.com/ricobag/Cashier-Project-Pacmann-1/assets/139092538/ed88467b-6fda-4a74-a114-4791037be287)
Berdasarkan Flowchart di atas, maka proses transaksi dalam sistem pemrograman membutuhkan beberapa langkah mulai dari pembentukan kelas transaksi sampai dengan proses checkout belanja. Beberapa fungsi yang digunakan antara lain :
- Membuat kelas transaksi dan fungsi otomatis id transaksi
![Pembuatan Kelas Transaksi](https://github.com/ricobag/Cashier-Project-Pacmann-1/assets/139092538/b57a3c02-18bb-4c7d-8e04-aa34cdd36e17)
- Membuat fungsi penambahan item dalam transaksi
 ![Pembuatan fungsi add item pada kelas transaksi](https://github.com/ricobag/Cashier-Project-Pacmann-1/assets/139092538/28190b28-ab28-422e-a75b-122717beb8d6)
- Membuat fungsi edit item dalam transaksi
 ![Pembuatan fungsi edit item pada kelas transaksi](https://github.com/ricobag/Cashier-Project-Pacmann-1/assets/139092538/6eb794a4-720a-413c-8e61-78baf68c9a99)
- Membuat fungsi delete item dalam transaksi
 ![Pembuatan fungsi delete item pada kelas transaksi](https://github.com/ricobag/Cashier-Project-Pacmann-1/assets/139092538/9c75884e-09fc-45ef-ad2f-bdbd357bfab5)
- Membuat fungsi kalkulasi harga dalam transaksi
 ![Pembuatan fungsi calculate total pada kelas transaksi](https://github.com/ricobag/Cashier-Project-Pacmann-1/assets/139092538/9e9611d9-a6d8-4cf3-a424-ff81fd08a0b8)
- Membuat fungsi kalkulasi diskon dalam transaksi
 ![Pembuatan fungsi discount rate pada kelas transaksi](https://github.com/ricobag/Cashier-Project-Pacmann-1/assets/139092538/2d8728cb-4c36-4183-89f1-3241371c83a5)
- Membuat fungsi reset transaksi
 ![Pembuatan fungsi reset transaksi pada kelas transaksi](https://github.com/ricobag/Cashier-Project-Pacmann-1/assets/139092538/37ab1335-a542-4c6f-aaf0-9f45bb891366)
- Membuat fungsi menampilkan hasil transaksi
![Pembuatan fungsi display transaksi pada kelas transaksi](https://github.com/ricobag/Cashier-Project-Pacmann-1/assets/139092538/48dc0c48-e8f0-41b2-8864-9be08488107c)
Setelah fungsi-fungsi pada kelas transaksi dibuat, maka selanjutnya akan berfokus pada fungsi-fungsi untuk test case berdasarkan case yang telah diberikan. Fungsi tersebut antara lain terdiri atas :
- Membuat fungsi create_transaction() dengan menginisiasikan ke dalam kelas Transaction()
![Pembuatan fungsi create transaksi](https://github.com/ricobag/Cashier-Project-Pacmann-1/assets/139092538/c070f0db-fcb4-4f62-9a52-6a815f8d1493)
- Membuat sub menu transaksi dengan input dengan perintah while True, untuk membuat loop yang berulang dalam transaksi
![Pembuatan fungsi loop transaksi](https://github.com/ricobag/Cashier-Project-Pacmann-1/assets/139092538/76323520-0581-4f45-9796-f0922636d09e)
- Membuat fungsi-fungsi if-elif berdasarkan journey customer yang diberikan.
![Pembuatan fungsi if-elif transaksi](https://github.com/ricobag/Cashier-Project-Pacmann-1/assets/139092538/71437ce7-3c68-45bb-a96b-8aaadb4d02a7)
- Memanggil fungsi display pada kelas transaksi.
![Pembuatan fungsi display transaksi](https://github.com/ricobag/Cashier-Project-Pacmann-1/assets/139092538/02a852a9-1a23-4ceb-965d-5df6e26402d2)
