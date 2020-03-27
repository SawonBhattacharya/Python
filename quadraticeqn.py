Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=int(input("Enter a number:"))
Enter a number:3
>>> b=int(input("Enter a number: "))
Enter a number: 4
>>> c=int(input("Enter a number: "))
Enter a number: 2
>>> import cmath
>>> d=(b**2)- 4*a*c
>>> sol1=(-b-cmath.sqrt(d))/(2*a)
>>> sol2=(-b+cmath.sqrt(d))/(2*a)
>>> print(sol1)
(-0.6666666666666666-0.47140452079103173j)
>>> print(sol2)
(-0.6666666666666666+0.47140452079103173j)
>>> 