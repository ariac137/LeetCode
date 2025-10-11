class Solution {
    public int removeElement(int[] nums, int val) {

        int n = nums.length;
        int size = n;

        int i = 0;

        while (i < size) {
            if (val == nums[i]) {
                swap(nums, i, size - 1);
                size--;
                continue;
            }
            i++;
        }

        return size;
        
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[j];
        nums[j] = nums[i];
        nums[i] = temp;
    }
}