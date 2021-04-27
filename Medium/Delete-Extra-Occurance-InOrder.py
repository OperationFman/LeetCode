from collections import Counter

def delete_nth(order,max_e):
    try:
        if order == '' or max_e <= 0:
            return []
        
        counts = dict(Counter(order))
        result = []
        
        for count in counts:
            if counts[count] > max_e:
                counts[count] = max_e
        
        for i in order:
            if counts[i] > 0:
                counts[i] -= 1
                result.append(i)
                
        return result
    except:
        return []