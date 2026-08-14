#  {key: values for vars in iterable}

# print 1st 10 numbers and their squares
d1={i:i**2 for i in range(1,11)}
print(d1)

percentage={'nish':91,'nishant':97,'misha':87}
cgpa={key: round(values/9.8,2) for (key,values) in percentage.items()}
print(cgpa)


# using zip
days = ["Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
temp_C = [30.5,32.6,31.8,33.4,29.8,30.2,29.9]
# comprehension
print({i:j for (i,j) in zip(days,temp_C)})
# dict()
print(dict(zip(days,temp_C)))

# using if conditon
products = {'phone':10,'laptop':0,'charger':32,'tablet':0}
print({key:value for (key,value) in products.items() if value>0})

# # Nested Comprehension
# print tables of number from 2 to 4

print({i:{j:i*j for j in range(1,11)} for i in range(2,5)})