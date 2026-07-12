class Solution:
    # BruteForce time: O(n^2), space: O(1)
    def brute_force(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
                
        return False
    

    # Sorting time: O(n log n), space: O(1) or O(n) depending on sorting algorithm
    def sorting(self, nums: list[int]) -> bool:
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
            
        return False
    
    
    # OPTIMAL SOLUTION
    # Hashset time: O(n), space: O(n)
    def hashset(self, nums: list[int]) -> bool:
        hashset = set()

        for i in range(len(nums)):
            if nums[i] in hashset:
                return True
            
            hashset.add(nums[i])

        return False


    # Hashset time: O(n), space: O(n)
    def hashset_using_python_effeciency(self, nums: list[int]) -> bool:
        return len(set(nums)) < len(nums)


# Object "Solution" instance 
solution = Solution()

# Sample input for algorithm
nums = [1, 2, 3, 3]

# All algo outputs
print(solution.brute_force(nums))
print(solution.sorting(nums))
print(solution.hashset(nums))
print(solution.hashset_using_python_effeciency(nums))