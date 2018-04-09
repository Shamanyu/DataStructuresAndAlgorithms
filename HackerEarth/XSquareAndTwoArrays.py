N, Q = raw_input('').split()
N = int(N)
Q = int(Q)

A = list()
B = list()
ASum = list()
BSum = list()

def constructASum():
	for position in range(N):
		if position > 1:
			ASum.append(A[position] + B[position-1] + ASum[position-2])
		elif position == 1:
			ASum.append(A[position] + B[position-1])
		else:
			ASum.append(A[position])
		
def constructBSum():
	for position in range(N):
		if position > 1:
			BSum.append(B[position] + A[position-1] + BSum[position-2])
		elif position == 1:
			BSum.append(B[position] + A[position-1])
		else:
			BSum.append(B[position])

A = raw_input('').split()
A = [int(number) for number in A]

B = raw_input('').split()
B = [int(number) for number in B]

constructASum()
constructBSum()

for counter in range(Q):
	matrix, L, R = raw_input('').split()
	matrix = int(matrix)
	L = int(L)
	R = int(R)
	if matrix == 1:
		if (R-L)%2 == 0:
			end = ASum[R-1]
		else:
			end = BSum[R-1]	
		if L == 1:
			print end
		else:
			print end - BSum[L-1-1]
	else:
		if (R-L)%2 == 0:
			end = BSum[R-1]
		else:
			end = ASum[R-1]
		if L == 1:
			print end
		else:
			print end - ASum[L-1-1]
