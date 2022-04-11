def maxSubArray(nums):
    """
    - numbers can be both positive and negative
    - returns one sum
    - sum whole list
    - max sum of the list [n:]
    - max sum of the list at [:n]
    [-2,1,-3,3,4,-1,2,1,-5,4]
    """
    total = 0
    temp = 0
    max = nums[0]
    for dig in nums:
        if dig > max:
            max = dig
        temp += dig
        if temp > total:
            total = temp
        elif temp <0:
            temp = 0
    if total == 0:
        return max
    return total
