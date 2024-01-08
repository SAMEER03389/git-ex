print("Fibonacci ")
num=int(input("Enter lenght of series: "))
first=0
second=1
print("{}/n{}".format(first,second))
i=0
while i<num-2:
    third=first+second
    print(third)
    first=second
    second=third
    i+=1
