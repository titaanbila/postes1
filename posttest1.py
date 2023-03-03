import random #sebagai modul agar bisa terpanggil
list = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(list) #untuk mengacak angka di dalam list

def quickSort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list[0] #pivot untuk mengambil nilai tengah untuk dibandingkan dengan list yg sudah tersedia
        print(f"Pivot : {pivot}")
        l = [x for x in list[1:] if x <= pivot] #variabel l menyimpan nilai x dari list index ke-1 jika x kurang dari pivot 
        g = [x for x in list[1:] if x >= pivot] #
        return quickSort(l) + [pivot] + quickSort(g) 


def mergeSort(list): #sebagai parameter agar bisa dipanggil
    for post_selanjutnya in range(len(list)-1,0,-1): 
        post_max = 0
        for x in range(1,post_selanjutnya+1):
            max_sementara = list [post_max] #variabel baru untuk menyimpan list sementara atau yg telah dipecah
            if max_sementara < list[x]: #jika variabel kurang dari list maka tertambah ke variabel baru
                post_max = x
        list [post_max],list [post_selanjutnya] = list [post_selanjutnya],list[post_max] #cara kerja

def pilihansort():
    print("====== Sort ======")
    print(" 1. Quick Sort ")
    print(" 2. Merge Sort ")
    print("==================")

    pilihan = input("1 atau 2? : ")
    print()
    if pilihan == "1" : #jika pilihan 1 yaitu quicksort
        print(quickSort(list))
        back = input("Kembali? : ")
        if back == "y":
            print()
            pilihansort()
        elif back == "n":
            exit()
    elif pilihan == "2" :
        print('Sebelum disort:', list)
        mergeSort (list)
        print('Setelah disort:',list)
        back = input("Kembali? : ")
        if back == "y":
            print()
            pilihansort()
        elif back == "n":
            exit()

pilihansort()