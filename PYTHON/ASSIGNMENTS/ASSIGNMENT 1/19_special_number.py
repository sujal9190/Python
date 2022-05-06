number = int(input("Enter the number"))
tpnum = f = number 


temp1 = 0
temp2 = 1
while number>0:
    add = int(number%10)
    temp1 = int(temp1+add)
    number = int(number/10)
while tpnum>0:
    mul = int(tpnum%10)
    temp2 = int(temp2*mul)
    tpnum = int(tpnum/10)
final = temp1 + temp2
if f == final:
    print("This is special number")
else:
    print("not special number")