n = int(input("Enter the range of number"))
tot = 0
for i in range(1,n+1):
    if i%2==0:
        print(i)
        tot = tot + i
print("Sum of even Numbers from 1 to {0} = {1}".format(i,tot))