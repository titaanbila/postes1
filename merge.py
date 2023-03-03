def merge_sort(list): #sebagai parammeter agar bisa dipanggil terus
    for post_selanjutnya in range(len(list)-1,0,-1): 
        post_max = 0
        for x in range(1,post_selanjutnya+1):
            max_sementara = list [post_max] #variabel baru untuk menyimpan list sementara atau yg telah dipecah
            if max_sementara < list[x]: #jika variabel kurang dari list maka tertambah ke variabel baru
                post_max = x
        list [post_max],list [post_selanjutnya] = list [post_selanjutnya],list[post_max] #cara kerja

#hasil 
list = [28,37,35,22,19,23,49,55,33,21,39,57]
print('Sebelum disort:', list)
merge_sort (list)
print('Setelah disort:',list)