class Solution {
public:
    int scoreOfString(string s) {

        int score{};

        for (size_t i{}; i < s.size() - 1; ++i)
            score += abs(s[i] - s[i + 1]);

        return score;
    }
};