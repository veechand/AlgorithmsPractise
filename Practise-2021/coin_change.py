import sys

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
         row is amount
         col is coins
        """
        coins = sorted(coins)
        print(coins)
        MAX_VALUE = sys.maxint
        dp = [[MAX_VALUE for i in range(len(coins))] for j in range(amount+1)]
        for i in range(len(dp[0])): # For amount 0 no coins are needed
            dp[0][i] = 0
        for amount in range(len(dp)):
            if amount % coins[0]  == 0:
                dp[amount][0] = amount/coins[0]
            else:
                dp[amount][0] = MAX_VALUE
                
        for cur_amount in range(1, len(dp)):
            for j in range(1, len(coins)):
                print("amount,coins", cur_amount, coins[j])
                value1 = MAX_VALUE
                value2 = MAX_VALUE
                if cur_amount >= coins[j]:
                    rem_amount = cur_amount % coins[j]
                    minus_amount = 0
                    while rem_amount <= cur_amount:
                        print ("rem_amount and dp",rem_amount,dp[rem_amount][j])
                        if dp[rem_amount][j] == MAX_VALUE:
                            rem_amount +=  coins[j]
                            minus_amount += 1
                            continue    
                        if dp[rem_amount][j] != MAX_VALUE:
                            value1 = (cur_amount / coins[j]) + dp[rem_amount][j] - minus_amount
                            print("value1", value1)
                            break
                value2 = dp[cur_amount][j-1]
                print("value1, value2", value1, value2)
                dp[cur_amount][j] = min(value1, value2)
        print(dp)
        return -1 if dp[-1][-1] == MAX_VALUE else dp[-1][-1]

solution = Solution()
# coins = [1,2,5]
# amount = 11
# print(solution.coinChange(coins, amount))
# coins = [2]
# amount = 3
# print(solution.coinChange(coins, amount))
# coins = [1]
# amount = 0
# print(solution.coinChange(coins, amount))
# coins = [2,5]
# amount = 12
# print(solution.coinChange(coins, amount))
coins = [186,419,83,408]
amount = 6249
# coins = [2,4,5]
# amount = 11
print(solution.coinChange(coins, amount))
