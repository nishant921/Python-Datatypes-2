# Difference between Lists and Tuples
# Syntax
# Mutability
# Speed : tuples are faster then list bcz immutable data types are faster
import time 

L = list(range(1000))
T = tuple(range(1000))

start = time.time()
for i in L:
  i*5
print('List time',time.time()-start)

start = time.time()
for i in T:
  i*5
print('Tuple time',time.time()-start)


# Memory: takes less space compare to list
import sys

L = list(range(1000))
T = tuple(range(1000))

print('List size',sys.getsizeof(L))
print('Tuple size',sys.getsizeof(T))


# Built in functionality: more funnctions in list where tuple has less functionallity
# Error prone: list are more difficult for error prone
# Usability            



# special syntax: tuple unpacking
a,b,c=(1,2,3)
print(a,b,c)

# Notice: others becomes a list, not a tuple.
a,b,*others = (1,2,3,4)
print(a,b)
print(others)

a, *middle, b = (1, 2, 3, 4, 5)
print(a)
print(middle)
print(b)

# swap
a=1
b=3
a,b=b,a
print(a,b)