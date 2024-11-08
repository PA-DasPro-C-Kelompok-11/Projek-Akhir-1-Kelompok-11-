# Pembelian Properti

## Deskripsi Program
Program ini adalah sebuah program dalam pembelian properti. Terdapat 2 role yaitu admin dan user. Role user dapat melihat properti yang dijual, membeli list properti, melihat saldo, menambah saldo untuk menonton film, melihat saldo dan menambahkan saldo, dan melihat urutan harga properti dari yang termurah dan termahal di setiap kategorinya. Untuk role admin sendiri dapat melakukan C.R.U.D. (Create, Read, Update dan Delete). Dan sama seperti user, admin juga bisa melihat urutan properti dari yang termurah dan tertinggi setiap kategorinya.

## Library
Terdapat 5 library yang kami gunakan di program ini yaitu:
1. PrettyTable untuk membuat tabel secara otomatis dan rapi,
2. os disini kami gunakan untuk membersihkan tampilan di terminal,
3. pwinput untuk membuat password tidak langsung terlihat,
4. datetime digunakan pada bagian struk untuk menunjukkan tanggal dan waktu pembelian,
5. json untuk mengakses dan mengupdate json.

## Fitur
### User

1. Melihat Produk
2. Menambah Saldo
3. Melihat Saldo
4. Membeli Produk
5. Sorting Produk Berdasarkan Harga dari yang Termurah
6. Sorting Produk Berdasarkan Harga dari yang Termahal
7. Melihat Struk/Invoice

### Admin

1. Menambah Produk 
2. Melihat Produk
3. Mengubah Produk
4. Menghapus Produk
5. Sorting Produk Berdasarkan Harga dari yang Termurah
6. Sorting Produk Berdasarkan Harga dari yang Termahal


# Penggunaan Program

## Menu Awal

![Screenshot 2024-11-08 220853](https://github.com/user-attachments/assets/6f3db947-2dcf-4e97-8dd0-d88e64be2864)


Tampilan yang pertama kali muncul saat menjalankan program adalah menu awal. Disini terdapat 3 pilihan yaitu Role Admin, Role Pembeli atau User, dan Keluar


### Login Admin

![Screenshot 2024-11-08 221052](https://github.com/user-attachments/assets/07090a1b-6958-4ce4-b388-2b1e3c021377)

Jika nomor 1 yang di input di menu awal, maka akan memunculkan menu admin. Pertama, masukkan nama dan password dari admin

![Screenshot 2024-11-08 221156](https://github.com/user-attachments/assets/08cf3656-47c2-48c3-8bd5-833ae2a9aa6d)

Jika ingin masuk ke menu admin maka masukkan:
nama akun : Jabbar
password : 123
Jika benar maka akan di arahkan ke menu admin


### Login User


![Screenshot 2024-11-08 221537](https://github.com/user-attachments/assets/648354c6-fae7-446a-ae08-1a803ffe4b4e)

Jika nomor 2 yang di input di menu awal, maka akan memunculkan pilihan untuk user, yaitu Daftar dan Login.

![Screenshot 2024-11-08 221657](https://github.com/user-attachments/assets/7075455b-a6d7-4577-a637-de7a2190e73e)

Jika user belum mempunyai akun, Ia harus mengdaftar terlebih dahulu dengan nama yang tidak ada dalam database dan password.

![Screenshot 2024-11-08 221704](https://github.com/user-attachments/assets/386476ba-f684-47d5-821d-1bd7a0ee4677)

Jika Daftar berhasil, user akan dibawa kembali dalam pilihan daftar atau login

![Screenshot 2024-11-08 221835](https://github.com/user-attachments/assets/80f89d2b-d9f7-4ba4-800f-b1d355491d57)

Setelah itu, user diminta untuk login menggunakan nama dan passsword yang telah terdaftar

![Screenshot 2024-11-08 221840](https://github.com/user-attachments/assets/8c58dde6-498e-498b-8d38-de03581914ff)

Jika user berhasil, akan memunculkan menu untuk user.


### Keluar Program


![Screenshot 2024-11-08 222240](https://github.com/user-attachments/assets/6d370126-350f-42e5-ba27-1fece1824c81)

Jika nomor 3 yang di input di menu awal, maka program akan berhenti dan memunculkan pesan di atas.

## Menu Admin

![Screenshot 2024-11-08 223257](https://github.com/user-attachments/assets/17ed14c9-45f2-45a3-af14-62ca7a24131b)

Jika nama akun dan password di login admin benar, maka akan memunculkan menu admin. Disini terdapat 7 pilihan yaitu, Create, Read, Update, Delete, Sorting Berdasarkan Harga Terendah setiap Kategori,  Sorting Berdasarkan Harga Tertinggi setiap Kategori, dan Kembali


### Menambah Produk

![Screenshot 2024-11-08 222627](https://github.com/user-attachments/assets/3eb3d063-5f94-40aa-aac9-f7b55c344ac4)

Jika nomor 1 yang di input di menu admin, maka akan masuk ke menu penambahan produk atau properti. Tabel berisi produk akan muncul, dan admin akan diberi pilihan kategori manakah yang ingin ditambah

![Screenshot 2024-11-08 222806](https://github.com/user-attachments/assets/04ea7896-387c-4c0b-abe8-87b440cc9764)

Jika admin memasukkan nomor 1, 2, atau 3, admin diharuskan untuk memasukkan nama produk baru untuk kategori yang dipilih, harga produk dengan ketentuan minimal 50.000.000, dan kuantitas dari produk. Tetapi, jika admin memasukkan nomor 4, Ia akan kembali ke menu admin.

![Screenshot 2024-11-08 232405](https://github.com/user-attachments/assets/509d3c98-7221-4385-9b81-c27d771aba4d)

Jika harga yang dimasukkan tidak sesuai, sistem akan meminta terus untuk memberikan harga yang sesuai.

![Screenshot 2024-11-08 222823](https://github.com/user-attachments/assets/8d9d5ae8-574c-4b42-bd03-9bb0e131c8f5)

Jika berhasil menambahkan, sistem akan memberitahu bahwa produk telah ditambah dan admin akan dikembalikan ke menu admin. Sama apabila pada awal pemilihan tambah memilih nomor 4 yaitu kembali ke menu admin.


### Melihat Produk

![Screenshot 2024-11-08 223111](https://github.com/user-attachments/assets/0292c1b3-5de2-48eb-9a6f-4e13986c8bf3)

Jika nomor 2 yang di input menu admin, maka akan menampilkan list dari produk yang ada. Jika ingin kembali ke menu admin, admin diharuskan mengklik "ENTER".


### Mengubah Produk

![Screenshot 2024-11-08 223422](https://github.com/user-attachments/assets/a7c1e57c-449b-4eed-92a0-505fb237696e)

Jika nomor 3 yang di input menu admin, maka akan menampilkan pilihan kategori manakah yang ingin diubah dan pilihan untuk kembali.

![Screenshot 2024-11-08 223722](https://github.com/user-attachments/assets/47af6c38-760e-478f-87eb-d9ffb6b21dbd)

Jika pilihan 1, 2, atau 3 yang dimasukkan, akan memperlihatkan ID, Nama Produk, Harga, dan Kuantitas dari pilihan kategori yang telah dipilih.

![Screenshot 2024-11-08 223755](https://github.com/user-attachments/assets/3ade1f05-36b6-4c2c-8a7a-d13afb44859b)

Setelah itu, admin diharuskan untuk memilih ID dari produk mana yang ingin diganti, memasukkan nama produk, harga, dan kuantitas dari produk.

![Screenshot 2024-11-08 232542](https://github.com/user-attachments/assets/8b536893-6cda-4f8e-8911-ccf142e92880)

Jika harga yang dimasukkan tidak sesuai, sistem akan meminta terus untuk memberikan harga yang sesuai.

![Screenshot 2024-11-08 223936](https://github.com/user-attachments/assets/66e55ad7-5bb8-4f2d-accb-18d56eb6e0de)

Jika berhasil, sistem akan memberitahu produk sudah diubah dan admin akan kembali ke menu admin. Sama apabila pada awal pemilihan update memilih nomor 4 yaitu kembali ke menu admin.


### Menghapus Produk

![Screenshot 2024-11-08 224149](https://github.com/user-attachments/assets/8cfb449c-f04c-4ded-b309-4602e89f5cf4)

Jika nomor 4 yang di input pada menu admin, maka akan menampilkan list dari produk yang ada dan pilihan kategori produk mana yang ingin dihapus, beserta pilihan untuk kembali.

![Screenshot 2024-11-08 224323](https://github.com/user-attachments/assets/fb24b76a-1a7e-437e-850b-8efc4f2f78d2)

Jika pilihan 1, 2, atau 3 yang dimasukkan, admin diharuskan memasukkan ID dari produk dengan kategori yang dipilih tadi untuk dihapus.

![Screenshot 2024-11-08 224330](https://github.com/user-attachments/assets/6aaf8c85-5639-4ff0-9052-5a882e6761c7)

Jika berhasil dihapus, sistem akan memberitahu bahwa produk telah dihapus dan admin akan dibawa kembali ke menu admin. Sama apabila pada awal pemilihan hapus memilih nomor 4 yaitu kembali ke menu admin.


### Sorting Produk Berdasarkan Harga dari yang Termurah

![Screenshot 2024-11-08 224931](https://github.com/user-attachments/assets/0dd69818-79e5-4b6e-956d-3c3b37af75c9)

Jika nomor 5 yang di input pada menu admin, akan menampilkan list produk yang telah disortir berdasarkan harga dari yang termurah sampai termahal. Apabila ingin kembali, admin harus klik "ENTER".


### Sorting Produk Berdasarkan Harga dari yang Termahal

![Screenshot 2024-11-08 225103](https://github.com/user-attachments/assets/ca28782b-fd61-49cb-8d8e-675ac73288b1)

Jika nomor 6 yang di input pada menu admin, akan menampilkan list produk yang telah disortir berdasarkan harga dari yang termahal sampai termurah. Apabila ingin kembali, admin harus klik "ENTER".


### Kembali

![Screenshot 2024-11-08 225212](https://github.com/user-attachments/assets/a948d625-0188-436b-b563-49706f442684)

Jika nomor 7 yang di input pada menu admin, akan mengembalikan admin ke menu awal.


## Menu User

![Screenshot 2024-11-08 225430](https://github.com/user-attachments/assets/8a393099-7121-48db-82aa-070a47928e30)

Jika user telah melewati login, user akan dibawa ke menu user. Disini terdapat 8 pilihan yaitu, Melihat Properti, Menambah Saldo, Melihat Saldo, Membeli Properti, Sorting Berdasarkan Harga Termurah setiap Kategori, Sorting Berdasarkan Harga Tertinggi setiap Kategori, Melihat Struk, dan Kembali.


### Melihat Properti

![Screenshot 2024-11-08 225642](https://github.com/user-attachments/assets/af2be64f-f719-4a2c-b655-94d8c3baa084)

Jika nomor 1 yang di input pada menu user, sistem akan menampilkan produk. Apabila user ingin kembali ke menu user, user harus klik "ENTER".


### Menambah Saldo

![Screenshot 2024-11-08 225817](https://github.com/user-attachments/assets/9ae2aaa8-1b45-4c9a-9f72-7cdb2f3de7c9)

Jika nomor 2 yang di input pada menu user, user akan dikasih pilihan nominal saldo yang ingin ditambahkan.

![Screenshot 2024-11-08 225912](https://github.com/user-attachments/assets/9523485d-5b2c-4129-929e-9004574f51ae)

Jika sudah, sistem akan memasukkan saldo ke akun user dan memberitahu total saldo dari akun user.


### Melihat Saldo

![Screenshot 2024-11-08 230015](https://github.com/user-attachments/assets/3ce86734-493a-4de4-b523-6c468b767b15)

Jika nomor 3 yang di input pada menu user, sistem akan menampilkan total saldo yang dimiliki user dan langsung mengembalikan user ke menu user.


### Membeli Properti

![Screenshot 2024-11-08 230639](https://github.com/user-attachments/assets/581509bd-244a-4cee-a55e-0755139d73c9)

Jika nomor 4 yang di input pada menu user, sistem akan menampilkan tabel dari produk dan memberikan pilihan kepada user kategori mana kah yang ingin dibeli dan pilihan untuk kembali.

![Screenshot 2024-11-08 230601](https://github.com/user-attachments/assets/48fa1571-dacf-47e9-8d46-028eb679dbce)

Jika user memilih satu dari ketiga kategori yang ada, user diminta untuk memasukkan ID dan jumlah dari properti yang dibeli. Setelah itu, sistem akan mengkonfirmasi user apakah betul produk yang dibeli. Apabila benar, sistem akan menampilkan bahwa pembelian berhasil dan saldo setelah pembelian, dan user akan dibawa kembali ke menu user.


### Sorting Produk Berdasarkan Harga dari yang Termurah

![Screenshot 2024-11-08 224931](https://github.com/user-attachments/assets/0dd69818-79e5-4b6e-956d-3c3b37af75c9)

Jika nomor 5 yang di input pada menu user, akan menampilkan list produk yang telah disortir berdasarkan harga dari yang termurah sampai termahal. Apabila ingin kembali, user harus klik "ENTER".


### Sorting Produk Berdasarkan Harga dari yang Termurah

![Screenshot 2024-11-08 225103](https://github.com/user-attachments/assets/ca28782b-fd61-49cb-8d8e-675ac73288b1)

Jika nomor 6 yang di input pada menu user, akan menampilkan list produk yang telah disortir berdasarkan harga dari yang termahal sampai termurah. Apabila ingin kembali, user harus klik "ENTER".


### Melihat Struk

![Screenshot 2024-11-08 231138](https://github.com/user-attachments/assets/9b55c8f7-19fa-4128-947a-11c68ee50ed9)

Jika nomor 7 yang di input pada menu user, sistem akan menampilkan properti apa saja yang telah dibeli, beserta saldo setelah pembelian, tanggal dan waktu sebuah pembelian. Apabila ingin kembali, user harus klik "ENTER".


### Kembali

![Screenshot 2024-11-08 231426](https://github.com/user-attachments/assets/95ee5dc3-7d7b-432b-a7c3-3e1bbd94e80e)


Jika nomor 8 yang di input pada menu user, user akan dibawa kembali pada bagian Daftar atau Login User.




