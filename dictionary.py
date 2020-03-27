#consists of elements in key value pair form
car={"Name": "Ravi", "USN": 102 ,"address": "xcf"}
print(car)

print(car["USN"])
print(car.get("USN"))

#updating value
car["USN"]=103
print(car)

for x in car.values():
    print(x)
for x in car:
    print(x)

for x in car.items():
    print(x)
for x,y in car.items():
    print(x,y)


print(len(car))

car["Age"]=23
print(car)
