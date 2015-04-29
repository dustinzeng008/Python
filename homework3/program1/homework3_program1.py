def bunnyEars2(number):
    if(number==0):                     #if 0 bonny then return 0
        return 0
    elif(number%2==0):                 #if odd bonnies then plus 2
        return 3 + bunnyEars2(number-1)
    else:                              #if even bonnies then plus 3
        return 2+bunnyEars2(number-1)

# output
print("bunnyEars2(0) -> "+str(bunnyEars2(0)))
print("bunnyEars2(1) -> "+str(bunnyEars2(1)))
print("bunnyEars2(2) -> "+str(bunnyEars2(2)))
print("bunnyEars2(3) -> "+str(bunnyEars2(3)))
