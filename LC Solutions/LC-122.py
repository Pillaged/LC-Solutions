def maxProfit(prices) -> int:
    """
    - buy and sell multiple times on the same day??? 
    - buy and sell one stock, multiple times per time series
    - maximize profit, return profit.
    """
    profit = 0
    currmax = 0
    for day in range(1, len(prices)):
        currmax = prices[day] - prices[day-1]
        if currmax > 0:
            profit += currmax
    return profit

a = [[7,1,5,3,6,4],[1,2,3,4,5],[7,6,4,3,1]] #7,4,0
for i in a:
    print(maxProfit(i))