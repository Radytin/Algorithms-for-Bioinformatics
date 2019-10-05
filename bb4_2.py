f = open('Desktop/rosalind_ba5c.txt', 'r')

v="AACCTTGG"
w="ACACTGTGA"



def LCSBTCK(v, w):
    
    m=len(v)+1
    n=len(w)+1
    BTCK=[[0 for x in range(m)]for y in range(n)]
    s=[[0 for x in range(m)]for y in range(n)]
    for i in range(n):
        s[i][0]= 0
        BTCK[i][0] = 0
    for j in range(m):
        s[0][j] = 0
        BTCK[0][j] = 1
    for i in range(1,len(w) + 1):
        for j in range(1,len(v) + 1):
            if v[j-1] == w[i-1]:
                f=1
            else:
                f=0
            s[i][j] = max(s[i-1][j], s[i][j-1], s[i-1][j-1] + f)
            if s[i][j] == s[i-1][j]:
                BTCK[i][j] = 0
            if s[i][j] == s[i][j-1]:
                BTCK[i][j] = 1
            if s[i][j] == s[i-1][j-1] + 1 and f == 1:
                BTCK[i][j]= 2
    return(BTCK)

def OUTPUT(BTCK, v, j, i):
    ans = ""
    while(i != 0 or j != 0):
        if BTCK[i][j] == 0:
            i -= 1
        else:
            if BTCK[i][j] == 1:
                j -= 1
            else:
                ans = ans + str(v[j-1])
                i -= 1
                j -= 1
    print(ans[::-1])

b=LCSBTCK(v,w)
OUTPUT(b,v,len(v),len(w))