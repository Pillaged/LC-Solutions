def maxProduct(nums) -> int:
    """
    - return x_1*x_2*[...x_n]
    - double negatives increase the total, future cases may include additional.
    - Kadane's Algorith.
    - max prod at [n:] and [:n]
    """
    currprod = nums[0]
    maxprod = nums[0]

    for pos in range(1,len(nums)):
        #print((pos, nums[pos]), currprod, maxprod)
        if nums[pos]:
            currprod *= nums[pos]
            maxprod = max(currprod, maxprod)
        else:
            maxprod = max(currprod, maxprod)
            currprod = 1
        

    return maxprod

"""
        max_prod, min_prod, ans = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            x = max(nums[i], max_prod*nums[i], min_prod*nums[i])
            y = min(nums[i], max_prod*nums[i], min_prod*nums[i])            
            max_prod, min_prod = x, y
            ans = max(max_prod, ans)
        return ans"""
        
a = [1,2,3,4,5] #120
b = [1,2,3,-4,-5] #120
c = [-5,-4,0,3,2,1] #20
d = [-5,0,-4,0,0] #0
e = [1,1,1,1,3,1,1,1,1] #3
f = [2,-5,-2,-4,3] #24
g = [-3] #-3
h = [3,-1,4] #4
i = [0, 3,-1,4,0,-1,6,0] #6

#print(maxProduct(c))
lzit = [a,b,c,d,e,f,g,h,i]
for i in lzit:
    print(maxProduct(i))