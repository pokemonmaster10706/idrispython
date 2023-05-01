largest = None
smallest = None
while True :
    num = input("enter a number: ")
    if num == "done" :
        break
    try :
        num = int(num)
        if smallest is None :
            smallest = num
        if largest is None :
            largest = num
    except :
        print("Invalid input")
        continue
    if largest < num :
        largest = num
    if smallest > num :
        smallest = num
print("   ")
print("Maximum is", largest)
print("Minimum is", smallest)
