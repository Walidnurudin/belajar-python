data = {
    "name": "walid",
    "age": "19",
    "hobby": "football"
}

# add
data['city'] = "indramayu"

# delete
del data["age"]

# edit
data['name'] = "walid nurudin"

print(data)
# {'name': 'walid nurudin', 'hobby': 'football', 'city': 'indramayu'}

# loop
for key, value in data.items():
    print(key + "-" + value)

# nested
banyak = {
    1: {
        "nama": "a",
        "kota": "aaa"
    },
    2: {
        "nama": "b",
        "kota": "bbb"
    }
}

for key, value in banyak.items():
    print("key = ", key)
    for key2 in value:
        print(value[key2])

# key =  1
# a
# aaa
# key =  2
# b
# bbb