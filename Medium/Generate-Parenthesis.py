class Solution:
    def generateParenthesis(self, n: int):
        # Base Case
        if n==1:
            return ['()']
        
        all_combos = self.generateParenthesis(n-1) # Recursively generate previous solution
        new_combos = [] #init combos for this n
        for combo in all_combos:
            i = 1 # Inserting a '()' in all possible places
            while i <= len(combo):
                new_combo = combo[:i]+'()'+combo[i:]
                i+=1
                new_combos.append(new_combo)
            
        return list(set(new_combos)) #return unique solutions

# Refactor!!