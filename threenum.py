num=int (input())
a=num//100
print("bai=%d\n"%a)
num-=(a*100)
b=num//10
print("shi=%d\n"%b)
num-=(b*10) #c=num%10
print("ge=%d\n"%num)
print("%d  %d  %d"%(a,b,num))
