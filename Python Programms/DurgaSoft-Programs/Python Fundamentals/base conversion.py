#binary conversion
a=bin(15)  #decimal to binary
b=bin(0o11) #octal form to binary
c=bin(0X10) #hexa decimal to binary
print("decimal to binary:",a)
print("octal to binary :",b)
print("Hexa decimal to binary :",c)
#octal conversion
x=oct(10)   #decimal to octal
y=oct(0B1111)  #binary to octal
z=oct(0X123)    #hexa decimal to octal
print("decimal to octal:",x)
print("binary to octal :",y)
print("Hexa decimal to octal :",z)
#hexa decimal conversion
t=hex(100)   #decimal to hexa
r=hex(0B111111) #binary  to hexa
s=hex(0o12345)  #octal to hexa
print("decimal to hexa:",t)
print("binary to hexa :",r)
print("ocal to hexa:",s)
