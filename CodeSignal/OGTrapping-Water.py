class Solution:
    def trap(self, height):
        stack = []
        
        current = 0
        ans = 0
        while current < len(height):
            while len(stack) > 0 and height[current] > height[stack[-1]]:
                top = stack.pop()
                if len(stack) == 0:
                    break

                dist = current - stack[-1] - 1

                ans += dist * (min(height[current], height[stack[-1]]) - height[top])
                
            stack.append(current) 
            current += 1
            
        return ans

# Refactor!
