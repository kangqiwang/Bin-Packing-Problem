def worstFit( weight, n, c):
 
 
    # Initialize result (Count of bins)
    res = 0
 
    # Create an array to store remaining space in bins
    # there can be at most n bins
    bin_rem = [0 for i in range(n)]
     
    # Place items one by one
    for i in range(n):
     
        # Find the best bin that can accommodate
        # weight[i]
 
        # Initialize maximum space left and index
        # of worst bin
        mx,wi = -1,0
 
        for j in range(res):
            if (bin_rem[j] >= weight[i] and bin_rem[j] - weight[i] > mx):
                wi = j
                mx = bin_rem[j] - weight[i]
             
 
        # If no bin could accommodate weight[i],
        # create a new bin
        if (mx == -1):
            bin_rem[res] = c - weight[i]
            res += 1
         
        else: # Assign the item to best bin
            bin_rem[wi] -= weight[i]
     
    return res
 
# Driver program
weight = [ 2, 5, 4, 7, 1, 3, 8 ]
c = 10
n = len(weight)
print(f"Number of bins required in Worst Fit : {worstFit(weight, n, c)}")
