#Converting different Data Types into Complex
a=10
b=complex(10)
c=complex(10.5)
d=complex(True)
e=complex(False)
f=complex("10")
g=complex("10.5")
print("The complex form of integer",a,"is :",b)
print("The complex form of float number 10.5",b)
print("The complex form boolean type True and False is:",d,"and",e)
print('''The complex form of strings "10" and "10.5" are''',f,"and",g,"respectively")
x=complex(2,-3)
print("The complex form of 2,-3 is:",x)
#complex("ten") cannot be converted into complex
y=complex(True,False)
print("The complex form of boolean values True and False is:",y)
