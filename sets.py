# Sets
# A set is an unordered collection of items. Every set element is unique (no duplicates) and must be immutable (cannot be changed).
# However, a set itself is mutable. We can add or remove items from it.

# Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.

# Characterstics:
# Unordered
# Mutable
# No Duplicates
# Can't contain mutable data types



# empty set
s=set()
print(s)
print(type(s))

# 1D set or homogenous set as all elements are of same type
s1={1,2,3}
print(s1)

s2={1,2,'nishant',(1,2,3),True,5.2}
print(s2)           


# using type conversion
s3=set([1,2,3,4])
print(s3)

# set can't have mutuable items
# s4={1,2,3,[1,3]}
# print(s4)



# accessing items/silicing
s1={1,2,3,4}
# print(s1[0])  #error set object is not subscriptable means they're unordered so indexing cannot be work

# editing items
# s1[0]=100   error as indexing cannot be work


# Adding new items
s={1,2,3,4}
s.add(5)
print(s)
# multiple items
s.update([1,2,3,4,5,6,7])
print(s)


# deleting items
# del
s={1,2,3,4}
del s
# discard()
s={1,2,3,4,5}
s.discard(5)
s.discard(10) #doesn;t throw error if element not foung
print(s)

# remove
s.remove(3)
print(s)
# s.remove(19)  throw error if element not found

# pop(): delete random items
s.pop()
print(s)

# clear: empty the set
s.clear()
print(s)