#Lab_6-4

classes= ['Geometry', 'Alegbra II', 'Pre Calc']
#List of classes

classes.append('Calc')
print(classes)
#Adding one more class to the list

print(classes[3])
#My method to only print one of the classes

classes.sort()
print(classes)
#Printing the classes in alphabetical order

classes_copy=classes[:]
classes_copy.reverse()
print(classes_copy)
#Copying the first list to a different variable and printing it in reverse order