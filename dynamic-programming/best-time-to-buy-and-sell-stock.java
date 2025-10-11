class Solution {
    public int maxProfit(int[] prices) {
        int maxGap = 0;
        int minPrice = Integer.MAX_VALUE;

        for (int price: prices) {
            if (price < minPrice) {
                minPrice = price;
            } else {
                maxGap = Math.max(maxGap, price - minPrice);
            }
        }

        return maxGap;
        
    }
}