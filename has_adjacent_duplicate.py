def has_adjacent_duplicate(L):
    ### Replace with your own code (begin) ###
    if len(L) < 2:                  #check if the list has less than 2 elements
        return False
    
    for i in range(len(L) - 1):     #for each element inthe list
        if L[i] == L[i + 1]:        #check if one element is equal to its next element
            return True             #return true
    return False                    #otherwise return false
    ### Replace with your own code (end)   ###