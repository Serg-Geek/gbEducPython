

nam = {}
with open("/home/user/Python/gbEducPython/Phonebook/model/name.txt", "r") as data:
    # a_nam = data.readline()# get str
    for line in data:
        key, *value = line.split('.')
        nam[key] = value
print(nam)
