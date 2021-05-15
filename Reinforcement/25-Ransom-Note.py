def checkMagazine(magazine, note):
    """ [['Quick'], ['Fox']] & [['Quick'], ['Brown'] ['Fox']] """
    try: # Boolean answer so might aswell try this
        state = True # Because it's print and not return we want to store state
                    # This is stupid inefficient, a better way would be to run the loop in a method 
                    # that returns the result if it equals a 'No'
        
        for i in note:
            if i not in magazine:
                state = False # If any token isn;t in the magazine it's a 'No'
                break # Break the loop for performance
            if i in magazine:
                magazine.pop(magazine.index(i)) # If it is in the mag, then remove it as it's been 'used'
                
        if state == True: # Check if that value is true or false, not doing so may equal 'No' followed by 'Yes'
            print('Yes')
        else:
            print('No')
    except:
        print('No')