num_str=input("enter the number:")
power=len(num_str)
total=sum(int(digit)**power for digit in num_str)
if int(num_str)==total:
    print("armstrong number")
else:
    print("not an armstrong number")