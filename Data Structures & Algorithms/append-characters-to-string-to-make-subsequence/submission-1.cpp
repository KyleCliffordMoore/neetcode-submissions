class Solution {
public:
    int appendCharacters(string s, string t) {
        
        size_t i{};
        for (size_t target_i{}; target_i < t.size(); ++target_i) {
            char target = t[target_i];

            bool found = false;
            for (; i < s.size();) {
                char curr = s[i];
                ++i;

                if (curr == target) {
                    found = true;
                    break;
                }
                    

            }
            if (!found)
                return t.size() - target_i;

        }

        return 0;
    }
};