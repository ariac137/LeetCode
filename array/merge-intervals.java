class Solution {
    public int[][] merge(int[][] intervals) {

        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

        
        int n = intervals.length;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 2; j++) {
                System.out.print(intervals[i][j] + " ");
            }
            System.out.println();
        }
        List<int[]> list = new ArrayList<>();

        if (n == 1) {
            return intervals;
        }

        int min_front = intervals[0][0];
        int max_end = intervals[0][1];

        int i = 1;

        while (i < n) {
            int front = intervals[i][0];
            int end = intervals[i][1];
            
            if (front <= max_end) {
                max_end = Math.max(end, max_end);  

            } else {
                int[] new_range = {min_front, max_end};
                list.add(new_range);
                min_front = front;
                max_end = end;

            }
            i++;
        }

        int[] new_range = {min_front, max_end};
        list.add(new_range);

        int[][] result = convertListToArray(list);
        return result;
    }

    public int[][] convertListToArray(List<int[]> list) {
        int[][] result = new int[list.size()][];
        for (int i = 0; i < list.size(); i++) {
            result[i] = list.get(i);
        }
        return result;
    }
}