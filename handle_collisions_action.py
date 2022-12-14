import constants
import pyray
from drawable import Drawable
from action import Action
from point import Point

class handle_collision_actions(Action):


    def __init__(self):
        self._game_over = False

    def execute(self, cast):

        if not self._game_over:
            self._handle_trails_collision(cast)
            self._handle_game_over(cast)

    def _handle_trails_collision_old(self, cast):

        bike1 = cast.get_first_actor("players")
        head1 = bike1.get_actors()[0]
        trails1 = bike1.get_actors()
        bike2 = cast.get_second_actor("players")
        head2 = bike2.get_actors()[0]
        trails2 = bike2.get_actors()
        
        print(len(trails1))
        for trail in trails1:
            if trail != head1 and head1.get_position().equals(trail.get_position()):
                self._game_over = True
            if head1.get_position().equals(trails2.get_position()):
                self._game_over = True

        print(len(trails2))
        for trail in trails2:
            if trail != head2 and head2.get_position().equals(trail.get_position()):
                self._game_over = True
            if head2.get_position().equals(trails1.get_position()):
                self._game_over = True

        #Eastons code end

    def _handle_trails_collision(self, cast):

        bike1 = cast.get_first_actor("players")
        head1 = bike1.get_actors()[0]
        trails = bike1.get_actors()
        bike2 = cast.get_second_actor("players")
        head2 = bike2.get_actors()[0]
        trails2 = bike2.get_actors()
        print(len(trails))
        for trail in trails:
            if trail != head1 and head1.get_position().equals(trail.get_position()):
                self._game_over = True
            if head2.get_position().equals(trail.get_position()):
                self._game_over = True
            for trail2 in trails2:
                if head1.get_position().equals(trail2.get_position()):
                    self._game_over = True
                if trail2 != head2 and head2.get_position().equals(trail2.get_position()):
                    self._game_over = True
        
    def _handle_game_over(self, cast):

        if self._game_over:
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x,y)
            

            message = Drawable()
            message = Drawable()
            pyray.begin_drawing()
            pyray.clear_background(pyray.BLACK)
            message.set_text("The Game is Over!")
            message.set_position(position)
            cast.add_actor("messages", message)