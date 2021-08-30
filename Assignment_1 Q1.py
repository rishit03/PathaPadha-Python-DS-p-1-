# Program to swap two numbers by using a third variable

x = 30 #Defining variable x
y = 40 #Defining variable y

print("When it is not swapped : ", "x = ",x, " y = ",y)

z = x
x = y
y = z

print("After it is swapped : ", "x = ",x, " y = ",y)

print("\n\n")


# Program to swap two numbers without using a third variable

x = 40
y = 50

print("When it is not swapped : ", "x = ",x, " y = ",y)

x,y = y,x

print("After it is swapped, ", "x = ",x, " y = ",y)

