
class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double sum1 = 0;
        for (int i=0; i<k; i++){
            sum1 += nums[i];
        }
        double sum2 = sum1;
        for(int i = k;i<nums.length;i++){
            sum2 += nums[i]-nums[i-k];
            sum1 = Math.max(sum1, sum2);
        }
        return sum1/k;
        
    }
}