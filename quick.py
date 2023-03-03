ListKu = [[2,3,"4"],2,4,97,{"a":"sd","b":"c",3:5},1,3,"aduh",1,223]
ListKu2 = []
array_int = []

def sor():
    for i in range(len(ListKu)):
        if type(ListKu[i]) == int:
            array_int.append(ListKu[i])
        else:
            ListKu2.append(ListKu[i])

def pt(list, low, high): #Partion
    i = (low-1)
    pivot = list[high]
    for j in range(low, high):
        if list[j] <= pivot:
            i = i+1
            list[i], list[j] = list[j], list[i]

    list[i+1], list[high] = list[high], list[i+1]
    return (i+1)

def qs(l, low, high): #Quick Sort
    if len(l) == 1:
        return l
    if low < high:
        pi = pt(l, low, high)
        qs(l, low, pi-1)
        qs(l, pi+1, high)

sor()
qs(array_int, 0, len(array_int)-1)
print("Sebelum sortir :")
print(ListKu)
print("Setelah sortir :")
print(array_int + ListKu2)