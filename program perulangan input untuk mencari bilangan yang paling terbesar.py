N = int(input("Masukkan jumlah bilangan: "))


MAX = 0
i = 1

while i <= N:
    bilangan = int(input(f"Masukkan bilangan ke-{i}: "))
    
    
    if bilangan > MAX:
        MAX = bilangan
    
   
    i += 1


print(f"Bilangan terbesar adalah: {MAX}")
