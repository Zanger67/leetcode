class Solution {
public:
    int minDifference(vector<int>& nums) {
        if (nums.size() <= 4) 
            return 0;

        int top4[4] = {nums[0], nums[1], nums[2], nums[3]};
        sort(top4, top4 + 4);
        int bot4[4] = {top4[3], top4[2], top4[1], top4[0]};

        for (int i = 4; i < nums.size(); i++) {
            if (nums[i] > top4[3]) {
                top4[0] = top4[1];
                top4[1] = top4[2];
                top4[2] = top4[3];
                top4[3] = nums[i];
            } else if (nums[i] > top4[2]) {
                top4[0] = top4[1];
                top4[1] = top4[2];
                top4[2] = nums[i];
            } else if (nums[i] > top4[1]) {
                top4[0] = top4[1];
                top4[1] = nums[i];
            } else if (nums[i] > top4[0]) {
                top4[0] = nums[i];
            }

            if (nums[i] < bot4[3]) {
                bot4[0] = bot4[1];
                bot4[1] = bot4[2];
                bot4[2] = bot4[3];
                bot4[3] = nums[i];
            } else if (nums[i] < bot4[2]) {
                bot4[0] = bot4[1];
                bot4[1] = bot4[2];
                bot4[2] = nums[i];
            } else if (nums[i] < bot4[1]) {
                bot4[0] = bot4[1];
                bot4[1] = nums[i];
            } else if (nums[i] < bot4[0]) {
                bot4[0] = nums[i];
            }
        }

        int a = (top4[3] - bot4[0] < top4[2] - bot4[1]) ? top4[3] - bot4[0] : top4[2] - bot4[1];
        int b = (top4[1] - bot4[2] < top4[0] - bot4[3]) ? top4[1] - bot4[2] : top4[0] - bot4[3];
        return (a < b) ? a : b;
    }
};
