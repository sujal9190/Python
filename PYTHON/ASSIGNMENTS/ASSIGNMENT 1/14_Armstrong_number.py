number = int(input("Enter the number for check"))
result = 0
n = 0
temp = number
while (temp != 0):
    temp = int(temp/10)
    n = n+1

temp = number
while (temp !=0):
    remainder = temp%10
    result = result + pow(remainder,n)
    temp = int(temp/10)
if(result == number):
    print("This is armstrong number")
else:
    print("not armstrong number")