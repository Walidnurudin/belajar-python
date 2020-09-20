# WHILE

count = 1

while count <= 5:
    print("count ke ", count)
    count = count + 1
else:
    print("selesai")


# FOR IN

text = 'python'
orang = ["walid", "nurudin"]

for huruf in text:
    print("huruf ", huruf)

for nama in orang:
    print("nama ", nama)


# NESTED

a = 0

while a <= 5:
    b = 0
    while b < a:
        print("*", end = " ")
        b = b + 1
    print()
    a = a + 1

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

for a in range(1, 6):
    for b in range(1, 6):
        c = a * b
        print(c, end = " ")
    print()

# 1 2 3 4 5 
# 2 4 6 8 10 
# 3 6 9 12 15 
# 4 8 12 16 20 
# 5 10 15 20 25 