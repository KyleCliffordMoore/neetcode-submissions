class Solution {
public:

    void print_vector(vector<int>& vec) {
        std::cout << "[";
        for (int c : vec)
            std::cout << c << ", ";
        std::cout << "]\n";
    }

    void print_vector_vector(vector<vector<int>>& vec) {

        std::cout << "[\n";
        for (vector<int>& v : vec)
            print_vector(v);
        std::cout << "]\n";

    }

    vector<int> topKFrequent(vector<int>& nums, int k) {
        
        vector<int> result;
        
        unordered_map<int, int> counts;
        for (int num : nums)
            ++counts[num];

        vector<vector<int>> buckets(nums.size() + 1); // No such thing of 0 count
        for (pair<const int, int>& count : counts)
            buckets[count.second].push_back(count.first);

        for (int i{static_cast<int>(buckets.size() - 1)}; i >= 0; --i) {
            while (!buckets[i].empty()) {

                if (k == 0)
                    return result;
                --k;
                result.push_back(buckets[i].back());
                buckets[i].pop_back();
            }
        }


        return result;
    }
};
