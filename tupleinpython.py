# Tuples: A tuple in Python is similar to a list. The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas we can change the elements of a list.

# In short, a tuple is an immutable list. A tuple can not be changed in any way once it is created.

# Characterstics

# Ordered  (1,2,3) not equal to (2,1,3)
# Unchangeble: immutable  t[0]=22 cannot edit error
# Allows duplicate: 

# Creating a Tuple
# Accessing items
# Editing items:  t[0]=22 cannot edit error
# Adding items:   cannot add items not even function to add like list
# Deleting items: only one case 'del t3': delete overall tuple, cannot delete portion

# Operations on Tuples
# Tuple Functions


t1=()  #empty tuple
t2=(1) #not tuple it take 1 as a int type
t=([1]) # not a tuple its list
print(type(t))
t3=('hello',)  #single elements syntax declaration [use comma otherwise it take as int,string,etc]
t4=(1,2,3,4,5)  #homo
t5=(1,2,3,[2,3],True)  #hetro

t6=tuple("hello")
print(t1,t2,t3,t4,t5,t6)


# Acessing items
# postive/negative index
# slicing
print(t4[0])
print(t4[::-1])
print(t4[-3:-1])
print(t4[-1:3:])
print(t4[-1:3:-1])
print(t5[-2][0])

