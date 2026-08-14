# Membership: in, not in
# iteration
d3={'Name':'Nishant','Sem':4,'year':'3rd','Branch':'CS',
    'Subject':{'Maths':99,'IOS':83,'PROG IN C':89}}

print('Nishant' in d3)  #gives false as in dictionary everything is about keys it search for keys
print('Name' in d3)
print('Subject' not in d3)


d3={'Name':'Nishant','Sem':4,'year':'3rd','Branch':'CS',
    'Subject':{'Maths':99,'IOS':83,'PROG IN C':89}}
for i in d3:
    print(i,d3[i])

# isinstance() is a built-in Python function used to check whether an object belongs to a particular data type (or class).
# isinstance(object, class_or_type)
for key, value in d3.items():
    if isinstance(value, dict):
        print(key)
        for sub_key, sub_value in value.items():
            print(f"   {sub_key}: {sub_value}")
    else:
        print(f"{key}: {value}")


# Dictionary Functions
# len/sorted/min/max
# len will give the total no. of keys
print(len(d3))
print(min(d3))
print(max(d3))
print(sorted(d3,reverse=True))


# items/keys/values
# items display all key value pair in tuple
print(d3.items())
print(d3.values())
print(d3.keys())


# update()
# given dict can be update using another dict
d1={1:2,3:5,4:2,7:4}
d2={4:10,7:14}
d1.update(d2)
print(d1)