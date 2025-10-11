class Solution {
    public int removeDuplicates(int[] nums) {
        int n = nums.length;

        int count = 1;
        int temp_count = 1;

        int i = 1;

        while (i < n) {
            if (nums[i] == nums[i - 1]) {
                if (temp_count > 1) {
                    i++;
                    continue;
                }
                nums[count] = nums[i];
                count++;
                temp_count++;

            } else {
                nums[count] = nums[i];
                count++;
                temp_count = 1;
            }
            i++;
        }

        return count;

        
    }
}