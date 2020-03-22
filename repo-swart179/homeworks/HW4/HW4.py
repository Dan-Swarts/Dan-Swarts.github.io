# CSCI 1133, Lab Section 002, HW 4
# Daniel Swarts, swart179

#==========================================
# Name: remove_the_fact
# Purpose: Given a list of strings, create a new list that has in
# position 0 the number of times “fact” was in the original list and in
# position 1, a list of all other strings in the original list that were
# not “fact”. There can be duplication of strings on the new list.
# Precondition: The list will only contain strings.
# Input Parameter(s)
# my_list: a list containing only strings or the empty list
# Return Value(s)
# -- if the input parameter is an empty list, return a list
# of [0, []]
# -- else return a list with the 0th index position containing the
# number of times “fact” was seen on the list and the 1st
# index position containing the list of the strings that are
# not “fact”. If there are no strings on the list, return
# an empty list in that position.
#============================================
def remove_the_fact(list_of_strings):
    x=0
    my_list = []
    for i in range(0,len(list_of_strings)):
        if type(list_of_strings[i]) == str:
            if list_of_strings[i] == 'fact':
                x += 1
            else:
                my_list.append(list_of_strings[i]) 
    Im_crying_right_now_its_two_AM_on_Tuesday = [x,my_list]
    return Im_crying_right_now_its_two_AM_on_Tuesday

#==========================================
# Name: average_of_ints
# Purpose:
# Precondition: Hint: Answer the question “What must be true prior
# to the call?” Is there a condition that must be true?
# Input Parameter(s)
#
# Return Value(s)
#
#============================================

def average_of_ints(list_of_ints):
    x=0
    my_list = []
    for i in range(0,len(list_of_ints)):
        if type(list_of_ints[i]) == int:
            my_list.append(list_of_ints[i])
    for j in my_list:
        x += j
    if len(my_list) != 0:
        x = (x / len(my_list))
        if (x - 0.5) % 1 == 0: #making sure it rounds up on a 0.5
            x += 0.5
            
        x = int(round(x))
            
    Im_crying_right_now_its_two_AM_on_Tuesday = [x,my_list]
    return Im_crying_right_now_its_two_AM_on_Tuesday

def max_of_lists(l1):
    x='l'
    for i in range(0,len(l1)):
        for j in l1[i]:
            if type(j) == int or type(j) == float:
                if x == 'l':
                    x = j
                else:
                    if j > x:
                        x = j
    if x == 'l':
        x = 0
    return x

def greater_than(list,num):
    if len(list) == 0:
        return False
    u = 'f'
    for i in list:
        if len(i) != 0:
            u = 't'
    if u = 't':        
        for i in list:
            if type(i) == float or type(i) == int:
                if i > num:
                    None 
                else:
                    return False
    return True

def find_biggest(list):
    x='i'
    for i in list:
        if x == 'i':
            x = i
        elif i > x:
            x = i
    return x

def find_index(my_list, element):
    for i in range(0, len(my_list)):
        if element == my_list[i]:
            return(i)

def selection_sort(list1):
    test = []
    for i in range(0,len(list1)):
        if i == 0:
            big_value = find_biggest(list1)
            initial_index = find_index(list1,big_value)
            list1[initial_index],list1[-1] = list1[-1],list1[initial_index]
            for j in range (0,len(list1)-1):
                test.append(list1[j])
        else:
            big_value = find_biggest(test)
            initial_index = find_index(test,big_value)
            list1[initial_index],list1[-1-i] = list1[-1-i],list1[initial_index]
            test[initial_index],test[-1] = test[-1],test[initial_index]
            test.pop(-1)
    return(list1)
