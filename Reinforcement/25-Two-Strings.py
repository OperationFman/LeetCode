def twoStrings(s1, s2):
  """ 'Hello' & 'World' """
  try: # Boolean response so may aswell try
      if s1 == '' or s2 == '': # If one is empty then it wouldn't match so must return no
          return "NO" 

      array1, array2 = list(s1), list(s2) # Need to iterate, so convert to lists. A little more convenient to do it in one line
      for i in array1:
          if i in array2:
              return "YES" # If a single element matches then it's a yes
      for i in array2:
          if i in array1:
              return "YES" # Do the same on the other list
      return "NO" # If niether of the above triggers then it must be a no
   except:
    return "NO" # If it breaks it was likely a no anyway
