fo = open('abc.txt', "r+")
print("Name of the file: ", fo.name)
hi = "hellopython is fun for everyone"
fo.write(hi)
str = fo.read(18)
print("the read string is\n", str)
fo.close()