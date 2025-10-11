class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int n = nums.length;
        Arrays.sort(nums);
        int closest_sum = Integer.MAX_VALUE;
        for (int i = 0; i < n - 2; i++) {
            int left = i + 1;
            int right = n - 1;
            while (left < right) {
                int sum = nums[left] + nums[right] + nums[i];
                
                if (sum == target) {
                    return sum;
                }
                if (Math.abs(target - sum) < Math.abs(target - closest_sum)) {
                    closest_sum = sum;
                }
                
                if (sum < target) {
                    while (left < right && nums[left] == nums[left + 1]) {left++;}
                    left++;

                } else {
                    while (left < right && nums[right] == nums[right - 1]) {right--;}
                    right--;
                }
            }

        }
        return closest_sum;
    }
}