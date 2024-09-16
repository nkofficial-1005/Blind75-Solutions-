class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {} #empty dictionary
        for i, value in enumerate(nums): #enumerate gives the index and value
            remainder = target - nums[i]
            if remainder in checked:
                return [checked[remainder], i]
            else:
                checked[value] = i