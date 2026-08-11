# zip() in tuple
t=(1,2,3,4)
t2=(1,2,3,4)
t1=zip(t,t2)
print(t1)
print(list(t1))
print(tuple(t1))



print(tuple(t1))
# Why is tuple(t1) empty after list(t1)?

# Because zip is an iterator, and iterators can be used only once.


# Create zip() again if you want both:

t = (1, 2, 3, 4)
t2 = (1, 2, 3, 4)

t1 = zip(t, t2)
print(list(t1))

t1 = zip(t, t2)   # create again
print(tuple(t1))