class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length <= 1:
            return 0
        i = 0
        max_profit = 0
        while i < length:
            # print(prices)
            # print("i = " + str(i))
            if self.can_buy(prices[i:]):
                # print("can buy when i = " + str(i))
                new_prices = prices[i + 1:]
                for j, price in enumerate(new_prices):
                    #print("j = " + str(j))
                    #print("price = " + str(price))
                    #print("in " + str(new_prices))
                    if price > prices[i]:
                        #print("price > prices[i]: " + str(price) + ">" + str(prices[i]))
                        temp_profit = (price - prices[i]) + self.maxProfit(new_prices[j + 1:])
                        #print("temp_profit = " + str(temp_profit))
                        if temp_profit > max_profit:
                            max_profit = temp_profit
                            temp_profit = 0
            i = i + 1
        return max_profit
        
        
        
    def can_buy(self, prices: List[int]) -> bool:
        length = len(prices)
        if length <= 1:
            return False
        for price in prices[1:]:
            if prices[0] < price:
                return True
        return False
 