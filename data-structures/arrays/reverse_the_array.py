"""
Problem: You are given an array of integers arr[]. Your task is to reverse the given array.
Difficulty: Easy
Source: GFG
Link: https://www.geeksforgeeks.org/problems/reverse-an-array/1

Description:
Note: Modify the array in place.


Example:
Input: arr = [1, 4, 3, 2, 6, 5]
Output: [5, 6, 2, 3, 4, 1]

Approach:
I'll use a two-pointer approach to reverse the array in place. One pointer will start at the beginning of the array and the other at the end.
I'll swap the elements at these pointers and then move the pointers towards each other until they meet.

We can make it optimal by not using temp variable for swapping rather using elegant python tuple unpacking.
nums[i], nums[j] = nums[j], nums[i]
but we will use a temp variable to make it more language friendly.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def reverse_array_using_two_pointer(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp
        left += 1
        right -= 1


if __name__ == "__main__":
    arr = [1, 4, 3, 2, 6, 5]
    reverse_array_using_two_pointer(arr)
    print(arr)