f = open('Desktop/rosalind_ba5e.txt', 'r')
f2 = open('Desktop/blomsum.txt', 'r')
fout=open('Desktop/output2.txt', 'w')
v=f.readline().replace('\n','')
w=f.readline().replace('\n','')
blom={}
a=f2.readline().replace('  ',' ').replace('\n','').replace('  ','').split(' ')
i=0

def LCS(v, w):
    sc=0
    sigma=5
    global  score
    m=len(v)+1
    n=len(w)+1
    Backtrack=[[0 for x in range(m)]for y in range(n)]
    s=[[0 for x in range(m)]for y in range(n)]
    for i in range(n):
        s[i][0]= -sigma*i
        Backtrack[i][0] = 0
    for j in range(m):
        s[0][j] = -sigma*j
        Backtrack[0][j] = 1
    for i in range(1,len(w) + 1):
        for j in range(1,len(v) + 1):
            f=score[blom[v[j-1]]][blom[w[i-1]]]
            s[i][j] = max(s[i-1][j]-sigma, s[i][j-1]-sigma, s[i-1][j-1] + f)
            if s[i][j] == s[i-1][j]-sigma:
                Backtrack[i][j] = 0
            if s[i][j] == s[i][j-1]-sigma:
                Backtrack[i][j] = 1
            if s[i][j] == s[i-1][j-1] + f:
                Backtrack[i][j]= 2
    fout.write(str(s[len(w)][len(v)])+'\n')
    return(Backtrack)

def OUTPUT(Backtrack, v, j, i):
    ans1 = ""
    ans2 = ""
    while(i != 0 or j != 0):
        if Backtrack[i][j] == 0:
            ans1 = ans1 + '-'
            ans2 = ans2 + str(w[i-1])
            i -= 1
        else:
            if Backtrack[i][j] == 1:
                ans1 = ans1 + str(v[j-1])
                ans2 = ans2 + str('-')
                j -= 1
            else:
                ans1 = ans1 + str(v[j-1])
                ans2 = ans2 + str(w[i-1])
                i -= 1
                j -= 1
    fout.write(ans1[::-1]+'\n')
    fout.write(ans2[::-1])



for symb in a:
    blom[symb]=i
    i=i+1
score=[]
for line in f2.readlines():
    s=line.replace('\n','').replace('  ',' ').split(' ')
    score.append([int(a) for a in s[1:]])
b=LCS(v,w)
OUTPUT(b,v,len(v),len(w))

