def all_subset(arr):
    subset = [None]*len(arr)
    helper(arr, subset, 0)

# 0 1 2==len(arr)
# (1)None None
# Back i=1
# Set subset[1] = arr[1]
# i=2
# (2)None 2
# Back i=1
# Back i=0
# Set Subset[0] = arr[0]
# Set Subset[1] = None
# (3)1 None
# i=1 (incremented i)
# Set Subset[1] = arr[1]
# (4)1 2
def helper(arr, subset, i):
    if i==len(arr):
        print(subset)
    else:
        subset[i]=None
        helper(arr, subset, i+1)
        subset[i] = arr[i]
        helper(arr, subset, i+1)


if __name__ == "__main__":
    all_subset([1,2])
    # all_subset([1,2,3])

# Add or not every element: 2^n
# CS Dojo: Facebook Interview Question: https://www.youtube.com/watch?v=bGC2fNALbNU
# Also Think About Iterative Approach