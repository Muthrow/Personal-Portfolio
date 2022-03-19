/***********************************************************************
 * Header File:
 *    Move: represents and action a creature can take in a battle
 * Author:
 *    Zack Pedersen
 * Summary:
 *    One of the actions a creature can take during a battle.
 ************************************************************************/

#include <iostream>
#include <string>
using namespace std;

class Move {
    private:
        /* stuff */
        string name;
        int attack;
        int accuracy;
        int pp;
        int affect;
         /*
            Health = 0
            Speed = 1
            Attack = 2
            Defense = 3
            Accuracy = 4
          */
    public:
        Move::Move();
        void display() { std::cout << name << "  (" << pp << ")"; }
        void showStats();
}

class TailSlap::Move {
    TailSlap::TailSlap() {
        name = "Tail Slap"
        attack = 20;
        accuracy = 90;
        pp = 10;
        affect = 0;
        return;
    }
}

class Bite::Move {
    Bite::Bite() {
        name = "Bite"
        attack = 34;
        accuracy = 100;
        pp = 5;
        affect = 0;
        return;
    }
}

class Scratch::Move {
    Scratch::Scratch() {
        name = "Scratch"
        attack = 15;
        accuracy = 100;
        pp = 15;
        affect = 0;
        return;
    }
}

class Kick::Move {
    Kick::Kick() {
        name = "Kick"
        attack = 30;
        accuracy = 80;
        pp = 10;
        affect = 0;
        return;
    }
}

class SandBlast::Move {
    SandBlast::SandBlast() {
        name = "Sand Blast"
        attack = 20;
        accuracy = 80;
        pp = 10;
        affect = 4;
        return;
    }
}

class SheildBreak::Move {
    SheildBreak::SheildBreak() {
        name = "Sheild Break"
        attack = 20;
        accuracy = 80;
        pp = 10;
        affect = 3;
        return;
    }
}

class Intimidate::Move {
    Intimidate::Intimidate() {
        name = "Intimidate"
        attack = 20;
        accuracy = 60;
        pp = 15;
        affect = 2;
        return;
    }
}

class KCBreak::Move {
    KCBreak::KCBreak() {
        name = "Shatter Knee-Caps"
        attack = 40;
        accuracy = 90;
        pp = 15;
        affect = 1;
        return;
    }
}
