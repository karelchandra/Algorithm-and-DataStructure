# assignment_2_2004
# Name: Karel Chandra, Student Id: 30373867
import math
import random

# q1
def count_encounters(target_difficulty, monster_list):
    '''
    This function will take in a tuple and will return
    the possible combinations of monster based on the target
    difficulty. First the function will check for empty monster
    list. If it is not empty then it will create a memo which
    in the 2D-array format, then it will be filled with every
    possible target_diffifculty. In each iteration it will checks
    for the previous row / col. In the end it will returns the
    combination of that particular target_difficulty.
    Input: target_difficulty = 15,
    monster_list = [("bear", 5), ("imp", 2), ("kobold", 3), ("dragon", 10)]
    Output: maximum combination of the target_list/ Integer
    Time complexity: O(DM) where D is the number of target difficulty
    and M is the len of monster_list. The first double loop is to
    assigned 2d array. Then the second double loop is to insert the
    values into the array.
    Space complexity: O(DM) where D is the number of target difficulty
    which is represented as column and M is the number of tuples,
    represented as rows of the 2d array.
    This function is sourced from: Lim Wern Han youtube video,
    2004 lecture slides, geeksforgeeks coin change problem
    '''
    # To check for invalid input
    if monster_list == []:
        return ValueError("The list is empty")
    else:
        # if it is valid then use loop to insert values
        
        # initialize 2d array
        rows, cols = (len(monster_list), target_difficulty+1)
        memo = [[0]*cols]*rows
        
        # base case when difficulty == 0 returns 1 combination for empty list
        for i in range(rows):
            memo[i][0] = 1
            
        # this double loop is use to fill in the 2d array with every possible combination
        for _ in range(len(monster_list)):
            for j in range(1, target_difficulty+1):
                if _ >= 1:
                    exclude = memo[_][j]
                else:
                    exclude = 0
                include = 0
                # checks if there are still possible combination
                if j - monster_list[_][1] >= 0:
                    balance = j - monster_list[_][1]
                    include = memo[_][balance]
                else:
                    include = 0
                # update the value of MEMO
                memo[_][j] = exclude + include
        # returns the combination corresponnding to the target_difficulty    
        return memo[len(monster_list)-1][target_difficulty]
    

# q2
def best_lamp_allocation(num_p, num_l, probs):
    '''
    This function is created to find the maximum choice of
    combination of lamps and plants through, counting the
    probability of each plants with given number of lights.
    First we initialize the 2d array, here the row and column
    depennds on num_p for row and num_l for col. Then we multiply
    the probability from 0 lamp till num_l and from 0 plant till
    num_p. Then we input the max choice of probability into the
    array.
    Input: Num_l for total number of light use, num_P for total
    number of plats use, probs is the list of all probabilities.
    Output: Maximum probability that can be achieved from the list. / Floats
    Time complexity: O(PL^2) where here p is the number of plants
    and L is the number of lights. Here the loop is a combination of
    nested and single loop. L^2 here is the nested loop where
    one plant will check for every possible lights.
    Space-complexity is O(PL) where an 2d array is created from P number
    of plants and L number of lights.
    Code referenced from: Lim Wern Han youtube vide, and lecture notes.
    '''
    # initialize 2d array
    cols,rows = (num_l+1,num_p)
    memo = [[0]*cols]*rows
    # defining base case
    memo[0][0] = probs[0][0]
    # start of combination loop of P*L^2
    # fill the 2d array with values
    for _ in range(num_p):
        for j in range(1,num_l+1):
            # to find max on the row
            if _ == 0:
                exclude = memo[_][j-1]
                include = probs[_][j]
                if exclude >= include:
                    memo[_][j] = exclude
                else:
                    memo[_][j] = include
            else:
                if j > 1:
                    exclude = memo[_-1][j-1]
                    for k in range(j,num_l+2):
                        # max column of num_l
                        if k > num_l+1:
                            break
                        else:
                            include = probs[_][k-1]
                            # store temporary variable in balance
                            balance = exclude*include
                            # add the maximum to the corresponding row and col
                            memo[_][j] = balance
    # return the optimal probability combination of lamp and plant                        
    return memo[num_p-1][num_l]
            