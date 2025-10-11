class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        int n = nums.length;
        Set<List<Integer>> permutation_set = new HashSet<>();

        List<Integer> list = Arrays.stream(nums)
                        .boxed()
                        .collect(Collectors.toList());
        permutations(list, new ArrayList<>(), permutation_set);

        List<List<Integer>> result = new ArrayList<>(permutation_set);

        return result;
        
    }

    public void permutations(List<Integer> list, List<Integer> temp_permutation, Set<List<Integer>> permutation_set) {
        int n = list.size();


        if (n == 1) {
            temp_permutation.add(list.get(0));
            permutation_set.add(new ArrayList<>(temp_permutation));
            return;
        }


        for (int i = 0; i < n; i++) {
            List<Integer> current_permutation = new ArrayList<>(temp_permutation);
            current_permutation.add(list.get(i));
            List<Integer> list_copy = new ArrayList<>(list);
            list_copy.remove(i);
            permutations(list_copy, current_permutation, permutation_set);
        }
        
    }

}