class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;

        int minPrice = Integer.MAX_VALUE;
        int totalProfit = 0;


        for (int i = 0; i < n; i++) {
            if (prices[i] <= minPrice) {
                minPrice = prices[i];
            } else {
                totalProfit += prices[i] - minPrice;
                minPrice = prices[i];
            }

        }

        return totalProfit;
        
    }
}