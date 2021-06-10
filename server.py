# import library socket karena akan menggunakan IPC socket
import socket
from datetime import datetime
import json
import random

TCP_IP = "127.0.0.1"    # definisikan alamat IP binding  yang akan digunakan 
TCP_PORT = 3000         # definisikan port number binding  yang akan digunakan 
BUFFER_SIZE = 1024      # definisikan ukuran buffer untuk mengirimkan pesan

# buat socket bertipe TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((TCP_IP, TCP_PORT))      # lakukan bind
s.listen(1)                     # server akan listen menunggu hingga ada koneksi dari client

# import data from txt
fo = open("db.txt", "r") #opens the file in read mode
NIK = fo.read().split(',')
fo.close()
# lakukan loop forever
while 1:
    # menerima koneksi
    conn, addr = s.accept()
    print("Alamat: ", addr)

    data = json.loads(conn.recv(BUFFER_SIZE)) # retrieve data
    print(data)
    response = {}
    if data['NIKPelapor'] not in NIK:
        response['waktuRespon'] = str(datetime.now())
        response['pesan'] = data['NIKPelapor'] + " tidak valid"
    else:
        response['waktuRespon'] = str(datetime.now())
        response['nama'] = data['namaPelapor']
        response['jumlahOrang'] = random.randint(1,10)

    conn.send(json.dumps(response).encode())

# tutup koneksi	
conn.close()
