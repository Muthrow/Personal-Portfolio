import arcade as arc
from bullet import Bullet
import math
from arcade import Color

MOVE_SPEED = 2
DECELERATION = .6
FIGHTER_HEALTH = 25
CAPITAL_HEALTH = 100
CAPITAL_LASER = "assets\sprites\Lasers\Laser Sprites\\11.png"
FIGHTER_LASER = "assets\sprites\Lasers\Laser Sprites\\06.png"
PEW = "assets\sounds\sound effects\laser.wav"
EXPLOSION_SOUND = "assets\sounds\sound effects\\rock_breaking.flac"

class Ship(arc.Sprite):
    def __init__(self, faction: int, filename: str, scale: float = 1, center_x: float = 0, center_y: float = 0,flipped_horizontally: bool = False, flipped_vertically: bool = False, flipped_diagonally: bool = False):
        super().__init__(filename, scale, center_x, center_y, flipped_horizontally, flipped_vertically, flipped_diagonally)
        self.speed = None
        self.decel = .4
        self.laser_file = FIGHTER_LASER
        self.destination = self.position
        self.pew = arc.load_sound(PEW)
        self.hp = 20
        self.bump_damage = 10
        self.faction = faction
        self.move_distance = 100
        self.range = 300
        self.has_gone = False
        self.is_moving = False
        self.touching_list = arc.SpriteList()

        # self.decel = DECELERATION

    def move(self):
        """ Takes a destination and a power and moves in the specified Direction """
        if self.collides_with_point(self.destination):
            self.change_x = 0
            self.change_y = 0
            self.is_moving = False

    def setMove(self, destination):
        """ Sets the destination of the ship """
        dest_x = destination[0]
        dest_y = destination[1]

        angle_x = dest_x - self.center_x
        angle_y = dest_y - self.center_y
        angle = math.atan2(angle_y, angle_x)

        self.change_x = math.cos(angle) * self.speed
        self.change_y = math.sin(angle) * self.speed

        self.angle = math.degrees(angle)

        self.destination = destination

        self.has_gone = True
        self.is_moving = True

        return True


    def update(self):
        if self.is_moving == True:
            self.move()
        # for item in self.touching_list:
            # pass
        if self.has_gone == True and self.is_moving == False:
            self.alpha = 100
        else:
            self.alpha = 255
        if self.hp <= 0:
            self.kill()
            self.music = arc.load_sound(EXPLOSION_SOUND)
            self.player = self.music.play()
        return super().update()


    def shoot(self, target_x, target_y):
        """ Fires a shot in the direction of the destination """
        arc.play_sound(self.pew)
        angle_x = target_x - self.center_x
        angle_y = target_y - self.center_y
        angle = math.atan2(angle_y, angle_x)
        destination = [self.center_x+self.range * math.cos(angle), self.center_y+self.range * math.sin(angle)]


        laser = Bullet(self.laser_file, origin=self, destination=destination, scale=.1)
        laser.position = self.position
        laser.change_x = math.cos(angle) * laser.speed
        laser.change_y = math.sin(angle) * laser.speed
        laser.angle = math.degrees(angle)

        self.has_gone = True

        return laser

    def showStats(self):
        """ Prints our ships stats to the console """
        print(f'Health: {self.hp}\nPosition: {self.position}\nFaction: {self.faction}')


class Fighter(Ship):
    def __init__(self, filename: str, scale, center_x: float = 0, center_y: float = 0,flipped_horizontally: bool = False, flipped_vertically: bool = False, flipped_diagonally: bool = False):
        super().__init__(filename, scale, center_x, center_y, flipped_horizontally, flipped_vertically, flipped_diagonally)
        self.speed = MOVE_SPEED
        self.hp = FIGHTER_HEALTH
        self.laser_file = FIGHTER_LASER
        self.bump_damage = 10

class Capital(Ship):
    def __init__(self, filename: str, scale, center_x: float = 0, center_y: float = 0,flipped_horizontally: bool = False, flipped_vertically: bool = False, flipped_diagonally: bool = False):
        super().__init__(filename, scale, center_x, center_y, flipped_horizontally, flipped_vertically, flipped_diagonally)
        self.speed = MOVE_SPEED/2
        self.hp = CAPITAL_HEALTH
        self.laser_file = CAPITAL_LASER
        self.bump_damage = 8
        self.range = 500

    def shoot(self, target_x, target_y):
        laser = super().shoot(target_x, target_y)
        laser.damage = 20
        return laser