#Lab_6-3

colors=['Red', 'Orange', 'Yellow', 'Green']
#Making the first list of colors 

colors.extend(['Blue', 'Purple', 'Black'])
print(colors)
#Extending my list of colors 

colors.append('White')
print(colors)
#Using a different function to add one more color

colors.insert(3, 'Light Green')
print(colors)
#Inserting another color into my series of colors ion the third spot

color_copy= colors [:]
print(color_copy)
#Making a copy of the first list

color_copy.remove('Light Green')
print (color_copy)

