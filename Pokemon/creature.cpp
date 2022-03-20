#include <iostream>
#include <vector>
#include <string>
#include "move.h"
#include "creature.h"
using namespace std;

void Creature::showStats() {
    /* Display the stats for the creature in a list type format */
    cout << name << endl;
    cout << "Health: " << health << endl;
    cout << "Speed: " << speed << endl;
    cout << "Attack: " << attack << endl;
    cout << "Defense: " << defense << endl;
    cout << "Accuracy:" << accuracy << endl;
    return;
}

void Creature::display() {
    /* Display the menu for the Creature */
    cout << "1: ";
    moveList[0].display();
    cout << "   2:";
    moveList[1].display();
    cout << endl;
    cout << "3: ";
    moveList[2].display();
    cout << "   4:";
    moveList[3].display();
    cout << endl;
    return;
}

Creature::Creature(int health, int speed, int attack, int defense, int accuracy) {
    /* Constructor */
    this->health = health;
    this->speed = speed;
    this->attack = attack;
    this->defense = defense;
    this->accuracy = accuracy;
    /* Set Moves */
    return;
}