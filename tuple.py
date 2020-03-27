T1=("xyz",1,10.2)
print(T1)
#tuple is immutable. we can't change anything once it is written.


#T1[1]=2
#print(T1) gives an error

print(T1[2])
print(T1[-1])

t2=tuple(('1','2','3'))
print(t2)

#t2.remove('2') not possible

print(t2.count('2'))
print(t2.index('2'))
