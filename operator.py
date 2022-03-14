#operator aritmatika

a = 2
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)

#contoh kasus

nama ="saldy ramli(D0217011)"
lama_lembur = 11
gaji_pokok = 1000000
gaji_lembur = 5000
total_gajilembur =lama_lembur*gaji_lembur
gaji_kotor =gaji_pokok + total_gajilembur
pajak = 9/100
potongan = gaji_pokok*pajak 
gaji_bersih = gaji_kotor -potongan

print("nama :",nama)
print("lama_lembur :Rp",lama_lembur)
print("gaji_pokok :Rp",gaji_pokok )
print("total_gajilembur : RP",total_gajilembur)
print("gaji_kotor :Rp",gaji_kotor)
print("pajak :Rp",pajak)
print("potongan :Rp",potongan)
print("gaji_bersih :Rp",gaji_bersih)

#operator penugasan

nilai = 5
nilai += 2
print(nilai)
nilai -= 3
print(nilai)
nilai *= 4
print(nilai)
nilai /= 5
print(nilai)
nilai %= 6
print(nilai)
nilai **= 7
print(nilai) 
nilai //= 2
print(nilai)


#operator perbandingan

nilai1 = 2
nilai2 = 3
print(nilai1 == nilai2)
print(nilai1 != nilai2)
print(nilai1 > nilai2)
print(nilai1 < nilai2)
print(nilai1 >= nilai2)
print(nilai1 <= nilai2)

#operator logika

#and
print("hasil dari true dan false adalah :",True and False)
print("hasil dari False dan True adalah :",False and True)
print("hasil dari False dan false adalah :",False and False)
print("hasil dari true dan true adalah :",True and True)

#or
print("hasil dari true dan false adalah :",True or False)
print("hasil dari False dan True adalah :",False or True)
print("hasil dari False dan false adalah :",False or False)
print("hasil dari true dan true adalah :",True or True)

#not
print("hasil dari false adalah :",not False)
print("hasil dari true adalah :",not True)



