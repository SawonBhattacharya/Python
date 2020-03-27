l=[]
#count=0
for i in range(1,51):
    l.append(i)
#a=int(input())
for i in l:
    if(i%3==0 and i%5==0):
        print("Fizz&Buzz"+str(i))
    elif(i%5==0):
        print("Buzz."+str(i))
    elif(i%3==0):
        print("Fizz."+str(i))
       
           

