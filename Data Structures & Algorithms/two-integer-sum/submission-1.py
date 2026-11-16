class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = []
        # a = int(input("Enter the number of elements in list: "))

        # for i in range(a):
        #     num = print("Enter the elements: ")
        #     nums.append(num)
        
        # target = int(input("Enter target num: "))

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                