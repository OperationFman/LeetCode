def create_phone_number(n):
    n.insert(0, '(')
    n.insert(4, ') ')
    n.insert(8, '-')
    return ''.join(str(i) for i in n)