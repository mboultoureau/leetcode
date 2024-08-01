class Solution {
public:
    int countSeniors(vector<string>& details) {
        int seniors = 0;
        for (const std::string& person : details)
        {
            if (std::stoi(person.substr(11, 2)) > 60)
            {
                seniors += 1;
            }
        }

        return seniors;
    }
};