#include <iostream>
#include <string>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    int characterReplacement(const std::string& s, int k) {
        std::unordered_map<char, int> freq;  
        int left = 0;
        int maxCount = 0;  
        int res = 0;

        for (int right = 0; right < s.size(); ++right) {
            freq[s[right]]++;
            maxCount = std::max(maxCount, freq[s[right]]);

            
            while ((right - left + 1) - maxCount > k) {
                freq[s[left]]--;
                left++;
            }

            
            res = std::max(res, right - left + 1);
        }

        return res;
    }
};

