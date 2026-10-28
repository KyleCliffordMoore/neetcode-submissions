class Solution {
public:

    int toIdx(char c) {
        return c - 'a';
    }

    bool isAnagram(string s, string t) {
        
        int word1[26];
        int word2[26];

        for (char c : s) word1[toIdx(c)] += 1;
        for (char c : t) word2[toIdx(c)] += 1; 

        for (size_t i{}; i < 26 ; ++i) std::cout << word1[i] << ", " << word2[i] << '\n';

        for (size_t i{}; i < 26 ; ++i)
            if (word1[i] != word2[i])
                return false;

        return true;
    }
};
