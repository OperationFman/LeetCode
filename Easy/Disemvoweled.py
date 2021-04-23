def disemvowel(string_):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    array = list(string_)
    response = []
    for i in array:
        if i not in vowels:
            response.append(i)
    string_ = ''.join([str(j) for j in response])
    return string_