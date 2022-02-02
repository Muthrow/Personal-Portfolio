from msilib.schema import Class
import arcade as arc
from ship import Capital, Fighter, Ship

FIGHTER_SCALING = .1
CAPITAL_SCALING = .2
SPAWN = 100

class Faction():
    """ A class to represent a faction being controlled by the player in the game """

    def __init__(self, style, side):
        self.turns = 3
        self.ships = arc.SpriteList()
        # self.setup(style=style, side=side)

    # def setup(self, style, side):
        if style == 1:
            flip_x = False
            flip_y = True
            flip_diag = True
            fighter_sprite = "assets\sprites\Faction1\F5S1.png"
            capital_sprite = "assets\sprites\Faction1\F5S4.png"
            laser_sprite = "assets\sprites\Faction1\laser.png"
        elif style == 2:
            flip_x = False
            flip_y = False
            flip_diag = False
            fighter_sprite = "assets\sprites\Faction2\destroyer.png"
            capital_sprite = "assets\sprites\Faction2\carrier.png"
            laser_sprite = "assets\sprites\Faction2\laser.png"
        elif style == 3:
            flip_x = True
            flip_y = True
            flip_diag = True
            fighter_sprite = "assets\sprites\Faction3\\alien1.png"
            capital_sprite = "assets\sprites\Faction3\\alien4.png"
            laser_sprite = "assets\sprites\Faction3\laser.png"
        elif style == 4:
            flip_x = False
            flip_y = False
            flip_diag = False
            fighter_sprite = "assets\sprites\Faction4\\bluecruiser.png"
            capital_sprite = "assets\sprites\Faction4\\bluedestroyer.png"
            laser_sprite = "assets\sprites\Faction4\laser.png"

        # self.ships.append(arc.Sprite(capital_sprite, flipped_vertically=flip_x, flipped_horizontally=flip_y, flipped_diagonally=flip_diag, center_x=30, center_y=30))
        # for i in range(3):
        #     self.ships.append(arc.Sprite(fighter_sprite, flipped_vertically=flip_x, flipped_horizontally=flip_y, flipped_diagonally=flip_diag, center_x=i*10+10, center_y=20))


        self.ships.append(Capital(capital_sprite, scale=CAPITAL_SCALING, flipped_vertically=flip_x, flipped_horizontally=flip_y, flipped_diagonally=flip_diag, center_x=SPAWN, center_y=SPAWN, laser_name=laser_sprite))
        for i in range(3):
            self.ships.append(Fighter(fighter_sprite, scale=FIGHTER_SCALING, flipped_vertically=flip_x, flipped_horizontally=flip_y, flipped_diagonally=flip_diag, center_x=i*50+SPAWN-50, center_y=SPAWN-50, laser_name=laser_sprite))

    def getShips(self):
        return self.ships
