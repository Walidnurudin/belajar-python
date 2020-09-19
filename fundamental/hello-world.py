"""
Belajar bahasa python
(ini komentar)
"""

# VARIABEL
nama = 'walid nurudin '
_kelas = input("masuk kelas apa? ")
print(nama + _kelas)

# string
print('Walid\nNurudin')
print('Walid\tNurudin')
print('\'Walid\'')

# methods string
print(nama.capitalize()) # Walid nurudin
print(nama.replace('i', 'e')) # waled nuruden

# number
x = 10
y = 20
print(x * y)

# methods number
print(max(x, y)) # 20
print(min(x, y)) # 10
print(round(8.14)) # 8
print(round(8.70)) # 9

import math
print(math.pi) # 3.14

# string & number
print(nama, x) # walid nurudin 10
print(nama + str(x)) # walid nurudin10

s = '5'
print(x + int(s)) # 15