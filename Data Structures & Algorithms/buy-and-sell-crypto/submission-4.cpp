class Solution {
public:
    int maxProfit(vector<int>& prices) {

        int smallest = prices[0];
        int dist = 0;

        for (int price : prices) {

            smallest = min(price, smallest);
            dist = max(dist, price - smallest);
        }
        return dist;
    }
};
