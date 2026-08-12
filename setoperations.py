# sets operations 
s1={1,2,3,4,5}
s2={4,5,6,7,8}

# union  ( | )
print(s1|s2)

# intersection ( & )
print(s1&s2)

# difference ( - )
print(s1-s2)
print(s2-s1)

# symetric difference ( ^ )
print(s1^s2)
print(s2^s1)


# membership Test : 
# in
print(1 in s2)
print(1 in s1)
print(s2 in s1)
# not in
print(1 not in s1)
print(s2 not in s1)


# loops
for i in s1:
    print(i)