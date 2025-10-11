class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int indexDiff, int valueDiff) {
        int n = nums.length;

        if (indexDiff == n) {
            Arrays.sort(nums);
        }

        for (int i = 0; i < n; i++) {

            if (indexDiff == n) {
                for (int j = 1; j <= valueDiff + 1 && i + j < n; j++) {
                    if (Math.abs(nums[i] - nums[i + j]) <= valueDiff) {
                        return true;
                    }

                }
            }
            else {
                for (int j = 1; j <= indexDiff && i + j < n; j++) {
                    if (Math.abs(nums[i] - nums[i + j]) <= valueDiff) {
                        return true;
                    }

                }
            }

            
        }

        return false;
        
    }
}