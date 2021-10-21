# FIT2004 Assignment 1 2021
# Name: Karel Mackenzie Chandra
# Student Id: 30373867
# Tutor/Lecturer : Lim Wern Han


# Q1 Integer Radix Sort
import math

def num_rad_sort(nums,b):
    """
    This function will take in alist of integers as an input,
    and will sort using radix sort it will output the sorted list.
    First we find the max column by finding the len(max(element)),
    after finding the max column then call the counting_sort_table
    with parameters that is (list, base, and the index). Returns
    the sorted list.
    The input = [4321, 33789, 234, 12], b = 10
    The output = [12, 234, 4321, 33789]
    Big-O complexity time = O((n+b) * logbM), n here is the len of
    the input list and b here is the len of base need in making
    count_array, lastly logbM here is the number of column needed to
    iterate through the elements of the list.
    """
    # This function is referenced from : https://www.cs.helsinki.fi/u/tpkarkka/opetus/13s/spa/lecture03.pdf/pg.41
    if nums == []:
        print("list is empty")
    else:
        # find the max column
        col = math.log(max(nums), b)
    
        # start moving through the columns
        i = 0
        while i < col:
            nums = counting_sort_stable(nums,b,i)   # call counting_sort_table
            i += 1
        return nums
    

def counting_sort_stable(nums,b,i):
    '''
    This is where the sort of radix_sort, first
    implement the count_array by multiplying by b,
    then count the occurence of the element, create
    a position pointer corresponding to the counter,
    create a temporary array to store the sorted list,
    the position here is use to update the characters
    and store it  into the temporary array to be copied
    back to the list.
    Precondition: studio_list have at least 1 item
    Big-O complexity: O(n+b) where here n is the len of
    list and b is the base use to modularize the
    couting_sort.
    Input: unsorted list (same num_rad_sort above as it is part of)
    Output: sorted list (same num_rad_sort above as it is part of)
    '''
    # This function is reference from Course notes by Daniel ANDERSON/pg.29
    # initialize count array
    count_array = [0]*(b)
        
    # loop through the elements of column use base to loop back to 0
    col_index = 0
    for _ in range(len(nums)):
        col_index = (nums[_] // (b**i)) % b
        count_array[col_index] += 1   # count occurence
    
    # initialize position array
    position_array = [0]*(b)
    # add 1 to the first element
    position_array[0] = 1
    
    # set the corresponding index to the position
    for _ in range(1,b):
        position_array[_] = position_array[_ - 1] + count_array[_ - 1]
    
    # initialize output array
    output_array = [0]*(len(nums))
    
    # swap the array based on count_array
    for _ in range(len(nums)):
        col_index = (nums[_] // (b**i)) % b
        output_array[position_array[col_index]-1] = nums[_]  # use the position to swap the element
        position_array[col_index] += 1
    
    # copy the element from the output_array back to the original list 
    for _ in range(len(nums)):
        nums[_] = output_array[_]
    print(nums)
    
    return output_array


# Q2 Timing bases
import time
import random

def base_timer(num_list, base_list):
    """
    This function is to count the speed it takes when a
    list of input is run through the code. The loop will
    run based on the base list, then we initialize timer
    for start & end to calculate the time taken for each
    input.
    Input: num_list, base_list
    Output: time taken for the specific input
    Big-O complexity: O(n) where n is the list of base.
    """
    # This function is referenced from ed discussion on timeit error
    time_list = []
    # iiterate through every base.
    for i in base_list:
        start = time.time() # start timing
        num_rad_sort(num_list,i) # radix sort function call
        end = time.time()   # end timing
        time_taken = end - start # end-start
        time_list.append(time_taken)
    return time_list # return the time taken.

# set of inputs     
random.seed("FIT2004S22021")
data1 = [random.randint(0,2**25) for _ in range(2**15)]
data2 = [random.randint(0,2**25) for _ in range(2**16)]
bases1 = [2**i for i in range(1,23)]
bases2 = [2*10**6 + (5*10**5)*i for i in range(1,10)]


# Q3 Interest Groups
def interest_groups(data):
    """
    This function operates through a tuple, first
    it will checks for empty list if not empty
    then continue. We preprocess the list input
    by ordering the list of like by it's length.
    After preprocessing then padding is added so
    that the index won't go out of range due to
    the different length. After all the radix sort
    we combine the names that have the same like
    element, maintaing the relative order then
    we group and output the list of names.
    Big-O complexity: O(NM), where n is the len
    of list and M = XY, where X is the num of
    like list and Y is the longest string in
    like of list.
    Input: tuple of name and like list
    output: tuple of names in groups
    """
    # This function is a combination of:
    # Q1, https://www.cs.helsinki.fi/u/tpkarkka/opetus/13s/spa/lecture03.pdf/pg.39, tutorial wk3 num 3, num 6  
    # checks if data is empty or not
    if data == []:
        print("The list is empty")
    else:
        # if not initialise array that is going to be temp
        out_array_ll = []
        maxim = 0
        
        # pre process data
        for _ in range(len(data)):
            temp = 0
            maxi = data[_][1]
            for _ in maxi:
                temp += len(_)
            if temp > maxim:
                maxim = temp
        
        # store in temp
        out_array_ll = counting_sort_pre(data,maxim) # call counting_sort_pre
        
        # add padding for like list
        for _ in range(len(data)):
            temp_ll = out_array_ll[_][1]
            for _ in range(len(temp_ll)):
                if len(temp_ll[_]) == len(max(temp_ll)):
                    continue
                else:
                    temp_ll[_] = temp_ll[_] + " "*(len(max(temp_ll)) - len(temp_ll[_]))
        # sort the like list
        out_array_ll = str_rad_sort(out_array_ll,27,1) # Radix sort Like list
        
        # group names that have same interest
        j = 0
        result = [[out_array_ll[0][0]]]
        for _ in range(1,len(out_array_ll)):
            if out_array_ll[_][1] == out_array_ll[_-1][1]:
                result[j].append(out_array_ll[_][0])
            else:
                j += 1
                result.append([out_array_ll[_][0]])
        
        
        # copy back to original array
        out_array_ll = result
        
        # sort the names so they are alphabetically ordered
        maxim = 0
        for _ in range(len(out_array_ll)):
            temp_ll = out_array_ll[_]
            # find maximum length of string
            for _ in temp_ll:
                temp = 0
                temp += len(_)
                if temp > maxim:
                    maxim = temp
            # add padding to the names for radix sort       
            for _ in range(len(temp_ll)):
                if len(temp_ll[_]) == maxim:
                    continue
                else:
                    temp_ll[_] = temp_ll[_] + " "*(maxim - len(temp_ll[_]))
        
        # call radix sort and sort the names
        out_array_ll = str_rad_sort(out_array_ll,27,0)
        
        # remove all unnecessary padding so output would be as expected
        for _ in range(len(out_array_ll)):
            temp_ll = out_array_ll[_]
            for _ in range(len(temp_ll)):
                temp_ll[_]= temp_ll[_].replace(" ", "")
        
        # return the final tuple 
        return out_array_ll

def counting_sort_pre(nums,b):
    '''
    This function is use for pre-processing of tuple
    This is where the sort of radix_sort, first
    implement the count_array by multiplying by b,
    then count the occurence of the element, create
    a position pointer corresponding to the counter,
    create a temporary array to store the sorted list,
    the position here is use to update the characters
    and store it  into the temporary array to be copied
    back to the list.
    Precondition: studio_list have at least 1 item
    Big-O complexity: O(n+b) where here n is the len of
    list and b is the base use to modularize the
    couting_sort.
    Input: unsorted list (same num_rad_sort above as it is part of)
    Output: sorted list (same num_rad_sort above as it is part of)
    Precondition: studio_list have at least 1 item
    '''
    # This function is reference from Course notes by Daniel ANDERSON/pg.29
    # initialize count array
    count_array = [0]*(b+1)
        
    # loop through the elements of column  
    col_index = 0
    for _ in range(len(nums)):
        temp = 0
        maxi = nums[_][1]
        for _ in maxi:
            temp += len(_)
        col_index = temp
        count_array[col_index] += 1
    
    # initialize position array
    position_array = [0]*(b+1)
    position_array[0] = 1
    
    # set the index
    for _ in range(1,b+1):
        position_array[_] = position_array[_ - 1] + count_array[_ - 1]
    
    # initialize output array
    output_array = [0]*(len(nums))
    
    # swap the array based on count_array
    for _ in range(len(nums)):
        strL = nums[_]
        temp = 0
        maxi = nums[_][1]
        for _ in maxi:
            temp += len(_)
        col_index = temp
        output_array[position_array[col_index]-1] = strL  # swap with original
        position_array[col_index] += 1
    return output_array

def str_rad_sort(nums,b,element):
    """
    This function will take in alist of strings as an input,
    and will sort based oon characters using radix sort it will output the sorted list.
    First we find the max column by finding the len(max(string)),
    after finding the max column then call the counting_sort_table
    with parameters that is (list, base, and the index). Returns
    the sorted list.
    The input = [("nuka", ["birds", "napping"]),
        ("hadley", ["napping birds", "nash equilibria"]),
        ("yaffe", ["rainy evenings", "the colour red", "birds"]),
        ("laurie", ["napping", "birds"]),
        ("kamalani", ["birds", "rainy evenings", "the colour red"])]
    The output = [('nuka', ['birds  ', 'napping']),
    ('laurie', ['napping', 'birds  ']),
    ('hadley', ['napping birds  ', 'nash equilibria']),
    ('yaffe', ['rainy evenings', 'the colour red', 'birds         ']),
    ('kamalani', ['birds         ', 'rainy evenings', 'the colour red'])]
    Big-O complexity time = O((n+b) * logbM), n here is the len of
    the input list and b here is the len of base need in making
    count_array, lastly logbM here is the number of column needed to
    iterate through the elements of the list.
    
    """
    # This function is reference from Course notes by Daniel ANDERSON/pg.31
    # find the max length of string column
    output_array = []
    name_array = []
    # radix_name
    if element == 0:
        maxim = 0
        # loop through tuple
        for _ in range(len(nums)):
            count = 0 
            temp = 0
            maxi = nums[_]
            for _ in maxi:
                temp = 0
                temp += len(_)
                if temp > maxim:
                    maxim = temp
                count += 1
            # find max col
            col_ll = maxim -1 

            # loop through the column of like list
            if count == 1:
                output_array.append((maxi))
                continue
            else:
                while col_ll >= 0:
                    temp_ll = counting_sort_stable_str(maxi,b,col_ll) # call counting sort
                    col_ll -= 1
                name = temp_ll
                # store back the element
                output_array.append((name))# call counting sort
        return output_array #print temp
    # radix like list
    else:
        for _ in range(len(nums)):
            name = nums[_][0] # names
            maxi = nums[_][1] # like list
            # find max col
            col_ll = len(max(maxi)) - 1
            
            # loop through the column of like list
            while col_ll >= 0:
                temp_ll = counting_sort_stable_str(maxi,b,col_ll) # call counting sort
                col_ll -= 1
            maxi = temp_ll
            # store back the element
            output_array.append((name,maxi))
        return output_array

def counting_sort_stable_str(nums,b,i):
    """
    This is where the sort of radix_sort, first
    implement the count_array by multiplying by b,
    then count the occurence of the character by finding
    the ascii values of each character, create
    a position pointer corresponding to the counter,
    create a temporary array to store the sorted list,
    the position here is use to update the characters
    and store it  into the temporary array to be copied
    back to the list.
    Precondition: studio_list have at least 1 item
    Big-O complexity: O(n+b) where here n is the len of
    list and b is the base use to modularize the
    couting_sort.
    Input: unsorted list (same num_rad_sort above as it is part of)
    Output: sorted list (same num_rad_sort above as it is part of)
    Precondition: studio_list have at least 1 item
    """
    # This function is reference from Course notes by Daniel ANDERSON/pg.29
    # initialize count array
    count_array = [0]*(b+1) # save space for " "
        
    # loop through the elements of column  
    col_index = 0
    for _ in range(len(nums)):
        alpha = ord(nums[_][i]) - 96  # find the ascii corresponding value to the char
        if alpha < 0:
            col_index = (alpha // (b**i))+ 1 % b # if - value then traverse back to 0
        else:
            col_index = alpha + 1
        count_array[col_index] += 1  # find occurence of character
    
    # initialize position array
    position_array = [0]*(b+1)
    position_array[0] = 1
    
    # set the index
    for _ in range(1,b+1):
        position_array[_] = position_array[_ - 1] + count_array[_ - 1]
    
    # initialize output array
    output_array = [0]*(len(nums))
    
    # swap the array based on count_array
    for _ in range(len(nums)):
        alpha = ord(nums[_][i]) - 96 # find the ascii corresponding 
        if alpha < 0:
            col_index = (alpha // (b**i)) + 1 % b # if - value then traverse back to 0

        else:
            col_index = alpha + 1
        output_array[position_array[col_index]-1] = nums[_] # update the array
        position_array[col_index] += 1
    # return the sorted list
    return output_array
