def solution(nums):
    if nums == None or len(nums) == 0:
        return []
    else:
        nums.sort()
        return nums