class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        
        std::vector<int> new_nums;

        for (int num : nums) new_nums.push_back(num);
        for (int num : nums) new_nums.push_back(num);

        return new_nums;
    }
};