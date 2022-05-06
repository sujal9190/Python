year = int(input("Enter the year for check"))
if (year%4==0) and (year%100!=0) or (year%400==0):
    print("This is leap Year")
else:
    print("Not the leap year")