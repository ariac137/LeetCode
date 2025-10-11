class Solution {
    public void sortColors(int[] nums) {

        final int RED = 0;
        final int WHITE = 1;
        final int BLUE = 2;

        int n = nums.length;

        int low = 0;
        int mid = 0; 
        int high = n - 1;

        while (mid <= high) {
            if (nums[mid] == RED) {
                swap(nums, low, mid);
                low++;
                mid++;
            } else if (nums[mid] == WHITE) {
                mid++;
            } else {
                swap(nums, high, mid);
                high--;
            }
        }
        
    }

    public void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}