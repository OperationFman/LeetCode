input1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
# Bounds - ["9:00", "20:00"]

input2 = [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]]
# Bounds - ["10:00", "18:30"]

# Return the 'blocks' available in both calenders for a meeting, e.g:
# [[11:30, 12:00], [15:00, 16:00], [17:00, 18:30]]
# A block is a minimum of 30 minutes but must not be secular 30's

# Convert values to numbers
def inputCleaner(inputVal):
    cleanedInput = []
    for block in inputVal:
        converted = []
        for time in block:
            chop = time.split(":")
            chop = [ int(x) for x in chop ]
            converted.append(chop)
        cleanedInput.append(converted)
    return cleanedInput

cal1 = inputCleaner(input1)
cal2 = inputCleaner(input2)
print(cal1)
print(cal2)

# Combine calenders into one ordered list from starts. If starts are the same then default to the greater end time
# [[9:00, 10:30], [10:00, 11:30], [12:00, 13:00], [12:30, 14:30], [14:30, 15:00], [16:00, 18:00], [16:00, 17:00]]

# Iterate through, if the end of a time is less than the start of another, check if it's big enough for a free block (Larger than 30 minutes)
    # if it isn't then append the end time of the next to the current end and check again
# [9:00, 11:30], [12:00, 15:00], [16:00, 17:00]

# Get the highest start bound and the lowest end bound and check them against the above list
# [10:00] & [18.30]
# Check if the early is before the first in the blocked list above, if it is the first block will be between it and the first in the result, if it isnt do nothing
# Result = [] (Here it does nothing)

# Calculate the gaps between the last and the first
# Simply grab the last and the first of each node excluding the very last for now
# [11:30, 12:00], [15:00, 16:00]

# Do last, Check if the later bound is larger than the final in the above blocked list, if it is then append a block from the last to it on the result, if not do nothing
# result = [[11:30, 12:00], [15:00, 16:00], [17:00, 18:30]]