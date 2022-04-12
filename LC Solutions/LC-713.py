def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:
    """
    - k is a limit to the curr product
    - a = Test the entire array if less than k
    - Recursively solve: [:n] and [n:] for a
    - count for each time it passes
    - return the count
    """
    count = 0
    total = 1
    for r in range(0,len(nums)):
        total *= nums[r]
        for l in range(r):
            print(nums[l:r], total, total<k, count)
            if total < k:
                count += 1
            else:
                total = total//nums[l]
            
            print(l,r)
    return count

lzit = []
lzit.append(([10,5,2,6], 100)) #8
#lzit.append(([1,2,3], 6)) #4
#lzit.append(([1,2,3,4,5,6], 6)) #5 + 1 = 6
#lzit.append(([1,2,3,4,5,6], 35)) #6 + 5 + 2 + 1 = 14
#lzit.append(([1,2,3,4,5,6], 10)) #6 + 2 + 1 = 9
#lzit.append(([1,2,3,4,5,6], 1000)) #6 + 5 + 4 + 3 + 2 + 1 = 21

for i in lzit:
    print(numSubarrayProductLessThanK(i[0], i[1]))