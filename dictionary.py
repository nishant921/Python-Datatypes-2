# Dictionary: Dictionary in Python is a collection of keys values, used to store data values like a map, which, unlike other data types which hold only a single value as an element.

# In some languages it is known as map or assosiative arrays.

# dict = { 'name' : 'nitish' , 'age' : 33 , 'gender' : 'male' }

# Characterstics:

# Mutable
# Indexing has no meaning
# keys can't be duplicated
# keys can't be mutable items


# Empty dictionary
d={}
print(type(d))

# 1D dictionary/homogenous dictionary
d1={'name':'nishant', 'Gender':'Male', 'Year':'third'}
print(d1)


# mixed dictionary with immuatable types
d2={'name':'nishant',(1,2,3):'nish'}
print(d2)

# 2d dictionary
d3={'Name':'Nishant','Sem':4,'year':'3rd','Branch':'CS',
    'Subject':{'Maths':99,'IOS':83,'PROG IN C':89}}
print(d3)


# using sequence and dict function
d4=dict([('Name','NISHANT'),('AGE',20),('GENDER','M')])
print(d4)


# no duplicate keys: overwritten by latest
d5={'Name':'Nishant','Name':'Nish'}
print(d5)


# mutable items as key: key cannot be a mutable data type
# d6={'name':'nishant',[11,2,3]:1}   #throw error
# print(d6)
d7={'name':'nishant',(11,2,3):1}
print(d7)



# Accessing items in dict
# indexing doesn't work

# accessing by using key
d1={'name':'nishant', 'Gender':'Male', 'Year':'third'}
print(d1['name'])

# get()
print(d1.get('name'))


# Adding key-value pair
d1['Age']=20
d1['Weight']=50
print(d1)


# Remove key-value pair

# pop 
d1.pop('Weight') 
print(d1)

# popitem:deletes the last pair
d1.popitem()
print(d1)

# del
# del d1
del d1['name']
print(d1)

# clear
d1.clear()
print(d1)



# 2d dict accessing
d3={'Name':'Nishant','Sem':4,'year':'3rd','Branch':'CS',
    'Subject':{'Maths':99,'IOS':83,'PROG IN C':89}}
print(d3['Subject']['IOS'])
d3['Subject']['CPP']=70
print(d3)

# remove in 2d dict
del d3['Subject']['Maths']
print(d3)

# editing existing elements
d3['Sem']=5
d3['Subject']['CPP']=83
print(d3)