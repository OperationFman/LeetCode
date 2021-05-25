class Solution:
    def isValid(self, s):
        try:
            opens = ['(', '{', '['] # Having the opens and closes in to lists allows the access of
            closes = [')', '}', ']'] # Each ones index, that matches
            array = list(s) # makes the string more iterable

            store = [] # Think of a stack. Last on last off, if lasts doesn;t match then it's invalid

            for i in array:
                if i in opens: # If it's an open then we can;t do anything with it anyway
                    store.append(i) # add it to the stack (store)
                else:
                    close_index = closes.index(i) # Get the index in the closes
                    open_value = opens[close_index] # Match the index in opens to see if it's the same

                    if store[-1] != open_value: # If the last added to stack doesnt match the above found open
                        return False # It mustn't be valid. aka the last opened must always match a close, can't be: (])
                    else:
                        store.pop(-1) # If it did match then just remove it from the stack

            if store == []: # If all is well then the stack should be empty since every open 
                return True # Wouldve closed
            else:
                return False # If not (aka '(([[{{') then it's not valid

        except: # Finally it's a boolean so might aswell use try/except
            return False # This will trigger anyway if the input was '))]]}}' because it would fail
                        # Have no fear since it'd be invalid anyway