list1 = []
print(list1)
print(type(list[1]))
sum = 0

for i in range(5):
    n = int(input("Enter the number : "))
    list1.append(n)

for j in list1:
    sum += j

print("\nThe list looks like :",list1)

print("\nThe sum of all the elements in the list is :",sum)


