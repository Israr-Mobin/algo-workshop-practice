# Contains Duplicate

🔗 **LeetCode** (https://leetcode.com/problems/contains-duplicate/)

## Idea
Track numbers as you scan the array, A hash set gives O(1) average lookup so "have I seen this before?" is instant.

## Approach
- Create an empty set.
- For each number: if it's already in the set, return `True`.
- Otherwise add it to the set.
- No matches by the end -> return `False`.

## Complexity
- **Time:** O(n)
- **Space:** O(n)

## Pattern
**Hash Set** - reach for this when you need fast lookups and order doesn't matter.

## Solution
See `solution.py`.