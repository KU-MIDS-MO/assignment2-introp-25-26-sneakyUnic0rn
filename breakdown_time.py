def breakdown_time(seconds):
    ### Replace with your own code (begin) ###
    
    #return -1 if seconds < 0 or if seconds is not an integer
    if not isinstance(seconds, int) or seconds < 0:
        return -1
    
    #return {} for seconds = 0
    elif seconds == 0:
        return {}
    
    #calculate h, m, s
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    
    #prepare a dictionary
    time = {}
        
    #only add non 0 entries
    if h != 0:
        time[3600] = h
    if m != 0:
        time[60] = m
    if s!= 0:
        time[1] = s
        
    #return the final result
    return time
    
    ### Replace with your own code (end)   ###
