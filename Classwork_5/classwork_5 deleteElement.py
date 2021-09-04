t = (1,2,3,4,5,6)
print(t)

list1 = list(t)

x = int(input("Enter an element to delete : "))

for i in list1:
    if(i==x):
        list1.remove(i)
        break
else :
    print("Item is not in the list")

t2 = tuple(list1)

print("Updated list :",t2)
    


