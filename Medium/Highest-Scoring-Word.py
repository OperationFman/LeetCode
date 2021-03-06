from collections import Counter

def high(x):
    alphabet = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
                'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
                'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    
    if x == '':
        return 0
    
    try:
        up = x.upper()
        array = up.split(' ')
        originalArray = x.split(' ')
        
        scores = []    
        for word in array:
            score = 0
            for letter in word:
                if letter in alphabet:
                    score += alphabet[letter]
            scores.append(score)
        
        highest = max(scores)
        index = scores.index(highest)
        
        return originalArray[index]
    except:
        return 0