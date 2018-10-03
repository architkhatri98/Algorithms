# Make two functions
# One for sorting recursively the other for merging

# Function for merging two lists
# merge (A,B)-> To merge lists A[0:len(A)] and B[0:len(B)]
# We will not change the contents of the lists

def merge(A,B):
	(i,j)=(0,0)
	C = []
	(n,m)=(len(A),len(B))
	while (i+j < m+n):
		if(i==n): # If all elements of A have been merged
			print(i,j)
			print(B[j])
			C.append(B[j])
			j=j+1
		if(j==m): # If all elements of B have been merged
			print(i,j)
			print(A[i])
			C.append(A[i])
			i=i+1
		else:
			if(A[i]<=B[j]):
				print(i,j)
				print(A[i])
				C.append(A[i])
				i=i+1
			else:
				print(i,j)
				print(B[j])
				C.append(B[j])
				j=j+1
	return(C)

