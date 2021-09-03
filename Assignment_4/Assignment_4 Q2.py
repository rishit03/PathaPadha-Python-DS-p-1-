l1 = list((2,5,9,4,3,7,1))

print("Before sorting the list :",l1)

for i in range(0,7):
    for j in range(i+1,7):
        if(l1[i]>l1[j]):
            l1[i],l1[j] = l1[j],l1[i]

print("After sorting the list :",l1)
