import copy


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # first approach
    # O(n**2) complexity
    # count = 0
    # for i in range(0, len(nums)):
    #     count += 1
    #     i_value = nums.pop(0)
    #     for j in range(0, len(nums)):
    #         if i_value + nums[j] == target:
    #             return [i, j + count]

    # Better way of saying it
    # for i in range(0, len(nums)):
    #     for j in range(0, len(nums)):
    #         if nums[i] + nums[j] == target and i != j:
    #             return [i, j]

    # Second approach
    # O(n**2) complexity
    # count = 0
    # for i in range(0, len(nums)):
    # count += 1
    # num_without_i = copy.deepcopy(nums)
    # num_without_i.pop(0)
    # for j in range(0, len(num_without_i)):
    #     if nums[i] + num_without_i[j] == target:
    #         return [i, j + count]

    # Third approach idea => j = target - nums[i]

    # Forth approach idea => create dic from the list that we have and store all the sums results and the indexes of the values that resulted to that sum
    # Best Answer: combination of 3d approach and 4th approach
    num2 = {}

    for i, num in enumerate(nums):
        print(i, num)
        diff = target - num
        if diff in num2:
            return [num2[diff], i]
        num2[num] = i


nums = [3, 0, 0, 3]
target = 6
print(twoSum(nums, target))

nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))

nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))

# for i, j in enumerate(nums):
#     print(i, j)
