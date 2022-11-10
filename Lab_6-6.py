#Lab_6-6

inputs= input('input word one: ')
input_2=input('input word two: ') 
input_3=input('input word three: ') 
input_4=input('input word four: ')
input_5=input('input word five: ')
print(inputs, input_2, input_3, input_4, input_5)
#Making five different variables that each have user inputs 

input_list=[inputs, input_2, input_3, input_4, input_5]
print(input_list)
#Making a list out of the variables so when the user makes inputs, it puts it in a list

empty_list=[]
empty_list.append(input_list[0])
empty_list.append(input_list[1])
empty_list.append(input_list[2])
empty_list.append(input_list[3])
empty_list.append(input_list[4])
print (empty_list)
#adding each input to the empty list one at a time

inp_1_len=len(inputs)
inp_2_len=len(input_2)
inp_3_len=len(input_3)
inp_4_len=len(input_4)
inp_5_len=len(input_5)
end_list=[inp_1_len, inp_2_len, inp_3_len, inp_4_len, inp_5_len]
print(end_list)
#making new variables about the length of each list and putting them in a new list