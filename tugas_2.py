def input_user(a):
    list_angka=[]
    while True:
        angka=(input("masukan angka (ketik done ketika selesai): "))
        if angka.lower() == "done":
            break
        else:
            try:
                angka=int(angka)
                list_angka.append(angka)
            except:
                print ("masukan angka")
                
    if len(list_angka)<2:
        return ("jumlah inputan tidak sesuai ketentuan(masukan lebih dari 2 angka)")    
    return (f"{max(list_angka)} adalah nilai maksimal\n{min(list_angka)} adalah nilai minimal")
print(input_user(input))
    