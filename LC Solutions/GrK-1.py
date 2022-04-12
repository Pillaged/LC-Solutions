'''
Problem Statement 

Given an array of characters where each character represents a fruit tree, you are given two baskets and your 
goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.
You can start with any tree, but once you have started you cannot skip a tree.
You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both the baskets.
Example 1:
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
Example 2:
Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
'''

def fruitpicker(trees):
    basket1 = [trees[0],0]
    basket2 = [trees[0],0]
    maxsofar = 0
    currval = 0
    for f in range(1, len(trees)):
        if basket1[0] != trees[f] and basket2[0] != trees[f] and basket1[1] <= basket2[1]:
            basket1[0], basket1[1]= trees[f], f
        elif basket1[0] != trees[f] and basket2[0] != trees[f]:
            basket2[0], basket2[1] = trees[f], f
        currval = abs(basket1[1] - basket2[1])+1
        if f == len(trees)-1:
            currval = (f - min(basket1[1], basket2[1]))+1
        
        print(currval)
        maxsofar = max(currval, maxsofar)
    return maxsofar


##TESTS##

tests_list = []
tests_list.append((['A', 'B', 'C', 'A', 'C',], 3))
tests_list.append((['A', 'B', 'C', 'B', 'B', 'C'], 5))
tests_list.append((['A','T','E','U','G'], 2))
#tests_list.append(())
#tests_list.append(())

def testing_func(ls, n, iteration):
    if fruitpicker(ls) ==  n:
        print("Passed on test", iteration)
    else:
        print("Failed test number", iteration)

for j, i in enumerate(tests_list):
    testing_func(i[0], i[1], j+1)