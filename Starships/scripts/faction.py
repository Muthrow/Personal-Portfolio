from msilib.schema import Class
import arcade as arc
# from main import SCREEN_WIDTH
from ship import Capital, Fighter, Ship

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
FIGHTER_SCALING = .15
CAPITAL_SCALING = .25
SPAWN_GAP = 75


class Faction():
    """ A class to represent a faction being controlled by the player in the game """

    def __init__(self, style, side):
        self.turns = 0
        self.ships = arc.SpriteList()
        self.spawns = None
        self.fighter_scale = FIGHTER_SCALING
        self.capital_scale = CAPITAL_SCALING
        self.ship_cnt = [1,3]
        self.style = style
        # self.setup(style=style, side=side)

# Set faction specific settings
        if style == 1:
            self.fighter_scale *= 1.5
            self.capital_scale *= 1
            flip_x = False
            flip_y = True
            flip_diag = True
            fighter_sprite = "assets\sprites\Faction1\F5S1.png"
            capital_sprite = "assets\sprites\Faction1\F5S4.png"
        elif style == 2:
            self.fighter_scale *= .5
            self.capital_scale *= .65
            flip_x = False
            flip_y = False
            flip_diag = False
            fighter_sprite = "assets\sprites\Faction2\destroyer.png"
            capital_sprite = "assets\sprites\Faction2\carrier.png"
        elif style == 3:
            self.fighter_scale *= 1
            self.capital_scale *= 1.35
            flip_x = True
            flip_y = True
            flip_diag = True
            fighter_sprite = "assets\sprites\Faction3\\alien1.png"
            capital_sprite = "assets\sprites\Faction3\\alien2.png"
        elif style == 4:
            self.fighter_scale *= .8
            self.capital_scale *= 1.2
            flip_x = False
            flip_y = False
            flip_diag = False
            fighter_sprite = "assets\sprites\Faction4\\bluecruiser.png"
            capital_sprite = "assets\sprites\Faction4\\blueshuttlenoweps.png"

        if side == 1:
            spawn_agg_x = SCREEN_WIDTH/2
            spawn_agg_y = SPAWN_GAP
            self.spawns = [(spawn_agg_x,spawn_agg_y),(spawn_agg_x-SPAWN_GAP,spawn_agg_y),(spawn_agg_x,spawn_agg_y+SPAWN_GAP),(spawn_agg_x+SPAWN_GAP,spawn_agg_y)]
        if side == 2:
            spawn_agg_x = SCREEN_WIDTH-SPAWN_GAP
            spawn_agg_y = SCREEN_WIDTH/2
            self.spawns = [(spawn_agg_x,spawn_agg_y),(spawn_agg_x,spawn_agg_y+SPAWN_GAP),(spawn_agg_x-SPAWN_GAP,spawn_agg_y),(spawn_agg_x,spawn_agg_y-SPAWN_GAP)]
        if side == 3:
            spawn_agg_x = SCREEN_WIDTH/2
            spawn_agg_y = SCREEN_WIDTH-SPAWN_GAP
            self.spawns = [(spawn_agg_x,spawn_agg_y),(spawn_agg_x-SPAWN_GAP,spawn_agg_y),(spawn_agg_x,spawn_agg_y-SPAWN_GAP),(spawn_agg_x+SPAWN_GAP,spawn_agg_y)]
        if side == 4:
            spawn_agg_x = SPAWN_GAP
            spawn_agg_y = SCREEN_WIDTH/2
            self.spawns = [(spawn_agg_x,spawn_agg_y),(spawn_agg_x,spawn_agg_y+SPAWN_GAP),(spawn_agg_x,spawn_agg_y-SPAWN_GAP),(spawn_agg_x+SPAWN_GAP,spawn_agg_y)]




        self.ships.append(Capital(style, capital_sprite, scale=self.capital_scale, flipped_vertically=flip_x, flipped_horizontally=flip_y, flipped_diagonally=flip_diag, center_x=self.spawns[0][0], center_y=self.spawns[0][1]))
        for i in range(3):
            self.ships.append(Fighter(style, fighter_sprite, scale=self.fighter_scale, flipped_vertically=flip_x, flipped_horizontally=flip_y, flipped_diagonally=flip_diag, center_x=self.spawns[i+1][0], center_y=self.spawns[i+1][1]))

    def getShips(self):
        return self.ships
