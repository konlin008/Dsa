arr=["aman","arnab","anik","souvik"]
print(arr[0])

###Use the len() method to return the length of an array (the number of elements in an array).
print(len(arr)) 

###You can use the for in loop to loop through all the elements of an array.
x=len(arr)
for x in arr:
    print(x) 
    
### You can use the append() method to add an element to an array.   
arr.append("faizan")
print(arr)

###You can use the pop() method to remove an element from the array.
arr.pop(1)
print(arr)

###You can also use the remove() method to remove an element from the array.
arr.remove("faizan")
print(arr)
print(type(arr))

###Removes all the elements from the list
arr.clear()
print(arr)