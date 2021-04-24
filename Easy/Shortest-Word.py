def find_short(s):
    if s == None:
        return None
    array = s.split(' ')
    smallest = ''
    for i in array:
        if smallest == '':
            smallest = i
        elif len(i) < len(smallest):
            smallest = i
    return len(smallest)