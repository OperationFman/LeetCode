def Solution(S):
    try:
        S = list(S)
        copy = S[::-1]

        for i in range(len((S))):
            if S[i] == '?' and copy[i] == '?':
                S[i], copy[i] = 'a', 'a'
            elif S[i] == '?' and copy[i] != '?':
                S[i] = copy[i]
            elif S[i] != '?' and copy[i] == '?':
                copy[i] = S[i]
            elif S[i] != copy[i]:
                return "NO"
            else:
                continue
            