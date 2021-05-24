array = [1, 6, 2, 4, 8, 1, 4, 3, 6, 3, 8, 3, 4, 6, 9, 1, 3, 6, 2, 9, 5, 7, 2, 4, 6]

def stalinSort(array):
    elims = []
    count = array[0]
    for i in array:
        if i != count:
            elims.append(i)
        else:
            count += 1

    elims.reverse()
    for i in elims:
        array.pop(i)

    print(array)

stalinSort(array)