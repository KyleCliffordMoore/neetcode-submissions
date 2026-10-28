class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int, int> hashmap;

        for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
            int diff = target - nums[i];

            if (hashmap.contains(diff))
                return {hashmap.at(diff), i};

            hashmap[nums[i]] = i;
        }

        return {};

    }
};
