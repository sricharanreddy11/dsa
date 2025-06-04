"""
Problem: Min and Max in Array
Difficulty: Easy
Source: GFG

Description:
Given an array arr. Your task is to find the minimum and maximum elements in the array.

Note: Return a Pair that contains two elements the first one will be a minimum element and the second will be a maximum.


Example:
Input: arr[] = [3, 2, 1, 56, 10000, 167]
Output: 1 10000

Approach:
We need to iterate the array once to find the minimum and maximum element in the array so it will take O(n) for sure
Maintaining varibales for min and max and keep updating them through the iteration

More optimal approach -- to proccess in pairs i.e, iterate using a while loop with step as 2 so compare both of them at once!

Time Complexity: O(n)
Space Complexity: O(1)
"""

def min_and_max_using_iteration(nums):
    max = -1
    min = float('inf')
    for ele in nums:
        max = ele if ele >= max else max
        min = ele if ele <= min else min
    return min, max

def min_and_max_pairwise(nums):
    n = len(nums)
    if n % 2 == 0:
        if nums[0] > nums[1]:
            max_val, min_val = nums[0], nums[1]
        else:
            max_val, min_val = nums[1], nums[0]
        i = 2
    else:
        max_val = min_val = nums[0]
        i = 1

    while i < n - 1:
        if nums[i] > nums[i + 1]:
            local_max, local_min = nums[i], nums[i + 1]
        else:
            local_max, local_min = nums[i + 1], nums[i]

        max_val = local_max if local_max > max_val else max_val
        min_val = local_min if local_min < min_val else min_val

        i += 2

    return min_val, max_val

if __name__ == "__main__":
    # Add test cases here
    pass
