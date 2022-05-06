num = int(input("Enter The number of range"))
tot = 0
for i in range(1,num+1):
    if i%2!=0:
        print(i)
        tot = tot+i
print("The sum of odd numbers from 1 to {0} = {1}".format(i,tot))