"""
 The cost of a stock on each day is given in an array, find the max profit that you can make by buying and selling in those days.
  For example, if the given array is {100, 180, 260, 310, 40, 535, 695}, the maximum profit can earned by buying on day 0, 
  selling on day 3. Again buy on day 4 and sell on day 6. 
  If the given array of prices is sorted in decreasing order, then profit cannot be earned at all.

   Decreasing order then no profit
   Increasing order then difference between last and first day

   10 24 7 89 34 54 28

   Day 1 Buy - Day 2 Sell - 14
   Day 3 Buy -Day 4 Sell - 82
   Day 5 Buy - Day 6 Sell - 20

   10 24 7 8 9 11

   24 7 8 9 25

   basically there should a up and down, buy on down and sell on up
   Buy on Day 1: What's the profit
   Buy on Day 2: What's the profit
   Buy on Day 3: Profit
   Buy on Day N: Profit
   Max(PD1, PD2, PD3,.... PDN) - O(n2)
	
   Algorithm to calculate the profit:
    /*
     * Some DP can be add by traversing from last
     * By adding the last element to the store
    */ 
      start = i
      profit = 0
      end = start
      while(end <len(profit)):
      	if end + 1 < len(profit) and price[end] < price[end+1] // if end + 1 is last element then it will throw error
      		end += 1
	      else:
	      	  cur_profit = price[end] - price[start] // it can't be minus value
			  
	      	  if (cur_profit >  0):
	      	  	profit += cur_profit
			  start = end+1
			  end = end+2

"""

class Solution(object):
	def __init__(self):
		self.calculated_profits = []

	def find_profit(self, days_price):
		profits = []
		for i in range(0, len(days_price)):
			profits.append(self.calculate_profit(days_price, i))
		return max(profits)
	def find_profit_dp(self, days_price):
		profits = []
		self.calculated_profits  = [0 for i in range(len(days_price))]
		# self.calculated_profits[-1] = 0
		for i in range(len(days_price)-2, -1, -1):
			if days_price[i] < days_price[i+1]:
				self.calculated_profits[i] = (days_price[i+1] - days_price[i]) + self.calculated_profits[i+1]
			else:
				self.calculated_profits[i] = self.calculated_profits[i+1]
		return max(self.calculated_profits)

	def calculate_profit(self, days_price, starting_from):
		start = starting_from
		end = start
		profit = 0
		while (end < len(days_price)):
			if end + 1 < len(days_price) and days_price[end] < days_price[end+1]:
				end += 1
			else:
				cur_profit = days_price[end] - days_price[start]
				if (cur_profit > 0):
					profit += cur_profit
				start = end + 1
				end = start
		return profit

if __name__ == "__main__":
	solution = Solution()
	days_price = [100, 180, 260, 310, 40, 535, 695]
	days_price = range(1,1000000)
	days_price = [10,24,7,8,9,11]
	days_price = [10,8,7,6]
	max_profit = solution.find_profit_dp(days_price)
	print(max_profit)