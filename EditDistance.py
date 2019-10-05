f = open('Desktop/rosalind_ba5g.txt', 'r')

str1 ="PLEASANTLY"
str2 ="MEANLY"



def editDistance(str1, str2, m , n): 
   
    if m==0: 
         return n     
    if n==0: 
        return m 
   
    if str1[m-1]==str2[n-1]: 
        return editDistance(str1,str2,m-1,n-1) 
  
    return 1 + min(editDistance(str1, str2, m, n-1),    # Insertion 
                   editDistance(str1, str2, m-1, n),    # Deletion 
                   editDistance(str1, str2, m-1, n-1)    # Substitution 
                   ) 



print(editDistance(str1, str2, len(str1), len(str2)))