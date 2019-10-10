f = open('Desktop/rosalind_ba6b.txt','r')
perm = f.readline().strip().lstrip('(').rstrip(')').split()
perm =list(map(int, perm))


def breakpoint_count(permutation):
    return sum(map(lambda x,y: x - y != 1, permutation+[len(permutation)+1], [0]+permutation))


breakpoints = breakpoint_count(perm)
print(breakpoints)





