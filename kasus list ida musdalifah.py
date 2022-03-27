menu_item = 0
namebarang =[]
while menu_item != 8 :
    print(".....")
    print("1. mencetak list")
    print("2. menambahkan nama barang ke dlam list")
    print("3. menghapus nama barang dalam list")
    print("4. mengubah nama barang dalam list")
    print("5. menampilkan data dalam list")
    print("6. memeriksa data dalam list")
    print("7. mencari index")
    print("8. keluar")
    menu_item = int(input("pilih menu:"))
    if menu_item == 1 :
        barang = 0
        if len (namebarang) > 0 :
            while barang < len(namebarang[barang]):
                print(barang,".",namebarang[barang])
                barang =barang = 1
        else :
            print("kosong:")
    elif menu_item == 2 :
        name = input("masukkan nama :")
        namebarang.append(name)
        print(namebarang)
    elif menu_item == 3 :
        del_name = input("nama barang yang ingin dihapus :")
        if del_name in namebarang :
            item_number = namebarang.index(del_name)
            del namebarang[item_number]
            print(namebarang)
        else :
            print(del_name,"tidak ditemukan")
    elif menu_item == 4 :
        name = input("nama barang yang ingin di ubah :")
        if name in namebarang :
            item_number = namebarang.index(name)
            new_name = input("nama baru :")
            namebarang[item_number]= new_name
            print(namebarang)
        else :
            print(name,"tidak ditemukan")
    elif menu_item == 5 :
        print(namebarang)
    elif menu_item == 6 :
        barang_yang_dicari = input("masukkan barang yang dicari :")
        if barang_yang_dicari in namebarang :
            print("barang ini terdapat pada namebarang")
        elif barang_yang_dicari not in namebarang :
            print("barang ini tidak terdapat pada namebarang")
    elif menu_item == 7 :
        print(namebarang)
        barang_yang_dicari = input("masukkan barang dicari:")
        print(barang_yang_dicari, "berada pada index",(barang_yang_dicari))

print("selamat tinggal")
                    
