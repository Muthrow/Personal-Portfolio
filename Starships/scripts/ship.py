import arcade as arc
from bullet import Bullet
import math

MOVE_SPEED = 2
DECELERATION = .6
FIGHTER_HEALTH = 25
CAPITAL_HEALTH = 200
CAPITAL_LASER = "assets\sprites\Lasers\Laser Sprites\\11.png"
FIGHTER_LASER = "assets\sprites\Lasers\Laser Sprites\\06.png"
PEW = "assets\sounds\sound effects\laser.wav"
EXPLOSION_SOUND = "assets\sounds\sound effects\\rock_breaking.flac"

class Ship(arc.Sprite):
    def __init__(self, faction: int, filename: str, scale: float = 1, image_x: float = 0, image_y: float = 0, image_width: float = 0, image_height: float = 0, center_x: float = 0, center_y: float = 0, repeat_count_x: int = 1, repeat_count_y: int = 1, flipped_horizontally: bool = False, flipped_vertically: bool = False, flipped_diagonally: bool = False, mirrored: bool = None, hit_box_algorithm: str = "Simple", hit_box_detail: float = 4.5):
        super().__init__(filename, scale, image_x, image_y, image_width, image_height, center_x, center_y, repeat_count_x, repeat_count_y, flipped_horizontally, flipped_vertically, flipped_diagonally, mirrored, hit_box_algorithm, hit_box_detail)
        self.speed = None
        self.decel = .4
        self.laser_file = FIGHTER_LASER
        self.destination = self.position
        self.pew = arc.load_sound(PEW)
        self.hp = 20
        self.faction = faction
        self.move_distance = 100

        # self.decel = DECELERATION

    def move(self):
        """ Takes a destination and a power and moves in the specified Direction """
        if self.collides_with_point(self.destination):
            self.change_x = 0
            self.change_y = 0

    def setMove(self, destination):
        """ Sets the destination of the ship """
        self.destination = destination
        dest_x = destination[0]
        dest_y = destination[1]

        angle_x = dest_x - self.center_x
        angle_y = dest_y - self.center_y
        angle = math.atan2(angle_y, angle_x)

        self.change_x = math.cos(angle) * self.speed
        self.change_y = math.sin(angle) * self.speed

        self.angle = math.degrees(angle)

    def update(self):
        self.move()
        if self.hp <= 0:
            self.kill()
            self.music = arc.load_sound(EXPLOSION_SOUND)
            self.player = self.music.play()
        return super().update()


    def shoot(self, target_x, target_y):
        """ Fires a shot in the direction of the destination """
        print('pew pew')
        arc.play_sound(self.pew)
        laser = Bullet(self.laser_file, origin=self, scale=.1)
        laser.position = self.position
        angle_x = target_x - laser.center_x
        angle_y = target_y - laser.center_y
        angle = math.atan2(angle_y, angle_x)

        laser.change_x = math.cos(angle) * laser.speed
        laser.change_y = math.sin(angle) * laser.speed

        laser.angle = math.degrees(angle)

        return laser



class Fighter(Ship):
    def __init__(self, faction: int, filename: str, scale: float = 1, image_x: float = 0, image_y: float = 0, image_width: float = 0, image_height: float = 0, center_x: float = 0, center_y: float = 0, repeat_count_x: int = 1, repeat_count_y: int = 1, flipped_horizontally: bool = False, flipped_vertically: bool = False, flipped_diagonally: bool = False, mirrored: bool = None, hit_box_algorithm: str = "Simple", hit_box_detail: float = 4.5):
        super().__init__(faction, filename, scale, image_x, image_y, image_width, image_height, center_x, center_y, repeat_count_x, repeat_count_y, flipped_horizontally, flipped_vertically, flipped_diagonally, mirrored, hit_box_algorithm, hit_box_detail)
        self.speed = MOVE_SPEED
        self.hp = FIGHTER_HEALTH
        self.laser_file = FIGHTER_LASER

class Capital(Ship):
    def __init__(self, faction: int, filename: str, scale: float = 1, image_x: float = 0, image_y: float = 0, image_width: float = 0, image_height: float = 0, center_x: float = 0, center_y: float = 0, repeat_count_x: int = 1, repeat_count_y: int = 1, flipped_horizontally: bool = False, flipped_vertically: bool = False, flipped_diagonally: bool = False, mirrored: bool = None, hit_box_algorithm: str = "Simple", hit_box_detail: float = 4.5):
        super().__init__(faction, filename, scale, image_x, image_y, image_width, image_height, center_x, center_y, repeat_count_x, repeat_count_y, flipped_horizontally, flipped_vertically, flipped_diagonally, mirrored, hit_box_algorithm, hit_box_detail)
        self.speed = MOVE_SPEED/2
        self.hp = CAPITAL_HEALTH
        self.laser_file = CAPITAL_LASER

    def shoot(self, target_x, target_y):
        laser = super().shoot(target_x, target_y)
        laser.damage = 20
        return laser