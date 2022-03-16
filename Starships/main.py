""" Main Game Logic and Game Runner """
from importlib.resources import path
import os
import sys
import arcade as arc
import random
from asteroid import Asteroid
from ship import Ship
from faction import Faction

path = "C:\code\BYU-I\\2022-Winter\Applied Programming\Personal Portfolio\Personal-Portfolio\Starships"
GAME_WIDTH = 700
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Starships"
TILE_SCALING = .225
# MUSIC = "assets\sounds\music\I know your secret.mp3"
# MUSIC = "assets\sounds\music\Lord of The Rings (Calm Ambient Mix).mp3"
MUSIC = "assets\sounds\music\\17 The Maw.mp3"
# FACTION = 2
ASTEROID_COUNT = 60
SPAWN_BUFFER = 20
TEAM_COUNT = 3
ACTION_CNT = 3
ASTEROID_SCALE = .2

class Game(arc.Window):
    """ Main class for the application. """

    def __init__(self, width, height, title, resize, players):
        super().__init__(width, height, title, resize)
# Initialize lists
        self.background_color = arc.color.BLACK
        self.player1_list = arc.SpriteList()
        self.player2_list = arc.SpriteList()
        self.player3_list = arc.SpriteList()
        self.player4_list = arc.SpriteList()
        self.ship_list = arc.SpriteList()
        self.bullet_list = arc.SpriteList()
        self.physics_engine = None
        self.space_list = arc.SpriteList()
        # self.basic_map = None
        self.scene = None
        self.background_list = arc.SpriteList()
        self.asteriod_list = arc.SpriteList()
        self.player = None
        self.select = False
        self.selected_list = arc.SpriteList()
        self.music = None
        self.player = None
        self.faction_list = list()
        self.turn = 0
        self.team_cnt = players
        self.active_team = None

    def setup(self):
        """ setup sprites and sprite lists """
# Setup Map
        map_name = "assets\Starship test.tmx"
        # self.basic_map = arc.TileMap(map_name)
        # self.basic_map = arc.tilemap.read_tmx(map_name)
        # self.background_list = arc.tilemap.process_layer(self.basic_map,"Background",TILE_SCALING)


# Setup Teams
    # Team 1 (Gets first turn)
        team1 = Faction(1,4)
        self.active_team = team1
        self.player1_list = team1.getShips()
        self.ship_list.extend(self.player1_list)
        self.faction_list.append(team1)
    # Team 2
        team2 = Faction(4,2)
        self.player2_list = team2.getShips()
        self.ship_list.extend(self.player2_list)
        self.faction_list.append(team2)
    # Team 3
        if self.team_cnt >= 3:
            team3 = Faction(2,3)
            self.player3_list = team3.getShips()
            self.ship_list.extend(self.player3_list)
            self.faction_list.append(team3)
    # Team 4
        if self.team_cnt >= 4:
            team4 = Faction(3,1)
            self.player4_list = team4.getShips()
            self.ship_list.extend(self.player4_list)
            self.faction_list.append(team4)

        self.selected_list = arc.SpriteList()

# Setup Asteroids
        i = 0
        while i <= ASTEROID_COUNT:
            spawn = (random.randint(SPAWN_BUFFER,GAME_WIDTH-SPAWN_BUFFER),random.randint(SPAWN_BUFFER,GAME_WIDTH-SPAWN_BUFFER))
            scale = random.normalvariate(.9,.5)
            new_asteroid = Asteroid(position=spawn,scale=scale*ASTEROID_SCALE)
            if len(arc.check_for_collision_with_list(new_asteroid, self.ship_list)) == 0:
                self.asteriod_list.append(new_asteroid)
                i += 1


# Music
        self.music = arc.load_sound(MUSIC)
        # self.player = self.music.play()

    def on_draw(self):
        """ Draw Sprites """
# Clear the board before we draw again
        self.clear()
        # self.basic_map.draw()
# call draw on sprite lists
        self.player1_list.draw()
        self.player2_list.draw()
        self.player3_list.draw()
        self.player4_list.draw()
        self.asteriod_list.draw_hit_boxes(color=arc.color.WHITE)
        self.asteriod_list.draw()
        if self.select == True:
            self.active_team.getShips().draw_hit_boxes(color=arc.color.WHITE)
        self.selected_list.draw_hit_boxes(color=arc.color.WHITE)
        self.bullet_list.draw()

    def on_update(self, delta_time: float):
        """ Game Logic. Updated Every Frame """

# call update on sprite lists
        # self.basic_map.update()
        self.player1_list.update()
        self.player2_list.update()
        self.player3_list.update()
        self.player4_list.update()
        self.asteriod_list.update()
# Bullet logic
        self.bullet_list.update()
        for bullet in self.bullet_list:
    # Check for collision with asteroids
            hit_list = arc.check_for_collision_with_list(bullet, self.asteriod_list)
    # Check for collision with ALL ships
            hit_list.extend(arc.check_for_collision_with_list(bullet, self.ship_list))
    # Ignore the ship that made the shot
            if bullet.origin in hit_list:
                hit_list.remove(bullet.origin)
    # If we hit anything, remove the bullet and deliver damage
            for entity in hit_list:
                entity.hp -= bullet.damage
            if len(hit_list) > 0:
                bullet.kill()

# Crash Logic
        for ship in self.ship_list:
    # Asteroid crashing
            bump_list = arc.check_for_collision_with_list(ship, self.asteriod_list)
    # Ship crashing
            bump_list.extend(arc.check_for_collision_with_list(ship, self.ship_list))
            if len(bump_list) > 0:
                ship.hp -= bump_list[0].bump_damage
                bump_list[0].hp -= ship.bump_damage

# Turn Logic
        if self.active_team.has_turns() == False:
            self.active_team.reset()
            self.turn += 1
            self.active_team = self.faction_list[self.turn%self.team_cnt]
            if len(self.selected_list) > 0:
                self.selected_list.pop()


    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        if key == arc.key.SPACE:
            self.select = True

        if key == arc.key.D:
            if len(self.selected_list) > 0:
                self.selected_list.pop()

        if key == arc.key.S:
            self.selected_list[0].showStats()

        if key == arc.key.T:
            self.active_team.endTurn()

        if key == arc.key.P:
            self.selected_list[0].hp = -1

    def on_key_release(self, key, modifiers):
        """
        Called when the user releases a key.
        """
        if key == arc.key.SPACE:
            self.select = False

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):

# Shoot
        if button == arc.MOUSE_BUTTON_RIGHT and len(self.selected_list) == 1:
            attacker = self.selected_list[0]
            if attacker.has_gone == False:
                self.bullet_list.append(attacker.shoot(x, y))
                self.active_team.turns += 1
                self.selected_list.pop()

# Move
        if button == arc.MOUSE_BUTTON_LEFT and len(self.selected_list) == 1 and len(arc.get_sprites_at_point((x,y),self.player1_list)) == 0:
            runner = self.selected_list[0]
            if runner.has_gone == False:
                runner.setMove((x, y))
                self.active_team.turns += 1
                self.selected_list.pop()

# Select
        if button == arc.MOUSE_BUTTON_LEFT:
                click_list = arc.get_sprites_at_point((x,y),self.active_team.getShips())
                if len(click_list) > 0:
                    if len(self.selected_list) > 0:
                        self.selected_list.pop()
                    self.selected_list.append(click_list.pop())


def main():
    """ Main method """
    invalid = True
    # players = 4
    while invalid:
        try:
            players = int(input('How many players (2-4)'))
            pass
        except:
            print("Invalid player count")
        if players >= 2 and players <= 4:
            invalid = False
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, False, players)
    window.setup()
    arc.run()


if __name__ == "__main__":
    # Pyinstaller stuff
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        os.chdir(sys._MEIPASS)
    main()