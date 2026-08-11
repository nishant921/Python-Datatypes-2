# len/sum/min/max/sorted
t = (1,2,3,4,3)

print(len(t))
print(sum(t))
print(min(t))
print(max(t))
print(sorted(t,reverse=True))


# count
print(t.count(3))
print(t.count(22))  #gives zero if no element present


# index
# print(t.index(5))  error
print(t.index(3))  #gives index of first occurence 