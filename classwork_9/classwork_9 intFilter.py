list1 = [1,2,3,4,5,6,"mango","apple"]

y = filter(lambda x:type(x)==int,list1)

print(list(y))
