# functions in set

# len/sum/min/max/sorted

s1={11,2,73,4,5}
s2={1,2,3,4,5}
print(len(s1))
print(min(s1))
print(max(s1))
print(sorted(s1,reverse=True))


# union/update
print(s1.union(s2))

s1.update(s2)  #permanent change s1 by union 
print(s1)
print(s2)


s1={11,2,73,4,5}
s2={1,2,3,4,5}
# intersection/intersection_update
print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1)
print(s2)


# differnece/difference_update
s1={11,2,73,4,5}
s2={1,2,3,4,5}
print(s1.difference(s2))
s1.difference_update(s2)
print(s1)
print(s2)

# symmetric_difference/symmetric_difference_update
s1={11,2,73,4,5}
s2={1,2,3,4,5}
print(s1.symmetric_difference(s2))
s1.symmetric_difference_update(s2)
print(s1)
print(s2)



# isdisjoint/issubset/issuperset
s1={1,2,3,4}
s2={5,6}
print(s1.isdisjoint(s2))
s2={3,4,5,6}
print(s1.isdisjoint(s2))

# issubset
s1={1,2,3,4,5}
s2={2,3,4}
print(s2.issubset(s1))
print(s1.issubset(s2))

# superset
s1={1,2,3}
s2={1,2}
print(s1.issuperset(s2))
print(s2.issuperset(s1))


# copy
s1={1,2,3,4}
s2=s1.copy()
print(s1)
print(s2)