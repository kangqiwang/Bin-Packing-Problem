def firstFit(weight, n, c):
     
    # Initialize result (Count of bins)
    res = 0
     
    # Create an array to store remaining space in bins
    # there can be at most n bins
    bin_rem = [0]*n
     
    # Place items one by one
    for i in range(n):
       
        # Find the first bin that can accommodate
        # weight[i]
        j = 0
        while( j < res):
            if (bin_rem[j] >= weight[i]):
                bin_rem[j] = bin_rem[j] - weight[i]
                break
            j+=1
             
        # If no bin could accommodate weight[i]
        if (j == res):
            bin_rem[res] = c - weight[i]
            res= res+1
    return res
     
# Driver program
weight = [2, 5, 4, 7, 1, 3, 8]
c = 10
n = len(weight)
print("Number of bins required in First Fit : ",firstFit(weight, n, c))
