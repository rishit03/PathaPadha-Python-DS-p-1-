l = list(("a","b","c","d"))

x = input("enter an element : ")

for i in range (0, 4):
    if(l[i]==x):
        print("The input is in the list")
        break
else:
    print("It is not in the list")
