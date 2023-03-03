print("===========================================================")
print("|--------------------- Skintific Home --------------------|")
print("===========================================================")

varskintific = ["Barrier Repair", "Glowing Set", "Acne Set", "Retinol Set"]
pricelist = [475000,350000,375000,350000]

while True:
  
    print("Pilihan Admin : ")  
    print("1. Tambah varian Skintific")
    print("2. Hapus varian tertentu")
    print("3. Tambah varian di index tertentu")
    print("4. Mengcopy varian Skintific")
    print("5. Menghitung varian")
    print("6. Menggabung varian Skintific dengan pricelist")
    print("7. Membalikkan varian dan juga harga")
    print("8. Melihat varian ada di index berapa")
    print("9. Mengurutkan varian sesuai abjad")
    print("10.Membersihkan semua varian")

    pilihan = input ("Pilih opsi yang Anda inginkan : ")

    
    if pilihan == "1":
        print(varskintific)
        print(pricelist)
        varian = input("Varian yang ingin ditambah : ")
        price = input("Harga varian yang ditambah : ")
        varskintific.append(varian)
        pricelist.append(price)
        print(varskintific)
        print(pricelist)
        print()
        kembali = input("Ingin kembali? : y/n : ")
        if kembali == "y":
            print()
        elif kembali == "n":
            exit()
            
    elif pilihan == "2":
        print(varskintific)
        print(pricelist)
        index1 = int(input("Index varian Skintific yang ingin dihapus : "))
        index2 = int(input("Index harga varian yang dihapus : "))
        varskintific.pop(index1)
        pricelist.pop(index2)
        print(varskintific)
        print(pricelist)
        kembali = input("Ingin kembali? : y/n : ")
        if kembali == "y":
            print()
        elif kembali == "n":
            exit()

    elif pilihan == "3":
        print(varskintific)
        print(pricelist)
        indexA = int(input("Masukkan index : "))
        varian = input("Varian yang ingin ditambah : ")
        price = input("Harga varian : ")
        varskintific.insert(indexA,varian)
        pricelist.insert(indexA,price)
        print(varskintific)
        print(pricelist)
        print()
        kembali = input("Ingin kembali? : y/n : ")
        if kembali == "y":
            print()
        elif kembali == "n":
            exit()
    
    elif pilihan == "4":
        varskintific.copy()
        pricelist.copy()
        print(varskintific)
        print(pricelist)
        print()
        kembali = input("Ingin kembali? : y/n : ")
        if kembali == "y":
            print()
        elif kembali == "n":
            exit()

    elif pilihan == "5":
        varian = input("Masukkan varian : ")
        x = varskintific.count(varian)
        print(x)
        kembali = input("Ingin kembali? : y/n : ")
        if kembali == "y":
            print()
        elif kembali == "n":
            exit()

    elif pilihan == "6":
        l = 0 #sebagai indexing untuk print pricelist
        c = 1 #untuk numbering
        for q in varskintific: #menampilkan varian dan harga
            print(f'{c}. {q} dengan harga: {pricelist[l]}')  
            c += 1 
            l += 1
        varskintific.extend(pricelist)
        print(f"Setelah diextend : {varskintific}")  #biar bisa memasukkan variable dlm str
        kembali = input("Ingin kembali? : y/n : ")
        if kembali == "y":
            print()
        elif kembali == "n":
            exit()

    elif pilihan == "7":
        print(f"Sebelum direverse : ")
        print(varskintific)
        print(pricelist)
        varskintific.reverse()
        pricelist.reverse()
        print(f"Setelah direverse : ")
        print(varskintific)
        print(pricelist)
        kembali = input("Ingin kembali? : y/n : ")
        if kembali == "y":
            print()
        elif kembali == "n":
            exit()

    elif pilihan == "8":
        varian = input("Masukkan varian : ")
        y = varskintific.index(varian)
        print("Varian ada pada index ke : ")
        print(y)
        kembali = input("Ingin kembali? : y/n : ")
        if kembali == "y":
            print()
        elif kembali == "n":
            exit()

    elif pilihan == "9":
        varskintific.sort()
        for varskintific in varskintific:
            print(varskintific)
        kembali = input("Ingin kembali? : y/n : ")
        if kembali == "y":
            print()
        elif kembali == "n":
            exit()

    elif pilihan == "10":
        varskintific.clear()
        pricelist.clear()
        print(varskintific)
        print(pricelist)
        print()
        kembali = input("Ingin kembali? : y/n : ")
        if kembali == "y":
            print()
        elif kembali == "n":
            exit()