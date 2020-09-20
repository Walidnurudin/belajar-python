# SETS
# item yang tidak punya urutan
# tidak bisa diakses berdasarkan key dan index
# tidak boleh duplikat

huruf = {'a', 'b', 'c', 'd', 'e'}

# add
huruf.add('f')

# remove
huruf.remove('b')

print(huruf)
# {'f', 'e', 'c', 'a', 'd'}

nomor1 = {1, 2, 3, 4, 5}
nomor2 = {4, 5, 6, 7, 8}

print(nomor1 | nomor2)
# {1, 2, 3, 4, 5, 6, 7, 8}

print(nomor1 & nomor2)
# {4, 5}

print(nomor1 - nomor2)
# {1, 2, 3}

print(nomor2 - nomor1)
# {8, 6, 7}

print(nomor1 ^ nomor2)
# {1, 2, 3, 6, 7, 8}