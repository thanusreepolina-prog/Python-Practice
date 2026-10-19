num=int(input("enter the number:"))
if num<=1:
    print("not a prime number")
else:
    for i in range(2,num):
        if num%i==0:
            print("not a prime number")
            break
    else:
        print("it is a prime number")