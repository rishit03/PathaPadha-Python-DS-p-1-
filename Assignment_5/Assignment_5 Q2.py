list1 = []
x = []

for i in range(7):
    n = int(input("Enter the number : "))
    x.append(n)
        
for j in x:
    if j not in list1:
            list1.append(j)

print(list1)
