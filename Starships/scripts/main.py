""" Main Game Logic and Game Runner """
from ctypes import resize
from msilib.schema import Class
from operator import le
from pydoc import cli
from turtle import color
from unittest import runner
import arcade as arc
import click
from matplotlib.pyplot import cla, draw
from sqlalchemy import false
from ship import Ship
from faction import Faction

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Starships"
TILE_SCALING = .225
PLAYER_SCALE = .1
PLAYER_SPRITE = "assets\sprites\Faction2\cargoship.png"
MUSIC = "assets\sounds\music\Lord of The Rings (Calm Ambient Mix).mp3"


class Game(arc.Window):
    """ Main class for the application. """

    def __init__(self, width, height, title, resize):
        super().__init__(width, height, title, resize)
        self.background_color = arc.color.BLACK
        self.player1_list = arc.SpriteList()
        self.player2_list = arc.SpriteList()
        self.bullet_list = arc.SpriteList()
        self.physics_engine = None
        self.space_list = arc.SpriteList()
        self.basic_map = None
        self.scene = None
        self.background_list = arc.SpriteList()
        self.asteriod_list = arc.SpriteList()
        # self.asteriod_object_list = None
        self.player = None
        self.select = False
        self.selected_list = arc.SpriteList()
        self.music = None
        self.player = None

    def setup(self):
        # setup sprites and sprite lists

        # Setup Map
        map_name = "assets\Starship test.tmx"
        layer_options = {
            "Platforms": {
                "use_spatial_hash": True,
            },
        }
        self.basic_map = arc.tilemap.read_tmx(map_name)
        self.background_list = arc.tilemap.process_layer(self.basic_map,"Background",TILE_SCALING)
        self.asteriod_list = arc.tilemap.process_layer(self.basic_map, "Asteriod-sprite", TILE_SCALING, use_spatial_hash=True)
        # self.asteriod_object_list = arc.tilemap.process_layer(self.basic_map, "Asteriods", TILE_SCALING, use_spatial_hash=True)

        team1 = Faction(1,1)
        self.player1_list = team1.getShips()
        for ship in team1.getShips():
            print(ship.speed)
        # self.player = self.player1_list[0]
        self.selected_list = arc.SpriteList()
        # setup basic player
        # Setup Physics
        # self.physics_engine = arc.PhysicsEngineSimple(self.player, self.asteriod_list)

        self.music = arc.load_sound(MUSIC)
        self.player = self.music.play()

    def on_draw(self):
        self.clear()
        self.background_list.draw()
        # call draw on sprite lists
        self.player1_list.draw()
        # self.asteriod_object_list.draw()
        self.asteriod_list.draw()
        # self.asteriod_list.draw_hit_boxes(color=arc.color.WHITE)
        if self.select == True:
            self.player1_list.draw_hit_boxes(color=arc.color.WHITE)
        self.selected_list.draw_hit_boxes(color=arc.color.WHITE)
        self.bullet_list.draw()

    def on_update(self, delta_time: float):
        # game logic
        # call update on sprite lists
        self.background_list.update()
        # self.physics_engine.update()
        self.player1_list.update()
        self.asteriod_list.update()
        self.bullet_list.update()

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        if key == arc.key.SPACE:
            self.select = True

        if key == arc.key.D:
            self.selected_list.pop()

    def on_key_release(self, key, modifiers):
        """
        Called when the user releases a key.
        """
        if key == arc.key.SPACE:
            self.select = False

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):

        if button == arc.MOUSE_BUTTON_RIGHT and len(self.selected_list) == 1:
            attacker = self.selected_list[0]
            self.bullet_list.append(attacker.shoot(x, y))

        if button == arc.MOUSE_BUTTON_LEFT and len(self.selected_list) == 1 and len(arc.get_sprites_at_point((x,y),self.player1_list)) == 0:
            runner = self.selected_list[0]
            runner.setMove((x, y))

        if button == arc.MOUSE_BUTTON_LEFT:
                click_list = arc.get_sprites_at_point((x,y),self.player1_list)
                if len(click_list) > 0:
                    if len(self.selected_list) > 0:
                        self.selected_list.pop()
                    self.selected_list.append(click_list.pop())
                elif len(click_list) == 0:
                    if len(self.selected_list) > 0:
                        self.selected_list.pop()


def main():
    """ Main method """
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, False)
    window.setup()
    arc.run()


if __name__ == "__main__":
    main()