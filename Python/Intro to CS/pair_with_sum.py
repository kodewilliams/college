def HasPairWithTargetSum(nums, target_sum):
    for a in range(len(nums)):
        for b in range(a+1, len(nums)):
            current = nums[a] + nums[b]
            if current == target_sum:
                return True
    return False
