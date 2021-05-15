def maximumToys(prices, k):
    """ [4, 3, 5, 1, 2] """
    try:
        prices = sorted(prices) # Sort the array so the smallest values come first
        budget = k # Unecessary
        counter = 0 # Keep track of how many fit within the budget
        
        for i in prices:
            if i < budget: # As we move up the array they get more expensive but this maximizes what can fit
                counter += 1
                budget -= i # Remove the cost of the next smallest item on the budget
        # To make this more efficient you'd remove anything over the initial budget from the array anyway
                
        return counter
    except:
        return 0 # If something goes wrong, Mark probably couldn't buy anything anyway