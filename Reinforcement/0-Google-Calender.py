# Input 1 - [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
# Bounds - ["9:00", "20:00"]

# Input 2 - [["10:00", "11:30"], ["12:30", "14:30"], ["14:30, 15:00"], ["16:00", "17:00"]]
# Bounds - ["10:00", "18:30"]

# Return the 'blocks' available in both calenders for a meeting, e.g:
# [[11:30, 12:00], [15:00, 16:00], [17:00, 18:30]]
# A block is a minimum of 30 minutes but must not be secular 30's