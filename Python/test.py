def lengthOfLongestSubstring(s):
    n = len(s)
    list = []
    i, j, max_len = 0, 0, 0
    new_i,new_j=0,0
    while(i<n and j<n):
        if(not s[j] in list):
            list.append(s[j])
            j+=1
            if(j-i>max_len):
                new_i=i
                new_j=j
            print(new_i, new_j)
            max_len = max(max_len, j-i)    
        else:
            i=max(i+1,list.index(s[j])+1)
            # j+=1
            list.pop()
        # print(list)
    print(max_len)
    print(s[new_i:new_j])
    # return max_len

if __name__ == "__main__":
    str="pwwkew"
    lengthOfLongestSubstring(str)