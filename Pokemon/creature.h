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
#include <move.h>
#using std::vector;
#using std;

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
        Creature();
        virtual void display();
        virtual void showStats();

};