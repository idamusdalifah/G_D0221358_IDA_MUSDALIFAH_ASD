list = ['dipa',18,1.58,True]

#perulangan
for i in (list) :
    print(i)

print("===========")

i = 0
while i < len(list) :
    print(list[i])
    i += 1

#mengupdate nilai pada list
list[0] = 'ida'
print(list)

#menghapus nilai pada list
list.remove(18)
print(list)

#menambahkan nilai pada list
list.append('informatika')
print(list)
