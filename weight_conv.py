def konversi_berat ():
    berat = int(input("berapa berat anda: "))
    tipe = input("Kg atau Lbs ( k / l ): ")

    if tipe.lower() == "k":
        hasil = round(berat * 2.204623)
        print(f"Berat badan anda adalah {hasil} pounds")

    elif tipe.lower() == "l":
        hasil = round(berat * 0.453592)
        print(f"Berat badan anda adalah {hasil} Kg")