class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {

        Set<List<Integer>> uniqueSet = new HashSet<>();

        int n = nums.length;
        Arrays.sort(nums);

        for (int i = 0; i < n - 3; i++) {
            for (int j = i + 1; j < n - 2; j++) {
                int left = j + 1; 
                int right = n - 1;

                while (left < right) {
                    long sum = (long) nums[left] + nums[right] + nums[i] + nums[j];
                    //System.out.println(sum);
                    if (sum == target) {
                        List<Integer> quadruplets = Arrays.asList(nums[i], nums[j], nums[left], nums[right]);
                        Collections.sort(quadruplets);
                        uniqueSet.add(quadruplets);

                        while (left < right && nums[left] == nums[left + 1]) {left++;}
                        while (left < right && nums[right] == nums[right - 1]) {right--;}

                        left++;
                        right--;
                    }
                    else if (sum < target) {
                        while (left < right && nums[left] == nums[left + 1]) {left++;}
                        left++;
                    } else {
                        while (left < right && nums[right] == nums[right - 1]) {right--;}
                        right--;
                    }
                }
            }

        }

        List<List<Integer>> result = new ArrayList<>(uniqueSet);
        return result;
        
    }
}