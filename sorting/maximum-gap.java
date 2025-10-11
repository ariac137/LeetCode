class Solution {
    public int maximumGap(int[] nums) {
        int n = nums.length;

        if (n < 2) {
            return 0;
        }

        Arrays.sort(nums);
        int prev = 0; 
        int curr = 1;
        int maxGap = 0;

        while (curr < n) {
            int gap = Math.abs(nums[curr] - nums[prev]);
            if (gap > maxGap) {
                maxGap = gap;
            }
            prev++;
            curr++;
        }

        return maxGap;
    }
}