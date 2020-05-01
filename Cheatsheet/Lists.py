#Create List and print 
myList = ['pi', 'prerna', 'appy', 'cat']
# print(myList)

# #Indexed access
# print(myList[2])

# #Negative index -1 gives last element -2 second last and so on
# print(myList[-1])

# #Slicing list to obtain sublists last index is not inclusive
# print(myList[0:4])
# print(myList[1:])
# print(myList[:2])

#creating copy
# copy=myList
# print(copy)
# otherCopy=myList[:]
# print(otherCopy)

#append element

myList.append('3.14')
myList.append('update')
# print(myList)

#Length
# print(len(myList))

#changing elements via indexes
myList[-1]='infinite'
# print(myList[:])

#List Concatenation
# print(myList+[1,2,3])
# myList=myList+['IoT', 'APIs']

#List Replication
# print(myList*3)
# myList=myList*2

print(myList)
# List as : ['pi', 'prerna', 'appy', 'cat', '3.14', 'infinite']

#Removing elements using del
# del myList[0]
print(myList)

#Using for loop with lists
for i, name in enumerate(myList):
    print('Index : {} | Name : {} '.format(str(i),name)) 















