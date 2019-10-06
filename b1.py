
Pattern ="AAA"
DNA ="TTACCTTAAC GATATCTGTC ACGGCGTTCG CCCTAAAGAG CGTCAGAGGT"

def distanceBetweenPatternAndStrings(Pattern, Dna):

    k= len(Pattern)
    distance = 0 
    for string in DNA:
        HammingDistance = float("inf")
        for i in range(0, len(string)-k+1):
            if HammingDistance > HammingDistance(Pattern, string[i:i+k]):
                HammingDistance = HammingDistance(Pattern, string[i:i+k])
        distance = distance + HammingDistance
        print(distance)
    return distance

def HammingDistance(p, q):
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count

print (distanceBetweenPatternAndStrings(Pattern, DNA))        



