names=['aman','tania','amanat']
print(type(names))
print(names)

# append(): Adds a single element to the end of the list.
names.append('arman')
print(names)
# insert(): Inserts an element at a specific index.
names.insert(1, 'amin')
print(names)

for name in names:
    print(name)

age=[22,87,64,5,97,21,4,54,65]
age.sort()
print(age)