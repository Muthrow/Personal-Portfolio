#include <iostream>
#include <string>
#include "move.h"
using namespace std;

void Move::showStats() {
    /* Show the stats for the selected action */
    cout << name << endl;
    cout << "Attack: " << attack << endl;
    cout << "Accuracy: " << accuracy << endl;
    cout << "PP: " << pp << endl;
}

TailSlap::TailSlap() {
    name = "Tail Slap";
    attack = 20;
    accuracy = 90;
    pp = 10;
    affect = 0;
    return;
};