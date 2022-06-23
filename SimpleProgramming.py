!/usr/bin/python3

file = open(r"/home/.../data.dat", "r")
lines = file.readlines()
l = 0
for line in lines:
    z, o = 0, 0
    for char in line:
        if char == "0":
            z+=1
        elif char == "1":  
            o+=1
    if z % 3 == 0 or o % 2 == 0:
        l+=1
file.close()
print(l+"\n")
