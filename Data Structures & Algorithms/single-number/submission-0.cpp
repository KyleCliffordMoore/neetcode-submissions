class Solution {
public:
    int singleNumber(vector<int>& nums) {
        
        int curr = 0;
        for (int num : nums) {
            curr ^= num;
        }

        return curr;
    }
};
