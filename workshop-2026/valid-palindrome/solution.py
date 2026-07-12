class Solution:
    # BruteForce time: O(n), space: O(n)
    def brute_force(self, s: str) -> bool:
        new_string = ""

        for character in s:
            if character.isalnum():
                new_string += character.lower()
        
        return new_string == new_string[::-1]
    

    # OPTIMAL SOLUTION
    # TwoPointer time: O(n), space: O(1)
    def two_pointer(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while not s[left].isalnum() and left < right:
                left += 1
            while not s[right].isalnum() and left < right:
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1

        return True


# Object "Solution" instance 
solution = Solution()

# Sample input for algorithm
s = "Was it a car or a cat I saw?"

# All algo outputs
print(solution.brute_force(s))
print(solution.two_pointer(s))




        