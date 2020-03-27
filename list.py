#list
l1=["Ravi", "Ram","Varun"]
L2=[1,2,3,4,5]
L3=[10.2,10.3,9.8]
#we can store any type of data in the list
L4=["Ravi",10,11.2]
print(L4)
print(l1[1])
print(L4[1:2])
print(l1[:2])
print(L2[2:3])
L5=[l1,L2,L3,L4]
print(L5)
print(L5[1][1])#accessing a list from a list

print(L5[0][1])
#using for loop
for i in l1:
    print(i)

#list is mutable.we can make changes in it. we can perform addition, deletion of  elements in a list.
l1[1]="xccc" #replace an element
print(l1)

l1.insert(2,"aBBB") #insertan element
print(l1)

l1.append("xxx") #insert at the end
print(l1)

l1.remove("Ravi")
print(l1)

l1.pop()#last element is deleted
print(l1)

l6=l1.copy() #copy a list to other list 
print(l6)


#concatenation of two lists
l7=[ 'a', 'b','c','d'] 
l8=[1,2,3,4]
l9=l7+l8
print(l9)
 #another way

#for x in l9:
 #   l8.append()
  #  print(l8)

#another way
l7.extend(l8) #concatenation2
print(l7)

#l1.push("vvv")#push attribute is not there in python
#print(l1)

#thisList =["Apple", "Banana", "Cherry"]
#del(thisList[1])#mentioning index is mandatory
#print(thisList)

#del thisList
#print(thisList)
#alll the elements will get deleted

L3.clear()
print(L3)

#creating list using constructor
L1=list(("Apple", "Banana","Cherry"))
print(L1)


print(L1[-3:-1])#using in operator
if "Apple" in L1:
    print("Yes")

print(len(L1)) #no. of elements in the list

L1=[2,4,5,62,7]
L1.reverse()
print(L1)
#print(L1.sort())
L1.sort()
print(L1)
print(L1.index(2))







