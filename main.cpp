#include <iostream>
#include <vector>
using namespace std;

struct dataPoint {
    int education;
    int income;
};

int main()
{
    vector<int> education = {9, 10, 11, 12};
    vector<int> income = {30000, 35000, 40000, 45000};

    vector<dataPoint> plot(4);

    for (int i = 0; i < income.size(); i++)
    {
        plot[i].education = education[i];
        plot[i].income = income[i];
    }

    int sumIncome = 0;

    for (int i = 0; i < plot.size(); i++)
    {
        sumIncome = sumIncome + plot[i].income;
    }

    cout << sumIncome / income.size() << endl;

    return 0;
}