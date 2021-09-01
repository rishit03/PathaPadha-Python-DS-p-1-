string = input("Enter a string : ")

if(len(string)>=3):
    if(string[-3:]=="ing"):
        print("new string : ",string + "ly")

    else:
        print("new string : ",string + "ing")

else:
    print(string)
                             
