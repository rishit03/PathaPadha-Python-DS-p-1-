rows = int(input("Enter the no. of rows for the pattern : "))

for row in range (1,rows):
    for column in range (1,row+1):
        print("*", end=' ')
    print("\n")
        
