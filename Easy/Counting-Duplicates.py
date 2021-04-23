from collections import Counter

def duplicate_count(text):
    text = text.lower()
    text.split()
    print(text)
    result = 0
    counts = dict(Counter(text))
    print(counts)
    for i in counts:
        if counts[i] > 1:
            print('caught ' + str(i))
            result += 1
    return result