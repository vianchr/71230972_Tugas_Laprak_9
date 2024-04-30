filename = input("nama file: ")
handle = open(filename,"r")
baca=handle.read()
pisah=baca.split(" ")
unik=[]
for i in pisah:
    if i !="\n":
        unik.append(i)
print("================ Isi Berita ===========")
print (baca)
print()
print()
print ("=============== Kata Unik ============")
print (unik)


