def average():
    x = int(input("Enter marks in sub 1 : "))
    y = int(input("Enter marks in sub 2 : "))
    z = int(input("Enter marks in sub 3 : "))

    def sumMarks():
        sum = x+y+z

        print("The sum of marks in 3 subjects is : ",sum)

        return sum

    sumMarks()

    avg = (x+y+z)/3
    avg = float(avg)
    
        
    print("The average marks scored is : ",avg)

average()

