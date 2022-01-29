""" Main Game Logic and Game Runner """
from ctypes import resize
from msilib.schema import Class
import arcade as arc
from matplotlib.pyplot import cla

class Game(arc.Window):
    """ Main class for the application. """

    def __init__(self, width, height, title, resize):
        super().__init__(width, height, title, resize)


myGame = Game(600,800,"Your Mom",False)
