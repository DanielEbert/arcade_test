from __future__ import annotations

import arcade
from pyglet.math import Vec2

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCROLL_SPEED = 2

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.WHITE)
        self.middle_mouse_button_held = False
        self.camera = arcade.Camera(self.width, self.height)
        self.camera.scale = 2
        self.mouse_pos_x = 0
        self.mouse_pos_y = 0

    def setup(self):
        ...

    def on_draw(self):
        self.clear()
        self.camera.use()

        arcade.draw_circle_filled(100, 100, 50, arcade.color.YELLOW)
        arcade.draw_circle_filled(500, 500, 50, arcade.color.BLACK)

        arcade.draw_text(text=f'{self.mouse_pos_x} {self.mouse_pos_y}', start_x=10, start_y=20, color=arcade.color.BLACK, font_size=14)

    def set_mouse_pos(self, mouse_pos_x: int, mouse_pos_y: int) -> tuple[int, int]:
        camera_center_x = self.camera.position[0] + self.camera.viewport_width / 2
        camera_center_y = self.camera.position[1] + self.camera.viewport_height / 2

        self.mouse_pos_x = (mouse_pos_x - camera_center_x) * self.camera.scale + camera_center_x
        self.mouse_pos_y = (mouse_pos_y - camera_center_y) * self.camera.scale + camera_center_y

    def on_update(self, delta_time: float):
        pass

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        # Don't move the camera here. This is for zooming.
        pass

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_MIDDLE:
            self.middle_mouse_button_held = True

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_MIDDLE:
            self.middle_mouse_button_held = False

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.set_mouse_pos(round(x + self.camera.position[0]), round(y + self.camera.position[1]))
        if self.middle_mouse_button_held:
            self.camera.move(self.camera.position - Vec2(dx * SCROLL_SPEED, dy * SCROLL_SPEED))

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()


