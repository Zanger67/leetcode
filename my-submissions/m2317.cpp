class Solution {
public:
    int maximumXOR(vector<int>& nums) {
        int output = 0;

        for (int num : nums) {
            output |= num;
        }

        return output;
    }
};