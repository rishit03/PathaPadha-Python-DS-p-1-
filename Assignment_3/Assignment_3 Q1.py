string = input("Enter a string : ")

if(len(string)<2):
    print("\nEmpty string!")

else:
    start = string[0:2]
    end = string[-2:]

    print(start + end)
