s='hello_python'
print("The string is:",s)
print("The first letter of string",s,"is",s[0])
print("The sixth letter of string",s,"is",s[5])
print("The last letter of string",s,"is",s[-1])
#invalid slicing s[40](out of range)
print(s[1:40])#prints till last element
print(s[1:]) #prints till last element 
print(s[:5])#prints from sstarting to 4th index element(does not include 5th index element )
print(s[:])#prints complete  string
x=s*3
print("The multiplication of string",s,"3 times is",x)
print("The length of string is",len(s))