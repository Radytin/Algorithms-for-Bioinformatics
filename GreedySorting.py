f = open('Desktop/rosalind_ba6a.txt','r')
fout = open('Desktop/outputSorting.txt', 'w')
line= f.readline().rstrip('\n')
strip_right= line.rstrip(')')
strip_left = strip_right.lstrip('(')
permutation = strip_left.split(' ')

per =[]
for i in permutation:
	per.append(int(i))

def checkpos(index, value):
	if(abs(value) == index + 1):
		return True
	else:
		return False
		 	
def findIndex(index,per_list):
	for i in range(len(per_list)):
		if index + 1  == abs(per_list[i]):
			return i
 	 
def reverse(s_index, e_index, per_list):
	out = per_list[:]
	for i in range(s_index,e_index + 1):
		out[i]= - per_list[e_index - (i - s_index)]
	return out
	
def print_Permutations(per_list):
	out = ""
	for i in per_list:
		if i > 0:
			out += "+"
		out += str(i) + " "
		print("(" + out[:-1] + ")""\n")

 
for i in range(len(per)):
	
	if not checkpos(i, per[i]):
		ind = findIndex(i, per)
		per = reverse(i, ind , per)
		print_Permutations(per)
		
	if per[i] < 0:
 		per[i] =  - per[i]
 		print_Permutations(per)