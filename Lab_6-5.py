#Lab_6-5

numbers=[1, 2, 3]
print (numbers)
#List of numbers that fits the future specifications 

if len(numbers)<2:
    print("Error: List does not meet specifications")
if max(numbers)==min(numbers):
    print("Error: List does not meet specifications")
#If statements to keep the user response within the specifications 

print(min(numbers))
print(max(numbers)) 
#Print statements for the highest and lowest numbers in the list 