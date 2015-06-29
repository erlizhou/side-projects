#include <iostream>
#include <random>
#include <vector>

using namespace std;

struct suitdistribution {
    vector<int> lefthand, righthand;
};

void calculateProbability() {
    int total = 1000000;
    int count = 0;
    int remainhand[6] = {13,11,5,4,3,2};  //suppose 6 cards are K,J,5,4,3,2
    for (int i = 0; i < total; i++) {
        suitdistribution s;
        int randomdistribution;
        for (int j = 0; j < 6; j++) {
            randomdistribution = rand() % 2; //returns either 0 or 1
            if(randomdistribution == 0)
                s.lefthand.push_back(remainhand[j]); //put hand in either left or right hand
            else
                s.righthand.push_back(remainhand[j]);
        }
        if (s.lefthand.size() == 3 && s.lefthand[0] == 13)  //case when left hand has K tripleton
                count++;
        if ((s.lefthand.size() == 2 && s.lefthand[0] == 11) || (s.righthand.size() == 2 && s.righthand[0] == 11))  //case when either hand has J doubleton
                count++;
        if ((s.lefthand.size() == 2 && s.lefthand[0] == 13 && s.lefthand[1] == 11) || (s.righthand.size() == 2 && s.righthand[0] == 13 && s.righthand[1] == 11)) //case when either hand has K and J doubleton
                count++;
    }
    cout << double(count)/total << endl;
}

void calculateProbability1() {
    int total = 1000000;
    int count = 0;
    int remainhand[6] = {13,11,5,4,3,2};  //suppose 6 cards are K,J,5,4,3,2
    for (int i = 0; i < total; i++) {
        suitdistribution s;
        int randomdistribution;
        for (int j = 0; j < 6; j++) {
            randomdistribution = rand() % 2; //returns either 0 or 1
            if(randomdistribution == 0)
                s.lefthand.push_back(remainhand[j]); //put hand in either left or right hand
            else
                s.righthand.push_back(remainhand[j]);
        }
        if (s.lefthand.size() == 3 && s.lefthand[0] == 13)  //case when left hand has K tripleton
                count++;
        if ((s.lefthand.size() == 2 && s.lefthand[0] == 11) || (s.righthand.size() == 2 && s.righthand[0] == 11))  //case when either hand has J doubleton
                count++;
        if ((s.lefthand.size() == 2 && s.lefthand[0] == 13 && s.lefthand[1] == 11) || (s.righthand.size() == 2 && s.righthand[0] == 13 && s.righthand[1] == 11)) //case when either hand has K and J doubleton
                count++;
        if (s.righthand.size() == 2 && s.righthand[0] == 11)  //case when left hand has K doubleton
                count++;
        if ((s.lefthand.size() == 1 && s.lefthand[0] == 11)||s.righthand.size() == 1 && s.righthand[0] == 11)  //case when either hand has J singleton
                count++;

    }
    cout << double(count)/total << endl;
}

int main()
{
    calculateProbability();
    calculateProbability1();
    return 0;
}
