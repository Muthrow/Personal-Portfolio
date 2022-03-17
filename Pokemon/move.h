/***********************************************************************
 * Header File:
 *    Creature: represents a creature used to battle
 * Author:
 *    Zack Pedersen
 * Summary:
 *    Represents a basic creature to battle
 ************************************************************************/

#include <iostream>
#include <string>
#using std;

class Move {
    private:
        /* stuff */
        string name;
        int attack;
        int accuracy;
        int pp;
        int affect
    public:
        Move();
        virtual void display();
        virtual void showStats();
};