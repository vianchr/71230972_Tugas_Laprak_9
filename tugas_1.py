#mencari 3 nilai terbaik dari yang paling tinggi
def urutkan(list_angka):
    list_angka.sort()
    ilang=[]
    for i in list_angka:
        if i not in ilang: 
            ilang.append(i)
    balik=ilang[::-1]
    return(balik[0:3])

print(urutkan([1,2,3,4,5,5,5,5,5]))

