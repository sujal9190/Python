count = 0
num = int(input("Enter The number for check"))
while num !=0:
    num//=10
    count+=1
print("Count of this number is : "+ str(count))