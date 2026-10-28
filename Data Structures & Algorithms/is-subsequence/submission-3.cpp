class Solution {
public:
    bool isSubsequence(string s, string t) {
        
        size_t i{};
        for (char target : s) {

            for (; i < t.size();) {

                char curr = t[i];
                ++i;

                if (curr == target)
                    goto endloop;

            }

            return false;
            endloop:

        }

        return true;
    }
};