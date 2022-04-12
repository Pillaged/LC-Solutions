"""
- point to one pos behind, 2 pos behind.
- move by one.
- have a count of every arith. array behind, increment by

[1,2,3,4,5,6] = 4 of 3, 3 of 4, 2 of 5, 1 of 6 = 10
[1,2,3,4,5,6,7] = 5 of 3, 4 of 4, 3 of 5, 2 of 6, 1 of 7 = 15
[1,2,3,4,0,4,8] = 3 of 3, 1 of 4 = 4
[3,-1,-5,-9] = 3
[7,7,7,7] = 3

"""
def numberOfArithmeticSlices(nums: list[int]) -> int:
    consecutive = 0
    total = 0
    for i in range(2,len(nums)):
        if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
            consecutive += 1
        else: 
            for n in range(consecutive+1):
                total += n
            consecutive = 0
    for n in range(consecutive+1):
        total += n
    return total