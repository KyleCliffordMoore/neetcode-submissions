class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        
        std::set<int> canidates;

        for (int num : nums) {

            if (canidates.find(num) != canidates.end())
                return true;

            canidates.insert(num);
        }

        return false;

    }
};