// Kadane's Algorithm:
// Dynamic Programming

class Solution {
    public int maxSubArray(int[] nums) {
        int curr_max=0;
        int max=Integer.MIN_VALUE;
        for(int i=0; i<nums.length; i++) {
            curr_max = curr_max + nums[i];
            if(max<curr_max)
                max=curr_max;
            if(curr_max<0)
                curr_max=0;
        }
        return max;
    }
}