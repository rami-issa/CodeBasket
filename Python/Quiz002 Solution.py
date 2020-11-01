'''
Created on Mar 28, 2020

@author: ramiissa
'''
  
#Reverse the digits of a given number
def revers_digits(num): 
    global rev_num
    global base_pos 
    rev_num = 0
    base_pos = 1

    if(num > 0): 
        revers_digits((int)(num / 10)) 
        rev_num += (num % 10) * base_pos 
        base_pos *= 10
    return rev_num


#Do the comparison:
for num in range(1000, 10000):
    num_reversed = revers_digits(num)
    if num_reversed == (num*4):
        print ("number is ", num, " the reversed number is ", num_reversed)
