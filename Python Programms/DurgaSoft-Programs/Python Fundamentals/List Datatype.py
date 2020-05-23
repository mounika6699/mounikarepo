#appending the list
list1=[22,33,67,89]
print("The original list elements:",list1)
list1.append(45)
print("The Appended list ",list1)
#replacing the list elements
k=[1,2,3,4,5]
k[1]=10
k[2:]=[21,22,23]
print("The list changes to:",k)
#Adding elements to list
z=k+[14,7,90]
print("The list after adding z:",z)
#deleting the elements
del(z[3])
print("The list after deleting z:",z)
a=[10,20,30,40] #removing the element from the list
a.remove(20)
print(a)
list2=[12.5,14,79,10+5j,"python"]
list2.reverse()
print(list2)