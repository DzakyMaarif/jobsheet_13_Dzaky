def tebak_angka ():
    angka_tebak = 14
    batas = 5
    penghitung = 0

    while penghitung < batas:
        tebakan = int(input("Masukkan angka tebakan anda : "))
            
        if tebakan == angka_tebak:
            print("Selamat tebakan anda benar")
            break
        else:
            print("tebakan anda salah")
            penghitung += 1

    if penghitung == batas:
        print("Maaf tebakan anda masih salah, kesempatan habis")
        


