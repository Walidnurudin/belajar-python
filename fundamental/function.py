# function
def say():
    print("Hello world!")

say()

# parameter/argumen
def tambah(a, b):
    print("jumlah", a, "ditambah", b, "adalah", a + b)

tambah(10, 30)

# default parameter/argumen
def kurang(a = 10, b = 10):
    print(a - b)

kurang()

# return
def kali(a, b):
    return a * b

hasil1 = kali(5, 5)
hasil2 = kali(10, 5)

print(hasil1 + hasil2) # 75
print(kali(hasil1, hasil2)) # 1250

# keyword argument
def person(name, age):
    print("nama saya " + name + ", umur saya", age)

person(age = 19, name = "walid")
# nama saya walid, umur saya 19

# *arguments
def nama(*arg):
    for n in arg:
        print(n)

nama('a', 'b', 'c')

# **arguments
def data(**argu):
    for key, value in argu.items():
        print(key + " - " + value)

data(nama = "walid", asal = "indaramayu")