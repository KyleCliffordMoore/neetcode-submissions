class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        
        set<int> vals;

        for (int num : nums) {
            if (vals.count(num))
                return true;
            vals.insert(num);
        }
        return false;
    }
};