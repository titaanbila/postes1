import random
list = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(list)

def pilihansort():
    print("====== Sort ======")
    print(" 1. Quick Sort ")
    print(" 2. Merge Sort ")
    print("==================")
    print()

    pilihan = input("1 atau 2? : ")
    if pilihan == "1" :
        print(quickSort(list))
        back = input("Kembali? : ")
        if back == "y" :
            pilihansort()
    elif pilihan == "2" :
        #hasil 
        print('Sebelum disort:', list)
        mergeSort (list)
        print('Setelah disort:',list)


def quickSort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list[0] 
        print(f"Pivot : {pivot}")
        less = [x for x in list[1:] if x <= pivot]
        greater = [x for x in list[1:] if x > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)


def mergeSort(list): #sebagai parammeter agar bisa dipanggil terus
    for post_selanjutnya in range(len(list)-1,0,-1): 
        post_max = 0
        for x in range(1,post_selanjutnya+1):
            max_sementara = list [post_max] #variabel baru untuk menyimpan list sementara atau yg telah dipecah
            if max_sementara < list[x]: #jika variabel kurang dari list maka tertambah ke variabel baru
                post_max = x
        list [post_max],list [post_selanjutnya] = list [post_selanjutnya],list[post_max] #cara kerja

