# Program to compute the distance between two points

x1 = int(input("Enter the x coordinate of point 1 : "))
y1 = int(input("Enter the y coordinate of point 1 : "))

x2 = int(input("Enter the x coordinate of point 2 : "))
y2 = int(input("Enter the y coordinate of point 2 : "))

print("The points entered by you are : ", "(",x1, " , ",y1, ") and ", "(",x2, " , ",y2, ")")

distance = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
didtance = float(distance)

print("The distance between the above two points is : ", distance, " units") 
