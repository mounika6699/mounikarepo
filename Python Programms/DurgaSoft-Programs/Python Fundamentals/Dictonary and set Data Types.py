#dictonary
data={"name":"Jhon","Age":24,2:"M","list1":[1,2,3],"value":True,"list2":[[2,3,4],[7,8,9,10]]}
print(data["name"])
print(data["Age"]) #python is case sensitive
print(data["list1"])
print(data[2])
print(data["list1"][0])
print(data["list2"][1][2])
print(data.keys())
print(data.values())
print(data.items())
print(data)
#sets
z={1,2,3,7,7,99,11,99}
print(z)
#z[2] Set ojects does not support indexing
y=z.add(29)
print(z)
z.remove(7)
print(z)
