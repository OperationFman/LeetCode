def iq_test(numbers):
    array = numbers.split(' ')
    array = [ int(x) for x in array ]
    
    odds = []
    evens = []
    
    for i, v in enumerate(array):
        if v % 2 == 0:
            evens.append(i + 1)
        else:
            odds.append(i + 1)
    
    if len(odds) < len(evens):
        return odds[0]
    elif len(odds) > len(evens):
        return evens[0]
    else:
        return 1