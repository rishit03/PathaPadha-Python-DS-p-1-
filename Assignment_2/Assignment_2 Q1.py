print("Amstrong number is a number whose sum of cube of digits is equal to the same number. E.g 153 is an amstrong number\n")

n = int(input("Enter the number : "))

x = 0
y = n

while (y>0):
    i = y%10
    x = x + (i**3)
    y = y//10    #floor division is used. Eg. n was equal to 141, now n = 14

if (x==n):
    print("The number entered is an armstrong number.")

elif(x!=n):
    print("The number entered is not an armstrong number.")
