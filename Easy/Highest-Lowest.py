def high_and_low(numbers):
    numbers = numbers.split(" ")
    array = []
    for i in numbers:
        array.append(int(i))
    array.sort()
    l, h = array[0], array[-1]
    numbers = str(h) + " " + str(l)
    return numbers
    