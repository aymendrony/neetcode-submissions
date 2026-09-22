#include <unordered_set>
#include <iostream>
class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {
        std::unordered_set<char> charset;
        int max_value = 0;
        int L = 0;
        for(int R=0; R< s.size();++R){
            while( charset.count(s[R])){
                charset.erase(s[L]);
                ++L;
            }
            charset.insert(s[R]);
            max_value = std::max(max_value,R-L+1);
        }
        return max_value;
    }
};
