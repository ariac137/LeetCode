class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        if (m == 0) {
            for (int i = 0; i < n; i++) {
                nums1[i] = nums2[i];
            }
            return;
        } 

        if (n == 0) {
            return;
        }

        int i = 0; 
        int j = 0;

        while (i < m + j && j < n) {
            if (nums1[i] == nums2[j]) {
                i++;
                allMovesToRight(nums1, i, nums2[j], m + j);
                i++;
                j++;
            } else if (nums1[i] < nums2[j]) {
                i++;
            } else {
                allMovesToRight(nums1, i, nums2[j], m + j);
                i++;
                j++;

            }
        }

        while (j < n) {
            nums1[i] = nums2[j];
            i++;
            j++;
        }

        
    }

    public void allMovesToRight(int[] nums, int currentIndex, int num, int lastIndex) {

        for (int i = lastIndex; i > currentIndex; i--) {
            nums[i] = nums[i - 1];
        }
        nums[currentIndex] = num;
    }

}