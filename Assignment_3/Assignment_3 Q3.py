string = input("Enter a string : ")

print("Old String : ", string)

first = string[0]
last = string[-1]
middle = string[1:-1]

print("New String : ", last + middle + first)
