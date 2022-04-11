def maxProfit(prices):
    """
    - min purchase price
    - max sale price, right of min.
    - if no option to profit, blow up.

    prices = [7,1,5,3,6,4]
    5

    prices = [7,6,4,3,1]
    0

    prices = [7,-2,-3,4,-9]
    6

    prices = [-7,9,-8,-4,-5]
    16
    """
    min = prices[0]
    max = 0
    for i in prices:
        if i < min:
            min = i
        if i - min > max:
            max = i - min
    return max

hecka_prices = [[-7,9,-8,-4,-5],[7,-2,-3,4,-9],[7,6,4,3,1],[7,1,5,3,6,4]]
for i in hecka_prices:
    print(maxProfit(i))
