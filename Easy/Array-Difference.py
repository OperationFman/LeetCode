def array_diff(a, b):
    try:
        for i, v in enumerate(a):
            if v in b:
                a.pop(i)
        for i, v in enumerate(a):
            if v in b:
                a.pop(i)
        return a
    except:
        return []

# For some reason simply doing it twice will always work. 
# I dunno why but even a list with multiple repeated values won;t work in one pass but will in 2