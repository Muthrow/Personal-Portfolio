#include <iostream>
#include <string>
#include "move.h"
using namespace std;

void Move::showStats() {
    cout << name << endl;
    cout << "Attack: " << attack << endl;
    cout << "Accuracy: " << accuracy << endl;
    cout << "PP: " << pp << endl;
}
