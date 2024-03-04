class Solution(object):
    #暴力双for就好
    # def twoSum(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
    #     #n^2
    #     ls = len(nums)
    #     for i in range(ls):
    #         for j in range(i + 1, ls):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]

    # def twoSum(self, nums, target):
    #     # hash 2
    # enumerate: Return type: <class 'enumerate'>
#[(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
#[(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]


    #   num_indices = {}
        
    #   for i, num in enumerate(nums):
    #       complement = target - num
            
    #       if complement in num_indices:
    #           return [num_indices[complement], i]

    #       num_indices[num] = i
                
