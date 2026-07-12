class Solution:
    # BacktrackingHashset time: O(n! * n), space: O(n! * n)
    def backtracking_hashset(self, nums: list[int]) -> list[list[int]]:
        result = set()

        def backtrack(perm):
            if len(perm) == len(nums):
                result.add(tuple(perm))
                return 

            for i in range(len(nums)):
                if nums[i] != float("-inf"):
                    perm.append(nums[i])
                    nums[i] = float("-inf")
                    backtrack(perm)
                    nums[i] = perm[-1]
                    perm.pop()
            
        backtrack([])
        return list(result)
    

    # BacktrackingHashmap time: O(n! * n), space: O(n! * n)
    def backtracking_hashmap(self, nums: list[int]) -> list[list[int]]:
        result = []
        perm = []
        count = {n: 0 for n in nums}
        for num in nums:
            count[num] += 1
        
        def dfs():
            if len(perm) == len(nums):
                result.append(perm.copy())
                return
            
            for num in count:
                if count[num] > 0:
                    perm.append(num)
                    count[num] -= 1
                    dfs()
                    count[num] += 1
                    perm.pop()
        
        dfs()
        return result
    
   
    # BacktrackingBooleanArray time: O(n! * n), space: O(n! * n)
    def backtracking_boolean_array(self, nums: list[int]) -> list[list[int]]:
        result, n = [], len(nums)
        visit = [False] * n
        perm = []

        def dfs():
            if len(perm) == n:
                result.append(perm.copy())
                return 
        
            for i in range(n):
                if visit[i]:
                    continue
                    
                if i and nums[i] == nums[i - 1] and not visit[i - 1]:
                    continue

                visit[i] = True
                perm.append(nums[i])
                dfs()
                visit[i] = False
                perm.pop()
        
        nums.sort()
        dfs()
        return result


    # BacktrackingOptimal time: O(n! * n), space: O(n! * n)
    def backtracking_optimal(self, nums: list[int]) -> list[list[int]]:
        result = []

        def dfs(i):
            if i == len(nums):
                result.append(nums.copy())
                return
            
            for j in range(i, len(nums)):
                if j > i and nums[i] == nums[j]:
                    continue

                nums[i], nums[j] = nums[j], nums[i]
                dfs(i + 1)
            
            for j in range(len(nums) - 1, i, -1):
                nums[j], nums[i] = nums[i], nums[j]
        
        nums.sort()
        dfs(0)
        return result

    
    # OPTIMAL SOLUTION
    # Iteration time: O(n! * n), space: O(n! * n)
    def iteration(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        result = [nums.copy()]

        while True:
            i = n - 2
            while i >= 0 and nums[i] >= nums[i + 1]:
                i -= 1
            
            if i < 0:
                break

            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            
            nums[i], nums[j] = nums[j], nums[i]

            left, right = i + 1, n - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1
            
            result.append(nums.copy())
        
        return result


# Object "Solution" instance 
solution = Solution()

# Sample input for algorithm
nums = [1,1,2]

# All algo outputs
print(solution.backtracking_hashset(nums))
print(solution.backtracking_hashmap(nums))
print(solution.backtracking_boolean_array(nums))
print(solution.backtracking_optimal(nums))
print(solution.iteration(nums))
