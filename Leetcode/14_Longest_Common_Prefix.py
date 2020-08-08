class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(strs==[]):
            return ""
        # ["flower", "flow", "flight"]
        # n = 4("flow")
        n = min(len(str) for str in strs)
        # total no. of strings l=3
        l = len(strs)
        # Only lowercases allowed keep track
        b = [0]*26
        count = 0
        for i in range(n):
            for k in range(len(strs)):
                # Check for one by one letter for each string and increment the count
                b[ord(strs[k][i])-ord('a')] += 1
            # If the letter doesn't have same value as l
            # means we are missing one character from any of the string
            # else increase the count and reset b[letter] = 0
            # because if "aa" "aa" occurs count = 4 but no. of strings may be 2
            if(b[ord(strs[k][i])-ord('a')] == len(strs)):
                count+=1
                b[ord(strs[k][i])-ord('a')] = 0
            else:
                break
        return strs[0][:count]