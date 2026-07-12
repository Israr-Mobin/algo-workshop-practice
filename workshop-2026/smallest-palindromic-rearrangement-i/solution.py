class Solution:
    # BruteForce time: O(n! * n), space: O(n! * n)
    def brute_force(self, s: str) -> str:
        from itertools import permutations
        best = None

        for perm in set(permutations(s)):
            candidate = "".join(perm)

            if candidate == candidate[::-1]:
                if best is None or candidate < best:
                    best = candidate
        
        return best
    

    # Hashmap + Sort time: O(n log n), space: O(n)
    def hashmap_sort(self, s: str) -> str:
        from collections import Counter
        counts = Counter(s)
        middle = ''
        half = []

        for ch, n in counts.items():
            if n % 2:
                middle = ch
            half.extend([ch] * (n // 2))

        half.sort()
        left = ''.join(half)
        return left + middle + left[::-1]
    

    # OPTIMAL SOLUTION
    # CountingSort time: O(n), space: O(n)
    def counting_sort(self, s: str) -> str:
        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - 97] += 1

        middle = ''
        left_parts = []
        for i in range(26):
            n = counts[i]
            if n == 0:
                continue
            ch = chr(i + 97)
            if n % 2:
                middle = ch
            left_parts.append(ch * (n // 2))

        left = ''.join(left_parts)
        return left + middle + left[::-1]


# Object "Solution" instance 
solution = Solution()

# Sample input for algorithm
s = "daccad"

# All algo outputs
print(solution.brute_force(s))
print(solution.hashmap_sort(s))
print(solution.counting_sort(s))




        