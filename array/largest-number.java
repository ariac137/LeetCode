class Solution {
    public String largestNumber(int[] nums) {
        // Convert integers to strings
        String[] strNums = new String[nums.length];
        for (int i = 0; i < nums.length; i++) {
            strNums[i] = String.valueOf(nums[i]);
        }

        // Custom comparator: compare by (b+a).compareTo(a+b)
        Arrays.sort(strNums, (a, b) -> (b + a).compareTo(a + b));

        // If the largest number is "0", the whole number is 0
        if (strNums[0].equals("0")) return "0";

        // Join all strings
        StringBuilder result = new StringBuilder();
        for (String s : strNums) {
            result.append(s);
        }

        return result.toString();
    }
}