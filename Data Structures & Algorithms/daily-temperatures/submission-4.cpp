class Solution {
public:

    // create dup
    void printStack(stack<pair<int, int>> stk) {
        std::cout << " top [ ";
        while (!stk.empty()) {
            auto pr = stk.top();
            std::cout << "{ " << pr.first << ", " << pr.second << " }  ";
            stk.pop(); 
        }
        std::cout << "] bottom \n";
    }

    vector<int> dailyTemperatures(vector<int>& temperatures) {

        // Stack -- > [(30, idx), ]    
        // Next  -- > 38, nidx
        // if top < next then place (nidx - idx) in idx and pop
        // otherwise

        // init a return vector prefilled w/ 0s the size of temp
        vector<int> result(temperatures.size());

        stack<pair<int, int>> searching_temps;

        for (int curr_idx = 0; curr_idx < temperatures.size(); ++curr_idx) {

            int curr_val = temperatures[curr_idx];

            while (!searching_temps.empty()) {
                int top_val = searching_temps.top().first;
                int top_idx = searching_temps.top().second;

                if (top_val >= curr_val)
                    break;

                result[top_idx] = curr_idx - top_idx;
                searching_temps.pop();
            }

            searching_temps.push({temperatures[curr_idx], curr_idx});
        }

        return result;
    }
};
