'''
Created on Oct 31, 2020

@author: ramiissa
'''
from itertools import permutations 
from operator import itemgetter



''''
This is not final, will be updated
This will be continued
Not final yet
'''
#def validate_start_end_numbers(start_num, end_number):
    
#This function returns array of permutations for the given set of numbers
def get_permutations(start_num, end_num):
    permList = list(permutations(range(start_num, end_num)))
    return permList

def print_results(permList):
    myResult = []
    myTuple = []
    for i in range (len(permList)):
        firstEdge = permList[i][0]+permList[i][1]+permList[i][2]#+permList[i][3]
        secondEdge = permList[i][2]+permList[i][3]+permList[i][4]#+permList[i][6]
        thirdEdge = permList[i][0]+ permList[i][4]+permList[i][5]#+permList[i][8]
        if(firstEdge == secondEdge == thirdEdge):
            myTemp = permList[i]
            myList = list(myTemp)
            resultTotal = "Result = " , thirdEdge
            myList.append(resultTotal)
            myTuple = tuple(myList)
            myResult.append(myTuple)
    
    res = sorted(myResult, key = itemgetter(6))
    for item in res:
        print(item)


#This can be updated to ask user to insert start and end values
#Then validate input values
#
list_permutations = get_permutations(1, 7)
print_results(list_permutations)



