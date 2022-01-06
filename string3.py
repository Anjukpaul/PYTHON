def exchange(str):
    return str[-1:] + str[1: -1] + str[:1]
str=input("enter the string:")
print("string after exchange")
print(exchange(str))


