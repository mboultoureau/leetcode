class Solution {
private:
    static constexpr std::array<int, 12> daysInMonth = {
        31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
    };

public:
    static constexpr int toDayOfYear(std::string_view date) noexcept {
        int month = (date[0] - '0') * 10 + (date[1] - '0');
        int day   = (date[3] - '0') * 10 + (date[4] - '0');

        int daysBefore = std::accumulate(daysInMonth.begin(), daysInMonth.begin() + (month - 1), 0);
        
        return daysBefore + day;
    }
    
    int countDaysTogether(string arriveAlice, string leaveAlice, string arriveBob, string leaveBob) {
        int start = std::max(toDayOfYear(arriveAlice), toDayOfYear(arriveBob));
        int end   = std::min(toDayOfYear(leaveAlice),  toDayOfYear(leaveBob));

        return std::max(0, end - start + 1);
    }
};