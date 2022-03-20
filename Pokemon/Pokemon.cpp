// Pokemon.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include "creature.h"
#include "move.h"
using namespace std;


int main()
{
	// create our creatures
	int c1 = rand() % 4;
	int c2 = c1;
	while (c2 != c1) {
		c2 = rand() % 4;
	}

	switch (c1)
	{
	case 0:
		Dinosaur player;
	default:
		break;
	}
}
