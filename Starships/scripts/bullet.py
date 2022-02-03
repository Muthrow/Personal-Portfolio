import arcade
from matplotlib.pyplot import cla

class Bullet(arcade.Sprite):
    '''Generic projectile.'''

    def __init__(self, filename: str, scale: float = 1, image_x: float = 0, image_y: float = 0, image_width: float = 0, image_height: float = 0, center_x: float = 0, center_y: float = 0, repeat_count_x: int = 1, repeat_count_y: int = 1, flipped_horizontally: bool = False, flipped_vertically: bool = False, flipped_diagonally: bool = False, mirrored: bool = None, hit_box_algorithm: str = "Simple", hit_box_detail: float = 4.5):
        super().__init__(filename, scale, image_x, image_y, image_width, image_height, center_x, center_y, repeat_count_x, repeat_count_y, flipped_horizontally, flipped_vertically, flipped_diagonally, mirrored, hit_box_algorithm, hit_box_detail)
        self.speed = 5
        self.damage = 25

    def update(self):
        if self.center_x < 0 or self.center_x > 700 or self.center_y < 0 or self.center_y > 700:
            self.kill()
        return super().update()