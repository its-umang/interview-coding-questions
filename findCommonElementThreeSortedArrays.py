# https://www.youtube.com/watch?v=6M6Wxjyob48&list=PLUg9hRlm7gxR7e9OgtrsqgN7XEyNTZRPK&index=3
# Time Complexity: O(n) Better than O(n^3)
def fCETSA(l1, l2, l3):
    x, y, z = 0, 0, 0
    final = []
    while(x<len(l1) and y<len(l2) and z<len(l3)):
        if(l1[x] == l2[y] and l2[y] == l3[z]):
            final.append(l1[x])
            x, y, z = x+1, y+1, z+1
        elif(l1[x]>l2[y]):
            y+=1
        elif(l2[y]>l3[z]):
            z+=1
        else:
            x+=1
    return final

if __name__ == "__main__":
    l1 = [1, 5, 10, 20, 40, 80]
    l2 = [6, 7, 20, 80, 100]
    l3 = [3, 4, 15, 20, 30, 70, 80, 120]
    print(fCETSA(l1, l2, l3))