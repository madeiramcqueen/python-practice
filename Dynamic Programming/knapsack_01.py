def knapsack01(W,N,v,w):
    # Base case 0 items left or knapsack is full 
    if N == 0 or W == 0:
        return 0
    # if weight of current element is less than or equal to capacity we can 
    # either include or exclude the item. 
    if w[N] <= W:
        return max(v[N]+knapsack01(W-w[N],N-1,v,w),knapsack01(W,N-1,v,w))
    # if weight of current element is greater than the capacity we will
    # not include it thus returning just the ignoring part. 
    else:
        return knapsack01(W,N-1,v,w)