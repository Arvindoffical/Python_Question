
class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double sum1 = 0;
        for (int i=0; i<k; i++){
            sum1 += nums[i];
        }
        double sum2 = sum1;
        int j =0;
        for(int i = k;i<nums.length;i++){
            sum2 += nums[i]-nums[j];
            sum1 = Math.max(sum1, sum2);
            j++;
        }
        return sum1/k;
        
    }
}