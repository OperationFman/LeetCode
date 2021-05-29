from collections import Counter

def checkMagazine(magazine, note):
    """ [['Quick'], ['Fox']] & [['Quick'], ['Brown'] ['Fox']] """
    # Clue: Once you use a magazine word, aka element, it is removed and can't be used again. pop is your friend
    count = Counter(magazine)
    output = "Yes"
    
    for i in note:
        if i in count and count[i] > 0: # Checking if in a counter is O(1). If it exists and has any remaining then decrement
            count[i] -= 1
        else: # if the word doesn;t exist or have any elements left then it can't work
            output = "No"
            
    print(output) # it's print not return so store it in a value instead