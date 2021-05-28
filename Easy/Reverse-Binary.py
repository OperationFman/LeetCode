class Solution:
    def reverseBits(self, n):
        x = '{0:032b}'.format(n) # Convert binary to a string that still looks like the binary
        return int(x[::-1],2) # x[::-1] reverses the string (aka the binary). int(n,2) converts the binary into an int (12345678)