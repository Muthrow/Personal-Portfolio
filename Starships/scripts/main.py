""" Main Game Logic and Game Runner """
from ctypes import resize
from turtle import color, position
from unittest import runner
import arcade as arc
from matplotlib.pyplot import cla, draw
from sqlalchemy import false
from asteroid import Asteroid
from ship import Ship
from faction import Faction
import random

GAME_WIDTH = 700
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

SCREEN_TITLE = "Starships"
TILE_SCALING = .225
PLAYER_SCALE = .1
PLAYER_SPRITE = "assets\sprites\Faction2\cruiser.png"
MUSIC = "assets\sounds\music\I know your secret.mp3"
# MUSIC = "assets\sounds\music\Lord of The Rings (Calm Ambient Mix).mp3"
# MUSIC = "assets\sounds\music\\17 The Maw.mp3"
# FACTION = 2
ASTEROID_COUNT = 30
SPAWN_BUFFER = 30
TEAM_COUNT = 2

class Game(arc.Window):
    """ Main class for the application. """

    def __init__(self, width, height, title, resize):
        super().__init__(width, height, title, resize)

# Initialize lists
        self.background_color = arc.color.BLACK
        self.player1_list = arc.SpriteList()
        self.player2_list = arc.SpriteList()
        self.player3_list = arc.SpriteList()
        self.player4_list = arc.SpriteList()
        self.bullet_list = arc.SpriteList()
        self.physics_engine = None
        self.space_list = arc.SpriteList()
        self.basic_map = None
        self.scene = None
        self.background_list = arc.SpriteList()
        self.asteriod_list = arc.SpriteList()
        self.player = None
        self.select = False
        self.selected_list = arc.SpriteList()
        self.music = None
        self.player = None
        self.faction_list = list()
        self.turn = 1
        self.team_cnt = TEAM_COUNT

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

# Setup Asteroids
        # self.asteriod_list = arc.tilemap.process_layer(self.basic_map, "Asteriod-sprite", TILE_SCALING, use_spatial_hash=True)
        for each in range(ASTEROID_COUNT):
            spawn = (random.randint(SPAWN_BUFFER,GAME_WIDTH-SPAWN_BUFFER),random.randint(SPAWN_BUFFER,SCREEN_WIDTH-SPAWN_BUFFER))
            self.asteriod_list.append(Asteroid(position=spawn))
        # self.asteriod_object_list = arc.tilemap.process_layer(self.basic_map, "Asteriods", TILE_SCALING, use_spatial_hash=True)

# Setup Teams
# Team 1
        team1 = Faction(1,4)
        self.player1_list = team1.getShips()
        self.faction_list.append(team1)
# Team 2
        team2 = Faction(4,2)
        self.player2_list = team2.getShips()
        self.faction_list.append(team2)
# Team 3
        if self.team_cnt >= 3:
            team3 = Faction(2,3)
            self.player3_list = team3.getShips()
            self.faction_list.append(team3)
# Team 4
        if self.team_cnt >= 4:
            team4 = Faction(3,1)
            self.player4_list = team4.getShips()
            self.faction_list.append(team4)

        # for ship in team1.getShips():
            # print(ship.speed)
        # self.player = self.player1_list[0]
        self.selected_list = arc.SpriteList()
        # setup basic player
        # Setup Physics
        # self.physics_engine = arc.PhysicsEngineSimple(self.player, self.asteriod_list)

# Music
        self.music = arc.load_sound(MUSIC)
        # self.player = self.music.play()

    def on_draw(self):
        """ Draw Sprites """
# Clear the board before we draw again
        self.clear()
        self.background_list.draw()
# call draw on sprite lists
        self.player1_list.draw()
        self.player2_list.draw()
        self.player3_list.draw()
        self.player4_list.draw()
        # self.asteriod_object_list.draw()
        self.asteriod_list.draw()
        # self.asteriod_list.draw_hit_boxes(color=arc.color.WHITE)
        if self.select == True:
            self.player1_list.draw_hit_boxes(color=arc.color.WHITE)
        self.selected_list.draw_hit_boxes(color=arc.color.WHITE)
        self.bullet_list.draw()

    def on_update(self, delta_time: float):
        """ Game Logic. Updated Every Frame """

# call update on sprite lists
        self.background_list.update()
        # self.physics_engine.update()
        self.player1_list.update()
        self.player2_list.update()
        self.player3_list.update()
        self.player4_list.update()
        self.asteriod_list.update()
        self.bullet_list.update()
        for bullet in self.bullet_list:
            hit_list = arc.check_for_collision_with_list(bullet, self.asteriod_list)
            for faction in self.faction_list:
                hit_list.extend(arc.check_for_collision_with_list(bullet, faction.getShips()))
            if self.selected_list[0] in hit_list:
                hit_list.remove(self.selected_list[0])
            if len(hit_list) > 0:
                bullet.kill()
            for entity in hit_list:
                entity.hp -= bullet.damage

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
                # elif len(click_list) == 0:
                #     if len(self.selected_list) > 0:
                #         self.selected_list.pop()


def main():
    """ Main method """
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, False)
    window.setup()
    arc.run()


if __name__ == "__main__":
    main()