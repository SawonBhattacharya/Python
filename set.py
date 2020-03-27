#unordered collection of elements
s1={"apple", "banana", "cherry"}
print(s1)


s2=set(("apple",'x',2))
print(s2)
#elements do not have any index in set
#print(s1[1]) gives an error
#set does not display duplicate values

s3={1,3,3}
print(s3)

for i in s1:
    print(i)

s1.add("kiwi")#anywhere in the set
print(s1)

s1.remove("apple")
print(s1)#if apple is not present in set,it generates an error

s1.discard("banana")
print(s1) #does not generate any error, discards it if it is present.

s1.discard("melon")
print(s1)

s1.clear()#clears all the members
print(s1)

#combine two sets
s1={"apple","cherry"}
s1.update(s2)
print(s1)

#union of two sets
s1={"apple","tartaric", "let"}
s2={"tan","man","lan"}
s3=s1.union(s2)
print(s3)

#intersection of two sets
s1={1,2,3}
s2={2,3,4}
s3=s1.intersection(s2)
print(s3)

#difference
s3=s1.difference(s2)
print(s3)

s3=s1-s2
print(s3)
