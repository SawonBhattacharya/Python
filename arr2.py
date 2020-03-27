import array as arr

a=arr.array('f',[9.9,8.8,7.7])

print("the new create array is: ",end=" ")
for i in range(0,3):
    print(a[i])
print()
a.append(3.3)
print(a.index(9.9))
