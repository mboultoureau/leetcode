#include <regex>

class Solution {
public:
    int n = 0;
    unordered_map<int, string> urls;

    // Encodes a URL to a shortened URL.
    string encode(string longUrl) {
        n++;
        urls.emplace(n, longUrl);
        return "https://tinyurl.com/" + to_string(n);
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl) {
        std::smatch matches;
        std::regex_search(shortUrl, matches, std::regex("https://tinyurl.com/([0-9]+)"));
        if (matches.size() < 2)
        {
            return "";
        }

        return urls.at(stoi(matches[1]));
    }
};

// Your Solution object will be instantiated and called as such:
// Solution solution;
// solution.decode(solution.encode(url));