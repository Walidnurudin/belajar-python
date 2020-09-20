# LIST
isi = [1, 2, 3, 4]

# tambah
isi.append(5)

# edit
isi[1] = 'kosong'

# hapus
del isi[2]

print(isi)
# [1, 'kosong', 4, 5]

# convert ke tuple
print(tuple(isi))


# TUPLE
# tuple isinya tidak bisa di tambah, edit dan hapus

data = ("satu", "dua", "tiga")

print(data)
# ('satu', 'dua', 'tiga')

# convert ke list
print(list(data))