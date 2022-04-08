import math
def isPalindrome(x: int) -> bool:
    if x < 0 or (x%10 == 0 and x !=0):
        return False
    if x ==0:
        return True
    r = range(0, int(math.log10(x)))
    r2 = list(reversed(r))
    for i in r:
        last = (x//10**i)%10
        first = (x//(10**(r2[i]+1)))%10
        if first - last:
            return False
    return True









#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# 3 --> [((())), (()()), ()()(), (())(), ()(())]

# ()()(),       () (),                   () 
#            (())(),()(()),   |||    ((())),(()())

def generateParenthesis(n: int):
    list2 = []
    def helper(n):
        if n == 0:
            return ""
        leftstringy = ""
        rightstr = ""
        for i in range(1, n):
            leftstringy += "(" # (, ((, (((
            rightstr +=")"
            list2.append(leftstringy + helper(n-1) + rightstr)
        return leftstringy+rightstr
    helper(n)
    print(list2)

#generateParenthesis(3)