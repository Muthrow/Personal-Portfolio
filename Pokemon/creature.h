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
    private:
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

class Dinosaur::Creature
{
    public:
        Dinosaur();
}