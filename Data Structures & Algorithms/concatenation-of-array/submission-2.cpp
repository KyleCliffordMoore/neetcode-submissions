class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        
        vector<int> toReturn;

        for (int num : nums) toReturn.push_back(num);
        for (int num : nums) toReturn.push_back(num);

        return toReturn;

    }
};