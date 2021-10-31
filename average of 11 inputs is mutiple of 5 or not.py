count=1
sum=0
while count<=11:
    n=int(input("enter weight in kg:"))
    sum=sum+n
    count=count+1
sum=sum/11
print(sum)
if sum%5==0:
    print(sum,"=mutiple of 5")
else:
    print(sum,"is not multiple of 5")
    