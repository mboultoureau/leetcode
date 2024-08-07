class Solution {
public:
    void numberToUnit(int num, vector<string>& english)
    {
        switch (num)
        {
            case 1:
                english.push_back("One"); break;
            case 2:
                english.push_back("Two"); break;
            case 3:
                english.push_back("Three"); break;
            case 4:
                english.push_back("Four"); break;
            case 5:
                english.push_back("Five"); break;
            case 6:
                english.push_back("Six"); break;
            case 7:
                english.push_back("Seven"); break;
            case 8:
                english.push_back("Eight"); break;
            case 9:
                english.push_back("Nine"); break;
        }
    }

    void numberToTens(int num, vector<string>& english)
    {
        if (num < 10) numberToUnit(num, english);
        else if (num == 10) english.push_back("Ten");
        else if (num == 11) english.push_back("Eleven");
        else if (num == 12) english.push_back("Twelve");
        else if (num == 13) english.push_back("Thirteen");
        else if (num == 14) english.push_back("Fourteen");
        else if (num == 15) english.push_back("Fifteen");
        else if (num == 16) english.push_back("Sixteen");
        else if (num == 17) english.push_back("Seventeen");
        else if (num == 18) english.push_back("Eighteen");
        else if (num == 19) english.push_back("Nineteen");
        else if (num < 30)  english.push_back("Twenty");
        else if (num < 40)  english.push_back("Thirty");
        else if (num < 50)  english.push_back("Forty");
        else if (num < 60)  english.push_back("Fifty");
        else if (num < 70)  english.push_back("Sixty");
        else if (num < 80)  english.push_back("Seventy");
        else if (num < 90)  english.push_back("Eighty");
        else if (num < 100) english.push_back("Ninety");

        if (num > 20)
        {
            numberToUnit(num % 10, english);
        }
    }

    void numberToHundreds(int num, vector<string>& english)
    {
        if (num / 100 == 0)
        {
            numberToTens(num, english);
            return;
        }

        numberToUnit(num / 100, english);
        english.push_back("Hundred");
        numberToTens(num % 100, english);
    }

    void numberToThousands(int num, vector<string>& english)
    {
        if (num / 1'000 == 0)
        {
            numberToHundreds(num, english);
            return;
        }

        numberToHundreds(num / 1'000, english);
        english.push_back("Thousand");
        numberToHundreds(num % 1'000, english);
    }

    void numberToMillions(int num, vector<string>& english)
    {
        if (num / 1'000'000 == 0)
        {
            numberToThousands(num, english);
            return;
        }

        numberToThousands(num / 1'000'000, english);
        english.push_back("Million");
        numberToThousands(num % 1'000'000, english);
    }

    void numberToBillions(int num, vector<string>& english)
    {
        if (num / 1'000'000'000 == 0)
        {
            numberToMillions(num, english);
            return;
        }

        numberToMillions(num / 1'000'000'000, english);
        english.push_back("Billion");
        numberToMillions(num % 1'000'000'000, english);
    }

    string numberToWords(int num)
    {
        if (num == 0)
        {
            return "Zero";
        }

        vector<string> english;
        string result;
        numberToBillions(num, english);

        for (int i = 0; i < english.size(); i++)
        {
            result += english[i];
            if (i != english.size() - 1)
            {
                result += " ";
            }
        }

        return result;
    }
};