n = int(input("Enter the number : "))

sum = 0
x = n

while(x>0):
    y = x%10
    sum = sum + y
    x = x//10

print("The sum of the digits of the number entered is : ",sum)
    
