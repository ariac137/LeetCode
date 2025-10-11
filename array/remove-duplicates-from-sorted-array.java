class Solution {
    public int removeDuplicates(int[] nums) {
        int n = nums.length;
        int count = 1;
        int i = 1;

        while (i < n) {
            if (nums[i] != nums[i - 1]) {
                nums[count] = nums[i];
                count++;
            }
            i++;
        }

        return count;    
    }
}