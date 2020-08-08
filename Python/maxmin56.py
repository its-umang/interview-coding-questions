def maxmin(x1, x2):
    x1, x2 = str(x1), str(x2)
    mx1, mix1, mx2, mix2 = [], [], [], []
    for i in range(len(x1)):
        if(x1[i] == '5'):
            mx1.append('6')
            mix1.append(x1[i])
        elif(x1[i] == '6'):
            mx1.append(x1[i])
            mix1.append('5')
        else:
            mx1.append(x1[i])
            mix1.append(x1[i])
    for i in range(len(x2)):
        if(x2[i] == '5'):
            mx2.append('6')
            mix2.append(x2[i])
        elif(x2[i] == '6'):
            mx2.append(x2[i])
            mix2.append('6')
        else:
            mx2.append(x2[i])
            mix2.append(x2[i])
    maxsum = int(''.join(mx1)) + int(''.join(mx2))
    minsum = int(''.join(mix1)) + int(''.join(mix2))
    print(maxsum , " " , minsum)

if __name__ == "__main__":
    x1 = 546
    x2 = 555
    maxmin(x1, x2)