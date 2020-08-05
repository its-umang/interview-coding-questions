# Subarray with given sum
# Input:
# 5 12
# 1 2 3 7 5
# Output:(1 indexing)
# 2 4 

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, s = list(map(int, input().split()))
        a = list(map(int, input().split()))
        prev=0
        j=1
        curr_sum=a[prev]
        while(j<=len(a)):
            while(curr_sum>s and prev<j-1):
                curr_sum = curr_sum-a[prev]
                prev+=1
                # curr_sum = a[prev]
            if(curr_sum==s):
                print(prev+1, j)
            if(j<len(a)):
                curr_sum = curr_sum+a[j]
            j+=1
        if(curr_sum!=s):
            print(-1)


# 1
# 42 468
# 135 101 170 125 79 159 163 65 106 146 82 28 162 92 196 143 28 37 192 5 103 154 93 183 22 117 119 96 48 127 172 139 70 113 68 100 36 95 104 12 123 134