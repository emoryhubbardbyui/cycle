import constants
from color import Color
from point import Point
from drawable import Drawable

class Player1:



    def __init__(self):

        self._text = ""
        self._font_size = 15
        self._color = Color(245,245,245)
        quarter_of_width = constants.CELL_SIZE * 15
        half_of_height = int(constants.MAX_Y / 2)
        self._position = Point(quarter_of_width, half_of_height)
        self._velocity = Point(0,0)
        self._trails = []

        trail = Drawable()
        trail.set_position(self._position)
        trail.set_velocity(Point(0, 0))
        trail.set_text("@")
        trail.set_color(self._color)
        self._trails.append(trail)

    def add_trail(self):
        self._trail = Drawable()
        #use previous position to generate trail there and NOT STEP ON IT
        self._trail.set_position(self._old_position)
        self._trail.set_velocity(Point(0, 0))
        self._trail.set_text("#")
        self._trail.set_color(self._color)
        self._trails.append(self._trail)
    
    def get_color(self):

        return self._color

    def get_font_size(self):

        return self._font_size

    def get_position(self):

        return self._position

    def get_velocity(self):

        return self._velocity

    def move_next(self):

        x = (self._position.get_x() + self._velocity.get_x()) % constants.MAX_X
        y = (self._position.get_y() + self._velocity.get_y()) % constants.MAX_Y
        self._old_position = self._position
        self._position = Point(x, y)
        if not self._velocity.equals(Point(0, 0)): #only add trail if it moves
            self.move_first_trail()
      
    def move_first_trail(self):
        self._trails[0].move_next()
        self.add_trail()

    def set_color(self,color):

        self._color = color

    def set_position(self, position):
        self._position = position

    def set_font_size(self,font_size):

        self._font_size = font_size

    def set_velocity(self, velocity):

        self._velocity = velocity

    def set_text(self, text):

        self._text = text

    def get_text(self):
        return self._text

    def turn_bike(self, velocity):
        print("bike turned")
        self.set_velocity(velocity)
        self._trails[0].set_velocity(velocity)

    def has_actors(self):
        return True

    def get_actors(self):
        return self._trails