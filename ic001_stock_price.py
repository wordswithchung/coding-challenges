"""Suppose we could access yesterday's stock prices as a list, where:

- The indices are the time in minutes past trade opening time, which was 9:30am
local time.
- The values are the price in dollars of Apple stock at that time.
- So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the
best profit I could have made from 1 purchase and 1 sale of 1 Apple stock
yesterday.

No "shorting" - you must buy before you sell. You may not buy and sell in the
same time step (at least 1 minute must pass).
"""

# v1, naive, brute force answer; O(n^2) runtime
def get_max_profit_1(stock_prices_yesterday):
    """Given list of stock prices, return maximum profit one can make from one
    purchase, one sale, of one stock.


        >>> stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
        >>> get_max_profit_1(stock_prices_yesterday)
        6
    """

    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    for price in stock_prices_yesterday:
        for i in stock_prices_yesterday[1:]:
            if i - price > max_profit:
                max_profit = i - price

    return max_profit

# track min_price, track max_profit
def get_max_profit(stock_prices_yesterday):
    """Given list of stock prices, return maximum profit one can make from one
    purchase, one sale, of one stock.


        >>> stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
        >>> get_max_profit(stock_prices_yesterday)
        6
    """

    if len(stock_prices_yesterday) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')

    min_price = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    for current_price in stock_prices_yesterday[1:]:
        potential_profit = current_price - min_price
        min_price = min(current_price, min_price)
        max_profit = max(potential_profit, max_profit)

    return max_profit
