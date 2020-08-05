# from memory_profiler import memory_usage

# Use of list: 128 bytes
def method2(str):
    b = [0]*128
    for i in range(len(str)):
        b[ord(str[i])]+=1
    count = b.index(max(b))
    # print(b)
    print(chr(count))

# Simple Solution: Use dict/HashMap
def maxChar(str):
    dict = {}
    for i in range(len(str)):
        if(dict.get(str[i])):
            dict[str[i]]+=1
        else:
            dict[str[i]]=1
    count = max(dict, key=dict.get)
    print(dict)
    print(count)

if __name__ == "__main__":
    str1 = 'python'
    str2 = 'java'
    maxChar(str1)
    maxChar(str2)
    method2(str1)
    method2(str2)
    # memory_usage(maxChar)
    # memory_usage(method2)
    pass