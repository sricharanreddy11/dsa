"""
Problem: Kth Largest Element in an Array
Difficulty: Medium
Source: Leetcode

Description:
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Approach:

Directly sorting and giving the element in place would be of O(n logn) complexity
But for the average cases the quick-select would give more optimal solution

Dived and conquer method by keeping a pivot element and splitting the array into two parts and understanding in which part of the array we can find the smallest or the largest element


Time Complexity: O(n (k))
Space Complexity: O(n)
"""



def findKthLargest(self, nums, k):
        
        k = len(nums) - k  # for kth smallest we can just use k directly
        
        def quickSelect(l, r):
    
            pivot = nums[r]
            pointer = l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[pointer], nums[i] = nums[i], nums[pointer]
                    pointer += 1
            
            nums[pointer], nums[r] = nums[r], nums[pointer]

            if pointer > k:
                return quickSelect(l, pointer - 1)
            elif pointer < k:
                return quickSelect(pointer + 1, r)
            else:
                return nums[pointer]

        return quickSelect(0, len(nums) - 1)
    

if __name__ == "__main__":
    # Add test cases here
    pass