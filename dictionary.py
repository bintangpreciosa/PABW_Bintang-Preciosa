arsene_lupin = {
    'nama': 'Arsene Lupin',
    'nik': 1234,
    'jenis_kelamin': 'male',
    'tanggal_lahir': '1902-03-23'
}

sherlock_holmes = {
    'nama': 'Sherlock Holmes',
    'nik': 4321,
    'jenis_kelamin': 'male',
    'tanggal_lahir': '1876-08-16'
}

irene_adler = {
    'nama': 'Irene Adler',
    'nik': 6789,
    'jenis_kelamin': 'female',
    'tanggal_lahir': '1884-10-07'
}

orang = [arsene_lupin, sherlock_holmes, irene_adler]

print(orang)

orang = []

for i in range(3):
    nama = input(f"Masukkan nama orang ke-{i+1}: ")
    nik = int(input(f"Masukkan NIK orang ke-{i+1}: "))
    jenis_kelamin = input(f"Masukkan jenis kelamin orang ke-{i+1} (male/female): ")
    tanggal_lahir = input(f"Masukkan tanggal lahir orang ke-{i+1} (format: YYYY-MM-DD): ")
    

    data_orang = {
        'nama': nama,
        'nik': nik,
        'jenis_kelamin': jenis_kelamin,
        'tanggal_lahir': tanggal_lahir
    }
    
    orang.append(data_orang)


print(orang)



orang = [
    {'nama': 'Arsene Lupin', 'nik': 1234, 'jenis_kelamin': 'male', 'tanggal_lahir': '1902-03-23'},
    {'nama': 'Sherlock Holmes', 'nik': 4321, 'jenis_kelamin': 'male', 'tanggal_lahir': '1876-08-16'},
    {'nama': 'Irene Adler', 'nik': 6789, 'jenis_kelamin': 'female', 'tanggal_lahir': '1884-10-07'}
]


nama_dicari = input("Masukkan nama yang ingin dicari: ")


for data in orang:
    if data['nama'].lower() == nama_dicari.lower():
        print(f"Data ditemukan:")
        print(f"Nama: {data['nama']}")
        print(f"NIK: {data['nik']}")
        print(f"Jenis kelamin: {data['jenis_kelamin']}")
        print(f"Tanggal lahir: {data['tanggal_lahir']}")
        break
else:
    print("Data tidak ada")


