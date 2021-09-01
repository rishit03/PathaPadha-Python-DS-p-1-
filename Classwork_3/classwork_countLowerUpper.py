string = input("Enter a word or sentence : ")

lower = 0
upper = 0

for i in string:
    if(i.islower()):
        lower = lower+1
    elif(i.isupper()):
        upper = upper+1
        
print("The no. of lowercasr letters are : ", lower)
print("The no. of uppercase letters are : ", upper)
