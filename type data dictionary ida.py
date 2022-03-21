dictionary ={'dipa':'belajar type data','sumber':'jago ngoding'}

#perulangan
for key in (dictionary):
    print(key,dictionary[key])

#mengupdate nilai pada dictionary
dictionary['dipa'] ='belajar java'
print(dictionary)

#menghapus nilai pada dictionary
dictionary.pop('sumber')
print(dictionary)

#menambahkan nilai pada dictionary
dictionary['data']='belajar java'
print(dictionary)
