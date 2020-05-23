#bytes data Type
x=[10,32,44,89,90]
y=bytes(x)
print(type(y))
print(y[2])
#y[3]=78 Immutable objexDts
for i in x:
    print(i)
#Bytearray Data Type
data=[90,78,99,12,34]
a=bytearray(data)
print(type(a))
a[2]=102
print(a)
for i in a:
    print(i)
#range Data Type
b=range(10)
for i in b:
    print(i)
r=list(range(5,20))
print(r)
y=range(4,15,3) #printing range of elements with difference 3
for i in y:
    print(i)