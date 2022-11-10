#Lab_6-8

input1=int(input('Input Number 1: '))
input2=int(input('Input Number 2: '))
input3=int(input('Input Number 3: '))
input_list=[input1, input2, input3]
#user list of inputs and the list of them

if input1 %2 == 0 and input2 %2 == 0 and input3 %2 == 0:
    print("Even")
elif input1 %2 != 0 and input2 %2 != 0 and input3 %2 != 0:
    print('Odd')
else: print('Mixed')
#making conditional statements on whether the numbers are even, odd, or mixed by dividing the integers