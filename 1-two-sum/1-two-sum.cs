public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        int[] index = new int[2];

            for (int i = 0; i < nums.Length; i++)
            {
                for (int j = i+1; j < nums.Length; j++)
                {
                    if (nums[j] == target - nums[i])
                    {
                        index[0] = i;
                        index[1] = j;
                        
                    }

                }

            }
           
            return index;
    
    
}
}