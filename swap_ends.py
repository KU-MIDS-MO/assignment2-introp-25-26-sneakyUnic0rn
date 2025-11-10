def swap_ends(L, k):
    ### Replace with your own code (begin) ###
    
    #copy L into a new list
    new_list = L.copy()
    
    #check if k <= 0, the list is empty, if k is larger than half the list
    if k <= 0 or k > len(L)/2 or L == []:
        return new_list, 0
    
    else:
        #splice new_list
        k_front = new_list[:k]
        k_back = new_list[-k:]
        middle = new_list[k:-k]
        
        #do swapping
        new_list = k_back + middle + k_front
        
        return new_list, k
    ### Replace with your own code (end)   ###
