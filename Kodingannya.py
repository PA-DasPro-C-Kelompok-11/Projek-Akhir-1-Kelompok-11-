from prettytable import PrettyTable
from pwinput import pwinput
import json
import os
from datetime import datetime

PathjsonUser = r"C:\Users\LENOVO\OneDrive\Documents\PA Properti Rumah\user.json"

with open(PathjsonUser, "r") as jsonUser:
    dataUser = json.loads(jsonUser.read())

def tambahUser():
    try:
        with open(PathjsonUser, "r") as jsonUser:
            return json.load(jsonUser)
    except FileNotFoundError:
        return {"Nama": [], "Password": [], "saldo": []}
    
def simpanUser(data):
    with open(PathjsonUser, "w") as jsonUser:
        json.dump(data, jsonUser, indent=4)

PathjsonData = r"C:\Users\LENOVO\OneDrive\Documents\PA Properti Rumah\list.json"

def clear():
    os.system("cls")

def MembacaData():
    with open(PathjsonData, 'r') as file:
        data_produk = json.load(file)
    return data_produk
    
def MengupdateData(Data):
    with open(PathjsonData, 'w') as file:
        json.dump(Data, file, indent=4)

def daftaruser():
    clear()
    users = tambahUser()
    while True:
        try:
            print("===== REGISTER USER =====")
            namaUser  = input("Masukkan nama: ").lower()  
            if any(user["Nama User"].lower() == namaUser  for user in users): 
                print(f"{namaUser } sudah terdaftar.")
            else:
                passwordUser  = pwinput("Password: ", "*")
                new_user = {
                    "Nama User": namaUser ,
                    "Pw User": passwordUser ,
                    "Saldo": 0
                }
                users.append(new_user)
                simpanUser (users)
                print("====================")
                print(" REGISTER BERHASIL ")
                print("====================")
            break
        except ValueError:
            print("Terdapat kesalahan, silahkan coba lagi!")
        except KeyboardInterrupt:
            print("Tolong untuk tidak menekan Ctrl dan C secara bersamaan!")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")


def loginUser ():
    clear()
    global username
    try:
        users_data = tambahUser()
    except Exception as e:
        print(f"Terjadi kesalahan saat memuat data pengguna: {e}")
        return False
    
    if not users_data:
        print("User  tidak tersedia.")
        return False
    
    print("===== LOGIN USER =====")
    
    try:
        username = input("Masukkan username: ").strip().lower()  
        password = pwinput("Masukkan password: ", "*")
        
        if not username:
            print("Username tidak boleh kosong.")
            return False
        if not password:
            print("Password tidak boleh kosong.")
            return False
        
        for user in users_data:
            if user["Nama User"].lower() == username:
                if user["Pw User"] == password:
                    print("Login berhasil!")
                    return True
                else:
                    print("Password salah!")
                    return False
        
        print("Username tidak ditemukan!")
        return False

    except KeyboardInterrupt:
        print("\nLogin dibatalkan.")
        return False
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return False

def loginAdmin():
    clear()
    while True:
        admin = {
            "Jabbar": "123",
            "Maria": "123",
            "Liya": "123",
        }
        username = input("Masukkan Nama Anda       : ")
        password = pwinput("Masukkan Password        : ",'*')
        if username in admin and password == admin[username]:
            return True
            
        else:
            print("Nama pengguna atau kata sandi salah.")
            return False
            


def TampilProperti():
    clear()
    Data = MembacaData() 
    print("======== LIST PROPERTI =======")
    for kategori in Data["Kategori"]:
        nama_kategori = kategori["Nama Kategori"]
        print(f"\nKategori: {nama_kategori}")
        
        table = PrettyTable()
        table.field_names = ["ID", "Tipe/Jenis", "Harga", "Kuantitas"]
        table.title = f"Daftar Properti {nama_kategori}"
        
        for produk in kategori["Properti"]:
            table.add_row([
                produk["ID"], 
                produk["Tipe/Jenis"], 
                produk["Harga"], 
                produk["Kuantitas"]
            ])
        
        print(table)




def TambahProperti():
    clear()
    Data = MembacaData()
    TampilProperti()
    print("========= MENAMBAH PROPERTI ==========")
    print("")
    while True:
        print("1. Menambah Menu Di Kategori Rumah")
        print("2. Menambah Menu Di Kategori Tanah")
        print("3. Menambah Menu Di Kategori Ruko")
        print("4. Kembali")
        print("")
        Kategori = input("Masukkan Pilihan: ")
        if Kategori in ['1', '2', '3']:
            break
        elif Kategori == '4' :
            return
        else:
            print("Tidak ada pilihan")

    Menu = input("Masukkan Menu Baru: ")
    
    while True:
        print("Minimal harga 50.000.000")

        try:
            HargaMenu = int(input(f"Masukkan Harga Menu {Menu}: "))
            if 50000000 <= HargaMenu:
                break
            else:
                print("Harga Yang Anda Masukkan Tidak Sesuai ")
        except (ValueError, KeyboardInterrupt):
            print("Silahkan Masukkan Data Yang Valid dan Jangan Menekan CTRL + C ")



    while True:
        try:
            Kuantitas = int(input("Masukkan Kuantitas Properti: "))
            if Kuantitas > 0:
                break
            else:
                print("Kuantitas harus lebih dari 0")
        except (ValueError, KeyboardInterrupt):
            print("Masukkan angka yang valid untuk kuantitas")

    new_id = 1
    for item in Data.get("Kategori", []):
        for produk in item.get("Properti", []):
            if produk.get("ID", 0) >= new_id:
                new_id = produk["ID"] + 1


    MenuBaru = {
        'ID': new_id, 
        'Tipe/Jenis': Menu, 
        'Harga': HargaMenu,
        'Kuantitas': Kuantitas  
    }

    if Kategori == '1':
        for item in Data["Kategori"]:
            if item.get("Nama Kategori") == "Rumah":
                item["Properti"].append(MenuBaru)
                break
    elif Kategori == '2':
        for item in Data["Kategori"]:
            if item.get("Nama Kategori") == "Tanah":
                item["Properti"].append(MenuBaru)
                break
    elif Kategori == '3':
        for item in Data["Kategori"]:
            if item.get("Nama Kategori") == "Ruko":
                item["Properti"].append(MenuBaru)
                break

    MengupdateData(Data)
    print("+==================== MENU BERHASIL DI TAMBAHKAN ========================+")
    print(f"|         Properti {Menu} berhasil ditambahkan dengan ID {new_id}            ")
    print(f"|         Dengan Kuantitas {Kuantitas}                                   ")
    print("+========================================================================+")


def UpdateProperti():
    clear()
    Data = MembacaData()
    print("============== MENGUPDATE PROPERTI ===========")
    while True:
        clear()
        print("1. Mengubah Menu di Kategori Rumah")
        print("2. Mengubah Menu di Kategori Tanah")
        print("3. Mengubah Menu di Kategori Ruko")
        print("4. Kembali")
        Kategori = input("Masukkan pilihan: ")
        if Kategori == '1':
            nama_kategori = "Rumah"
            break
        elif Kategori == '2':
            nama_kategori = "Tanah"
            break
        elif Kategori == '3':
            nama_kategori = "Ruko"
            break
        elif Kategori == '4' :
            return
        else:
            print("Kategori yang dimasukkan tidak tersedia.")
    
    for item in Data["Kategori"]:
        if item.get("Nama Kategori") == nama_kategori:
            print(f"\nKategori: {nama_kategori}")
            for properti in item.get("Properti", []):
                print(f"ID: {properti['ID']} | Tipe/Jenis: {properti['Tipe/Jenis']} | Harga: {properti['Harga']} | Kuantitas: {properti['Kuantitas']}")

            try:
                id_properti = int(input("Masukkan ID Produk yang Ingin Diupdate: "))
            except (ValueError, KeyboardInterrupt):
                print("Silahkan Masukkan Data Yang Valid dan Jangan Menekan CTRL + C")
                return

            for properti in item.get("Properti", []):
                if properti.get("ID") == id_properti:
                    tipe_baru = input("Masukkan Nama Menu Baru: ")
                    
                    while True:
                        try:
                            print("Minimal harga 50.000.000")
                            harga_baru = int(input("Masukkan Harga Baru: "))
                            if 50000000 <= harga_baru:
                                break
                            else:
                                print("Harga Yang Anda Masukkan Tidak Sesuai")
                        except (ValueError, KeyboardInterrupt):
                            print("Silahkan Masukkan Data Yang Valid dan Jangan Menekan CTRL + C")
                    
                    while True:
                        try:
                            kuantitas_baru = int(input("Masukkan Kuantitas Baru: "))
                            if kuantitas_baru >= 0:
                                break
                            else:
                                print("Kuantitas harus bernilai 0 atau lebih")
                        except (ValueError, KeyboardInterrupt):
                            print("Silahkan Masukkan Data Yang Valid dan Jangan Menekan CTRL + C")
                    
                    properti['Tipe/Jenis'] = tipe_baru
                    properti['Harga'] = harga_baru
                    properti['Kuantitas'] = kuantitas_baru
                    
                    MengupdateData(Data)
                    print("Properti berhasil diupdate.")
                    return
                
            print(f"Properti dengan ID '{id_properti}' tidak ditemukan dalam kategori '{nama_kategori}'.")
            return
        
    print(f"Tidak ada kategori '{nama_kategori}' yang ditemukan.")


def HapusProperti():
    clear()
    Data = MembacaData()
    TampilProperti()
    print("================== MENGHAPUS PROPERTI =============")
    
    while True:
        try:
            print("1. Rumah")
            print("2. Tanah")
            print("3. Ruko")
            print("4. Kembali")
            Kategori = input("Masukkan pilihan kategori: ")
            
            if Kategori == '1':
                nama_kategori = "Rumah"
            elif Kategori == '2':
                nama_kategori = "Tanah"
            elif Kategori == '3':
                nama_kategori = "Ruko"
            elif Kategori == '4':
                return
            else:
                print("Kategori tidak tersedia.")
                continue
            
            id_hapus = int(input("Masukkan ID Produk yang Ingin Dihapus: "))
            for kategori in Data["Kategori"]:
                if kategori["Nama Kategori"] == nama_kategori:
                    list_properti = kategori["Properti"]
                    for item in list_properti:
                        if item["ID"] == id_hapus:
                            list_properti.remove(item)
                            MengupdateData(Data)
                            print(f"Properti dengan ID {id_hapus} berhasil dihapus dari kategori {nama_kategori}.")
                            return
            
            print(f"Properti dengan ID {id_hapus} tidak ditemukan dalam kategori {nama_kategori}.")
        
        except ValueError:
            print("ID harus berupa angka.")


def Sortingterendah():
    clear()
    Data = MembacaData()
    print("================= SORTING PROPERTI =============")
    for kategori in Data["Kategori"]:
        nama_kategori = kategori["Nama Kategori"]
        
        sorted_properti = sorted(
            kategori["Properti"], 
            key=lambda x: x.get('Harga', 0)
        )
        
        table = PrettyTable()
        table.field_names = ["ID", "Tipe/Jenis", "Harga", "Kuantitas"]
        table.title = f"Daftar Properti {nama_kategori} (Harga Terendah ke Tertinggi)"
        
        for produk in sorted_properti:
            table.add_row([
                produk["ID"], 
                produk["Tipe/Jenis"], 
                produk["Harga"], 
                produk.get("Kuantitas", 0)
            ])
        
        print(table)
    print('Ketik "ENTER" jika ingin kembali')
    input()
    

def Sortingtertinggi():
    clear()
    Data = MembacaData()
    print("================= SORTING PROPERTI =============")
    for kategori in Data["Kategori"]:
        nama_kategori = kategori["Nama Kategori"]
    
        sorted_properti = sorted(
            kategori["Properti"], 
            key=lambda x: x.get('Harga', 0),
            reverse=True  
        )
        
        table = PrettyTable()
        table.field_names = ["ID", "Tipe/Jenis", "Harga", "Kuantitas"]
        table.title = f"Daftar Properti {nama_kategori} (Harga Tertinggi ke Terendah)"
        
        for produk in sorted_properti:
            table.add_row([
                produk["ID"], 
                produk["Tipe/Jenis"], 
                produk["Harga"], 
                produk.get("Kuantitas", 0)
            ])
        
        print(table)
    print('Ketik "ENTER" jika ingin kembali')
    input()


def lihatSaldo3():
    clear()
    print("============ MELIHAT SALDO ============")
    if 'username' not in globals():
        print("Silakan login terlebih dahulu!")
        return
        
    try:
        users = tambahUser ()  
        user_found = False
        
        for user in users:
            if user["Nama User"].lower() == username.lower():  
                user_found = True
                saldo = user["Saldo"]
                print("+=================================+")
                print(f"| SALDO ANDA ADALAH Rp {saldo:,} |")
                print("+=================================+")
                break
                
        if not user_found:
            print("Error: User tidak ditemukan")
            
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")

def topUp4():
    clear()
    if 'username' not in globals():
        print("Silakan login terlebih dahulu!")
        return
        
    print("======= TOP UP SALDO ========")
    users = tambahUser ()
    print("[1].  Rp 25.000.000")
    print("[2].  Rp 50.000.000")
    print("[3].  Rp 100.000.000")
    print("[4].  Rp 150.000.000")
    print("[5].  Rp 300.000.000")
    print("[6].  Kembali")
    
    try:
        pilihan = int(input("Masukkan pilihan nominal (1-6): "))
        
        nominal = [25000000, 50000000, 100000000, 150000000, 300000000]
        
        if 1 <= pilihan <= 5:
            user_found = False
            for user in users:
                if user["Nama User"].lower() == username.lower():
                    user_found = True
                    konfirmasi = input(f"Anda akan top up sebesar Rp {nominal[pilihan-1]:,}. Lanjutkan? (y/n): ")
                    if konfirmasi.lower() == 'y':
                        user["Saldo"] += nominal[pilihan - 1]
                        simpanUser (users)
                        print(f"Top up berhasil!")
                        print(f"Saldo anda sekarang adalah Rp { user['Saldo']:,}")
                    else:
                        print("Top up dibatalkan")
                    break
            
            if not user_found:
                print("Error: User tidak ditemukan")
                
        elif pilihan == 6:
            return
        else:
            print("Pilihan anda tidak tersedia")
            
    except ValueError:
        print("Masukkan pilihan yang valid (angka 1-6)")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")


def beliProperti():
    while True: 
        clear()
        print("========= BELI PROPERTI =============")
        if 'username' not in globals():
            print("Silakan login terlebih dahulu!")
            return
        
        users = tambahUser ()
        Data = MembacaData()
        
        TampilProperti()
        
        print("1. Rumah")
        print("2. Tanah")
        print("3. Ruko")
        print("4. Kembali")
        kategori = int(input("Masukkan pilihan:  "))
        
        if kategori == 4:
            return

        id_properti = int(input("Masukkan ID properti yang ingin dibeli: "))
        
        if kategori == 1:
            kategori = "Rumah"
        elif kategori == 2:
            kategori = "Tanah"
        elif kategori == 3:
            kategori = "Ruko"

        properti_ditemukan = None
        for kat in Data["Kategori"]:
            if kat["Nama Kategori"] == kategori:
                for prop in kat["Properti"]:
                    if prop["ID"] == id_properti:
                        properti_ditemukan = prop
                        break
                if properti_ditemukan:
                    break
        
        if not properti_ditemukan:
            print("Properti tidak ditemukan.")
            input("Tekan ENTER untuk melanjutkan...")
            continue
        
        if properti_ditemukan["Kuantitas"] <= 0:
            print("Maaf, properti ini sudah habis/tidak tersedia.")
            input("Tekan ENTER untuk melanjutkan...")
            continue  
        
        user = next((u for u in users if u["Nama User"].lower() == username.lower()), None)
        if not user:
            print("User  tidak ditemukan.")
            input("Tekan ENTER untuk melanjutkan...")
            continue  
        
        if user["Saldo"] < properti_ditemukan["Harga"]:
            print("Saldo Anda tidak mencukupi untuk membeli properti ini.")
            input("Tekan ENTER untuk melanjutkan...")
            continue 
        
        while True:
            try:
                kuantitas = int(input("Masukkan jumlah properti yang ingin dibeli: "))
                if 1 <= kuantitas <= properti_ditemukan["Kuantitas"]:
                    break
                else:
                    print(f"Jumlah harus antara 1 dan {properti_ditemukan['Kuantitas']}.")
            except ValueError:
                print("Masukkan jumlah yang valid.")
        
        konfirmasi = input(f"Anda akan membeli {kuantitas} {properti_ditemukan['Tipe/Jenis']} seharga Rp {properti_ditemukan['Harga']:,} per unit. Total: Rp {properti_ditemukan['Harga'] * kuantitas:,}. Lanjutkan? (y/n): ") 
        if konfirmasi.lower() != 'y':
            print("Pembelian dibatalkan.")
            input("Tekan ENTER untuk melanjutkan...")
            continue  
        
        user["Saldo"] -= properti_ditemukan["Harga"] * kuantitas
        properti_ditemukan["Kuantitas"] -= kuantitas  
        
        simpanUser (users)
        MengupdateData(Data)
        
        print(f"Selamat! Anda telah berhasil membeli {kuantitas} {properti_ditemukan['Tipe/Jenis']}.")
        print(f"Saldo Anda sekarang: Rp {user['Saldo']:,}")
        
        simpanStruk(username, properti_ditemukan, user["Saldo"], kategori, kuantitas)
        
        break  




def simpanStruk(username, properti, saldo_sekarang, kategori, kuantitas):
    total_harga = properti['Harga'] * kuantitas  
    waktu_pembelian = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 

    struk_content = f"""
        +=================================+
    |          STRUK PEMBELIAN        |
    +=================================+
    | Nama User: {username}
    | Kategori: {kategori}
    | Tipe/Jenis: {properti['Tipe/Jenis']}
    | Harga Satuan: Rp {properti['Harga']:,}
    | Jumlah: {kuantitas}
    | Total Harga: Rp {total_harga:,}
    | Saldo Setelah Pembelian: Rp {saldo_sekarang:,}
    | Tanggal & Waktu: {waktu_pembelian}
    +=================================+
    """
    
    filename = f"{username}strukpembelian.txt"
    
    with open(filename, "a") as file:
        file.write(struk_content.strip())
        file.write("\n")
    


def lihatStruk(username):
    clear()
    print(f"========= LIHAT STRUK PEMBELIAN UNTUK {username.upper()} =========")
    
    filename = f"{username}strukpembelian.txt"
    
    if os.path.exists(filename):
        with open(filename, "r") as file:
            struk_content = file.read()
            print(struk_content)
    else:
        print("Struk pembelian tidak ditemukan untuk pengguna ini.")
    
    print('Ketik "ENTER" untuk kembali')
    input()



def MenuUser ():
    clear()
    global username 
    while True:
        print("============= MENU USER ==============")
        print("Selamat Datang User")
        print("1. Lihat Properti")
        print("2. Tambah Saldo")
        print("3. Lihat Saldo")
        print("4. Beli Properti")
        print("5. Sorting Berdasarkan Harga Terendah setiap Kategori")
        print("6. Sorting Berdasarkan Harga Tertinggi setiap Kategori ")
        print("7. Lihat Struk")
        print("8. Kembali")
        
        try:
            menuUser   = int(input("Masukkan pilihan: "))  
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka antara 1 dan 7.")
            continue  

        if menuUser  == 1:
            try:
                TampilProperti()
                print("")
                print('Pencet "ENTER" jika ingin kembali')
                input()
            except Exception as e:
                print(f"Terjadi kesalahan saat menampilkan properti: {e}")
        elif menuUser  == 2:
            try:
                topUp4()
            except Exception as e:
                print(f"Terjadi kesalahan saat menambah saldo: {e}")
        elif menuUser  == 3:
            try:
                lihatSaldo3()
            except Exception as e:
                print(f"Terjadi kesalahan saat melihat saldo: {e}")
        elif menuUser  == 4:
            try:
                beliProperti()
            except Exception as e:
                print(f"Terjadi kesalahan saat membeli properti: {e}")
        elif menuUser  == 5:
            try:
                Sortingterendah()
                4
            except Exception as e:
                print(f"Terjadi kesalahan saat menyortir properti: {e}")
        elif menuUser  == 6:  
            try:
                Sortingtertinggi()
                print("")
                print('Pencet "ENTER" jika ingin kembali')
                input()
            except Exception as e:
                print(f"Terjadi kesalahan saat menyortir properti: {e}")
        elif menuUser  == 7:  
            try:
                lihatStruk(username)
            except Exception as e:
                print(f"Terjadi kesalahan saat melihat struk: {e}")
        elif menuUser  == 8:
            return
        else:
            print("Pilihan tidak valid. Silakan masukkan angka antara 1 dan 7.")

def pilihanUser ():
    clear()
    while True:
        print("1. Daftar User")
        print("2. Login User")
        print("3. Kembali")
        
        try:
            pilihanUser  = int(input("Masukkan pilihan: "))  
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka 1, 2, atau 3.")
            continue  

        if pilihanUser  == 1:
            try:
                daftaruser()
            except Exception as e:
                print(f"Terjadi kesalahan saat mendaftar user: {e}")
        elif pilihanUser  == 2:
            try:
                if loginUser ():
                    MenuUser ()
                else:
                    return
            except Exception as e:
                print(f"Terjadi kesalahan saat login: {e}")
        elif pilihanUser  == 3:
            return
        else:
            print("Pilihan tidak valid. Silakan masukkan angka 1, 2, atau 3.")

def MenuAdmin():
    clear()
    while True:
        print("============== MENU ADMIN =============")
        print("Selamat Datang Admin")
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")  
        print("5. Sorting Berdasarkan Harga Terendah setiap Kategori")
        print("6. Sorting Berdasarkan Harga Tertinggi setiap Kategori")
        print("7. Kembali")
        
        try:
            menuAdmin = int(input("Masukkan pilihan: "))  
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka antara 1 dan 6.")
            continue  

        if menuAdmin == 1:
            try:
                TambahProperti()
            except Exception as e:
                print(f"Terjadi kesalahan saat menambahkan properti: {e}")
        elif menuAdmin == 2:
            try:
                TampilProperti()
                input("Tekan Enter untuk kembali ke menu...")
            except Exception as e:
                print(f"Terjadi kesalahan saat menampilkan properti: {e}")
        elif menuAdmin == 3:
            try:
                UpdateProperti()
            except Exception as e:
                print(f"Terjadi kesalahan saat memperbarui properti: {e}")
        elif menuAdmin == 4:
            try:
                HapusProperti()
            except Exception as e:
                print(f"Terjadi kesalahan saat menghapus properti: {e}")
        elif menuAdmin == 5:
            try:
                Sortingterendah()
                print("")
                print('Pencet "ENTER" jika ingin kembali')
                input()
            except Exception as e:
                print(f"Terjadi kesalahan saat menyortir properti: {e}")
        elif menuAdmin == 6:
            try:
                Sortingtertinggi()
                print("")
                print('Pencet "ENTER" jika ingin kembali')
                input()
            except Exception as e:
                print(f"Terjadi kesalahan saat menyortir properti: {e}")
        elif menuAdmin == 7:
            return
        else:
            print("Pilihan tidak valid. Silakan masukkan angka antara 1 dan 6.")


def MenuAwal():
    clear()
    while True:
        print("=============== MENU AWAL ===============")
        print("Selamat Datang di PROPERTIX")
        print("1. Admin")
        print("2. Pembeli")
        print("3. Keluar")
        
        try:
            pilihan = int(input("Masukkan pilihan role: ")) 
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka 1, 2, atau 3.")
            continue  
        
        if pilihan == 1:
            try:
                if loginAdmin():
                    MenuAdmin()
            except Exception as e:
                print(f"Terjadi kesalahan saat login sebagai admin: {e}")
        elif pilihan == 2:
            try:
                pilihanUser ()
            except Exception as e:
                print(f"Terjadi kesalahan saat mengakses menu pengguna: {e}")
        elif pilihan == 3:
            print("Terima kasih telah menggunakan PROPERTIX. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka 1, 2, atau 3.")


MenuAwal()


