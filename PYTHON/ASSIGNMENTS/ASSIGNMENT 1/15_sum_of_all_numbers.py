number = int(input("Enter the number"))
sum = 1
temp = 0
while number > 0:
    sum = int(number % 10)
    temp = int(temp+sum)
    number = int(number/10)
print(int(temp))