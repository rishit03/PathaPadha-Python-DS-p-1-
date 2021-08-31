n1 = int(input("Enter n1"))
n2 = int(input("Enter n2"))
n3 = int(input("Enter n3"))

if (n1<n2 and n1<n3) :
    if(n2<n3) :
        print("n3 is the greatest")
    if(n2>n3) :
        print("n2 is the greatest")

elif (n2<n1 and n2<n3) :
    if(n1<n3) :
        print("n3 is the greatest")
    if(n1>n3) :
        print("n1 is the greatest")

elif (n3<n1 and n3<n2) :
    if(n2<n1) :
        print("n1 is the greatest")
    if(n2>n1) :
        print("n2 is the greatest")
