string = input("Enter a word : ")

if(string[0::1]==string[-1::-1]):
    print("The word",string,"is a palindrome")

else:
    print("The word",string,"is not a palindrome")
