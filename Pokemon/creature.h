/***********************************************************************
 * Header File:
 *    Creature: represents a creature used to battle
 * Author:
 *    Zack Pedersen
 * Summary:
 *    Represents a basic creature to battle
 ************************************************************************/
#include <iostream>
#include <vector>
#include <string>
#include "move.h"
using namespace std;

class Creature
{
    /* Represents a creature
    Name, Health, Attack, Speed, Defense, Accuracy, MoveList
    Creature(^^), display(), showStats()
    */
protected:
    /* data */
    int health;
    int speed;
    int attack;
    int defense;
    int accuracy;
    string name;
    vector<Move> moveList;

public:
    Creature(int health, int speed, int attack, int defense, int accuracy);
    void display();
    void showStats();
};

class Dinosaur: public Creature
{
    public:
        Dinosaur();
};