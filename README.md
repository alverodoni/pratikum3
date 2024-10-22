# Praktikum 3 - Tipe Data, Variable, dan Operator

Nama : Doni alvero

Kelas : TI.24.A.5

NIM : 312410663

Mata Kuliah : Bahasa Pemograman

## Mencari bilangan terbesar dari bilangan yang diinputkan
Program ini menentukan bilangan terbesar dari serangkaian bilangan yang diinputkan hingga input 0. Program ini menggunakan loop `while` dan kondisi `if` untuk memperbarui nilai terbesar yang ditemukan.

## flowchart program 
![foto](https://github.com/alverodoni/foto/blob/8472fc98ff7df7c0d9037884d7a9a313be90ad9b/Screenshot%202024-10-22%20204047.png)

## kode program python
```python
N = int(input("Masukkan jumlah bilangan: "))


MAX = 0
i = 1

while i <= N:
    bilangan = int(input(f"Masukkan bilangan ke-{i}: "))
    
    
    if bilangan > MAX:
        MAX = bilangan
    
   
    i += 1


print(f"Bilangan terbesar adalah: {MAX}")
```

## penjelasan kode program
`N = int(input("Masukkan jumlah bilangan: "))`

Program meminta pengguna memasukkan jumlah bilangan yang akan diproses.
Input tersebut disimpan dalam variabel `N` dan dikonversi menjadi tipe data integer (bilangan bulat).

`MAX = 0`

Variabel `MAX` diinisialisasi dengan 0.
Variabel ini akan digunakan untuk menyimpan bilangan terbesar yang ditemukan selama proses.

`i = 1`

Variabel `i` diinisialisasi dengan 1.
Ini berfungsi sebagai penghitung atau indeks untuk melacak jumlah iterasi.

`while i <= N:`

Loop akan terus berjalan selama nilai `i` kurang dari atau sama dengan `N`.
Artinya, perulangan akan terjadi sebanyak `N` kali sesuai dengan jumlah bilangan yang diminta pengguna.

`bilangan = int(input(f"Masukkan bilangan ke-{i}: "))`

Dalam setiap iterasi, pengguna diminta memasukkan satu bilangan.
Bilangan tersebut disimpan dalam variabel `bilangan`.

`if bilangan > MAX:`

Program memeriksa apakah bilangan yang baru dimasukkan lebih besar dari nilai `MAX` saat ini.
Jika benar, maka nilai `MAX` diperbarui dengan bilangan tersebut.

`MAX = bilangan`

Jika bilangan yang baru dimasukkan lebih besar dari `MAX`, maka variabel `MAX` diisi dengan nilai bilangan tersebut.

`i += 1`

Setelah setiap iterasi, nilai `i` ditambah 1 agar loop mendekati kondisi berhenti (`i > N`)

`print(f"Bilangan terbesar adalah: {MAX}")`

Setelah semua bilangan dimasukkan dan dibandingkan, program menampilkan bilangan terbesar yang ditemukan dengan mencetak nilai `MAX`.

## hasil kode program
![foto]
