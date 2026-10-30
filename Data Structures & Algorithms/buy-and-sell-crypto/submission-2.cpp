class Solution {
public:
    int maxProfit(vector<int>& prices) {

        int smallest{prices[0]};
        int diff{};

        for (int curr : prices) {
            smallest = min(smallest, curr);
            diff = max(diff, curr - smallest);
        }
        return diff;
    }
};
