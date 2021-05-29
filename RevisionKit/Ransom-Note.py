def checkMagazine(magazine, note):
    """ [['Quick'], ['Fox']] & [['Quick'], ['Brown'] ['Fox']] """
    # Clue: Once you use a magazine word, aka element, it is removed and can't be used again. pop is your friend
    output = "Yes"
    
    for i in note:
        if i in magazine:
            magazine.pop(magazine.index(i))
        else:
            output = "No"
    
    print(output)