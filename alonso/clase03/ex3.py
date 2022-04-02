lst1 = ["Joe", "Sarah", "Mike", "Jess", "", "Matt", "", "Greg"]

# 'Mike'
lst1[2]

# 8
len(lst1)

# Type your code here.

newlist = []

for name in lst1:
    if(name != ''):
        newlist.append(name)

print(newlist)
