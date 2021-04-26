def solution(s):
    if s == '':
        return []
    
    if (len(s)) % 2 != 0:
        s = s + '_'
    
    return [s[i:i+2] for i in range(0, len(s), 2)]