#include <iostream>
#include <vector>
#include <string>
#include "move.h"
#include "creature.h"
using namespace std;

void Creature::showStats() {
    cout << name << endl;
    cout << "Health: " << health << endl;
    cout << "Speed: " << speed << endl;
    cout << "Attack: " << attack << endl;
    cout << "Defense: " << defense << endl;
    cout << "Accuracy:" << accuracy << endl;
    return;
}

void Creature::display() {
    cout << "1:" << moveList[0].display() << "   2:" << movelist[1].display() << endl;
    cout << "3:" << moveList[2].display() << "   4:" << movelist[3].display() << endl;
    return;
}

void Creature::Creature(int health, int speed, int attack, int defense, int accuracy) {
    this->health = health;
    this->speed = speed;
    this->attack = attack;
    this->defense = defense;
    this->accuracy = accuracy;

    /* Set Moves */
    return;
}