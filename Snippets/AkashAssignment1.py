N, Q = input('').split()
N = int(N)
Q = int(Q)
S = input('')

def calculateResult(L, R, K):
    character_array = [0]*26
    characters_traversed = 0
    for counter in range(L-1, R):
        character_array[ord(S[counter])-97] += 1
    for counter in range(0, 26):
        characters_traversed += character_array[counter]
        if characters_traversed >= K:
            return chr(97+int(counter))
    return ("Out of range")
    

for query in range(0, Q):
    L, R, K = input('').split(' ')
    L = int(L)
    R = int(R)
    K = int(K)
    print (calculateResult(L, R, K))

