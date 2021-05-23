def Solution(S):
    try:
        S = list(S)
        copy = S[::-1] # O(n)

        for i in range(len((S))): # one iteration, O(n)
            if S[i] == '?' and copy[i] == '?':
                S[i], copy[i] = 'a', 'a' # If both questions marks then make both m,atch with 'a'
            elif S[i] == '?' and copy[i] != '?': # If one a question mark, make it match the other
                S[i] = copy[i]
            elif S[i] != '?' and copy[i] == '?': 
                copy[i] = S[i]
            elif S[i] != copy[i]: # If they're letters but dont match, it's invalid
                return "NO"
            else:
                continue # If they're the same it''l continue

        if S == copy: # Palindromes match when reversed, if they do convert to string and return
            result = ''.join([str(elem) for elem in copy])
            return result
        else:
            return "NO"
    except:
        return "NO" # Something couldve gone wrong, catch it (e.g empty String)
