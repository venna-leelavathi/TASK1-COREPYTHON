num=int(input("enter a number:"))
order=len(str(num))
sum=0;
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**order
    temp//=10
if num==sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
