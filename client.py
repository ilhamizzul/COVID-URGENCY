# import library socket karena akan menggunakan IPC socket
import socket
import json

TCP_IP = "127.0.0.1"        # definisikan tujuan IP server
TCP_PORT = 3000             # definisikan port dari server yang akan terhubung
BUFFER_SIZE = 1024          # definisikan ukuran buffer untuk mengirimkan pesan

# definisikan pesan yang akan disampaikan
PESAN = {}
PESAN['NIKPelapor'] = input("Masukkan NIK pelapor :")
PESAN['namaPelapor'] = input("Masukkan nama pelapor :")
PESAN['namaTerduga'] = input("Masukkan nama terduga pasien covid :")
PESAN['alamatTerduga'] = input("Masukkan alamat terduga pasien covid :")
PESAN['gejala'] = input("Masukkan detail gejala yang dimiliki pasien covid :")


# buat socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan koneksi ke server dengan parameter IP dan Port yang telah didefinisikan
s.connect((TCP_IP, TCP_PORT))

# kirim pesan ke server
s.send(json.dumps(PESAN).encode())

# terima pesan dari server
data = s.recv(BUFFER_SIZE)

# tampilkan pesan/reply dari server
print("feedback : ", data.decode())

# tutup koneksi
s.close()

