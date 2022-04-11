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
    for r in range(len(nums)):
        total *= nums[r]
        #print(total, nums[:r])
        for l in range(r):
            total//= nums[l]
            print(r, l, nums[l:r], total)

            if total < k:
                count += 1
        if total < k:
            print(total, r)
            count += 1
            
        #print("ciount", count)
    return count, "answered"

lzit = []
lzit.append(([1,2,3], 6)) #4
#lzit.append(([1,2,3,4,5,6], 6)) #5 + 1 = 6
#lzit.append(([1,2,3,4,5,6], 35)) #6 + 5 + 2 + 1 = 14
#lzit.append(([1,2,3,4,5,6], 10)) #6 + 2 + 1 = 9
#lzit.append(([1,2,3,4,5,6], 1000)) #6 + 5 + 4 + 3 + 2 + 1 = 21

for i in lzit:
    print(numSubarrayProductLessThanK(i[0], i[1]))