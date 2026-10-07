Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
add = lambda a,b:a+b
print(add(10,20))
30
multiply = lambda a,b:a*b
print(multiply(5,4))
20
total = lambda a,b,c:a+b+c
print(total(10,30,50))
90

#lamda with map()
numbers = [1,2,3,4,5]
result = map(lambda num:num*2,numbers)
print(list(result))
[2, 4, 6, 8, 10]

numbers = [ 5,10,15,20]
result = map(lambda num:num+10,numbers)
print(list(result))
[15, 20, 25, 30]

a = [1,2,3]
b = [10,20,30]
result = map(lambda a,b:a+b,a,b)
print(list(result))
[11, 22, 33]

#lambda with filter()
numbers = [1,2,3,4,5,6]
results = filter(lambda num: num%2==0,numbers)
print(list(result))
[]
numbers = [1,2,3,4,5,6]
results = filter(lambda num: num%2 == 0,numbers)
SyntaxError: multiple statements found while compiling a single statement
numbers = [1,2,3,4,5,6]
result = filter(lambda num: num%2 == 0,nuumbers)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    result = filter(lambda num: num%2 == 0,nuumbers)
NameError: name 'nuumbers' is not defined. Did you mean: 'numbers'?
numbers = [1,2,3,4,5,6]
result = filter(lambda num: num%2 == 0,numbers)
SyntaxError: multiple statements found while compiling a single statement
>>> numbers = [1,2,3,4,5,6]
>>> result = filter(lambda num: num%2 == 0,numbers)
>>> print(list(result))
[2, 4, 6]
>>> 
>>> numbers = [5,12,8,20,15,3]
>>> result = filter(lambda num:num>10,numbers)
>>> print(list(result))
[12, 20, 15]
>>> 
>>> #lambda as a key in sorted()
>>> 
>>> names = ['lawrence','john','alex','christopher']
>>> result = sorted(names,key=lambda name:len(name))
>>> print(result)
['john', 'alex', 'lawrence', 'christopher']
>>> 
>>> #lambda with functools.reduce()
>>> from functools import reduce
>>> numbers = [1,2,3,4,5]
>>> result = reduce(lambda a,b:a+b,numbers)
>>> print(result)
15
>>> numbers = [1,2,3,4]
>>> result = reduce(lambda a,b:a*b,numbers)
>>> print(result)
24
