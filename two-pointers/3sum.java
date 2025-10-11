class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        int n = nums.length;
        Arrays.sort(nums);
        Set<List<Integer>> uniqueSet = new HashSet<>();
        
        for (int i = 0; i < n - 2; i++) {
            int left = i + 1;
            int right = n - 1;
            while (left < right) {
                if (nums[left] + nums[right] == - nums[i]) {
                    List<Integer> triplet = Arrays.asList(nums[left], nums[right], nums[i]);
                    Collections.sort(triplet);
                    uniqueSet.add(triplet);

                    while (left < right && nums[left] == nums[left + 1]) {
                        left++;
                    }
                    while (left < right && nums[right] == nums[right - 1]) {
                        right--;
                    }
                    left++;
                    right--;
                } else if (nums[left] + nums[right] < - nums[i]) {
                    left++;
                } else {
                    right--;
                }

            }

        }
        List<List<Integer>> result = new ArrayList<>(uniqueSet);
        return result;
    }
}