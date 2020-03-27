l=[]
count=0
for i in range(1,51):
    l.append(i)
a=int(input())
for i in l:
    if(i!=a and i%a==0):
        count+=1
print(count)           
