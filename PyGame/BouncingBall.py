from pygame import *
from PyGameApp import *
from PyGameSprite import *
from colour_constants import *

class BouncingBallApp(PyGameApp):
    def on_init(self):
        super().on_init()
        pygame.display.set_caption("Bouncing Ball")
        self.score = 0
        self.sprites = {}

        self.add_sprite("ball", PyGameSprite_Physics())
        self.sprite("ball").load_image("redball.png")
        self.sprite("ball").set_speed(5,5)

        self.add_sprite("bat", PyGameSprite_Image())
        self.sprite("bat").load_image("bat128x10.png")
        self.sprite("bat").set_x(self.boundary().width/2, "c")
        self.sprite("bat").set_y(self.boundary().height * 0.95, "tl")

        self.sprites["score"] = PyGameSprite_Text()
        self.sprites["score"].load_font(36)
        self.add_sprite("score", self.sprites["score"])

    def on_event(self, event):
        super().on_event(event)
        if event.type == pygame.KEYDOWN:
            if (event.key == K_q): # Q = Quit
                self.exit_app()
            elif (event.key == K_SPACE): # Space = Change direction
                speed = self.sprite("ball").get_speed()
                self.sprite("ball").set_speed(-speed[0], -speed[1])
        elif event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            y = self.sprite("bat").get_y("c")
            self.sprite("bat").set_xy_within(x, y, self.boundary(), "c")

    def on_loop(self):
        super().on_loop()
        self.sprite("ball").move_bounce(self.boundary())
        if self.sprite("ball").boundary().bottom >= self.boundary().bottom:
            self.sprite("ball").set_y(0)
        elif self.sprite("ball").collide_with(self.sprite("bat")):
            self.sprite("ball").bounce_y()
            self.score += 1

        self.sprites["score"].set_text(str(self.score), colours["black"])
        self.sprites["score"].set_xy(self.boundary().width/2, self.boundary().height * 0.05,"c")

    def on_render(self):
        self._display_surf.fill(colours["burlywood"])
        super().on_render()
        pygame.display.flip()

theApp = BouncingBallApp()
theApp.on_execute()
