class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      min_till_now = 100000
      profit = 0
      for price in prices:
        if min_till_now > price:
          min_till_now = price
        elif profit < price - min_till_now:
          profit = price - min_till_now
      return profit
