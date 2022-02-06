import arcade as arc

IMG_FILE = "assets\sprites\\Asteroid\\asteroid-big-0000.png"
BREAK_SOUND = arc.load_sound("assets\sounds\sound effects\Chunky Explosion.mp3")

SCALE = .15

class Asteroid(arc.Sprite):
    """ A class to represent an asteroid """
    def __init__(self, position, filename: str = IMG_FILE, scale: float = SCALE, image_x: float = 0, image_y: float = 0, image_width: float = 0, image_height: float = 0, center_x: float = 0, center_y: float = 0, repeat_count_x: int = 1, repeat_count_y: int = 1, flipped_horizontally: bool = False, flipped_vertically: bool = False, flipped_diagonally: bool = False, mirrored: bool = None, hit_box_algorithm: str = "Simple", hit_box_detail: float = 4.5):
        adj = scale * 5
        self.hp = 50 * adj
        self.bump_damage = 8 * adj
        center_x = position[0]
        center_y = position[1]
        super().__init__(filename, scale, image_x, image_y, image_width, image_height, center_x, center_y, repeat_count_x, repeat_count_y, flipped_horizontally, flipped_vertically, flipped_diagonally, mirrored, hit_box_algorithm, hit_box_detail)

    def update(self):
        if self.hp <= 0:
            self.kill()
            self.music = BREAK_SOUND
            self.player = self.music.play()
        return super().update()