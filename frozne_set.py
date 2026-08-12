# Frozen set is just an immutable version of a Python set object

f1=frozenset([1,2,3,4])
f2=frozenset([2,3,5,6])
print(f1)
print(f1|f2)
print(f1.intersection(f2))
print(f1.union(f2))


# 2d frozne set
f3=frozenset([1,2,3,frozenset([3,4,5])])
print(f3)