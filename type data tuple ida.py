tuple=('dipa',18,158,False)

#perulangan
for i in (tuple):
   print (i)

print("========")

i = 0
while i < len(tuple) :
    print(tuple[i])
    i += 1

#mengupdate nilai pada tuple dengan cara dikonvensi
    tup=list(tuple)
    tup[0]="data"
    print(tup)
#menghapus nilai pada tuple
    tup.remove(False)
    print(tup)
#menambahkan nilai pada tuple
    tup.insert (2,"dipa")
    print (tup)
