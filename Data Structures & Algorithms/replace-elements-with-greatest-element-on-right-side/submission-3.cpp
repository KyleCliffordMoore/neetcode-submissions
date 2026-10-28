class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        
        int largest{arr[arr.size() - 1]};
        vector<int> to_return{-1};

        for (size_t i{arr.size() - 1}; i >= 1;) {
            --i;

            to_return.push_back(largest);
            largest = max(arr[i], largest);

        }
        std::reverse(to_return.begin(), to_return.end());

        return to_return;

    }
};