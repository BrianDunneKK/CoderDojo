import pygame

class PyGameSprite:
    def __init__(self):
        self._rect = pygame.Rect(0,0,0,0)
        self._sprite_surf = pygame.Surface((0, 0))

    def boundary(self):
        return self._rect

    def get_size(self):
        return [self._rect.w, self._rect.h]

    def get_x(self, which="lt"):
        x = self._rect.left
        if (which=="rt" or which=="rb" or which=="tr" or which=="br"):
            x = self._rect.right
        elif (which=="c"):
            x = self._rect.centerx
        return x

    def get_y(self, which="lt"):
        y = self._rect.top
        if (which=="lb" or which=="rb" or which=="bl" or which=="br"):
            y = self._rect.bottom
        elif (which=="c"):
            y = self._rect.centery
        return y

    def get_xy(self, which="lt"):
        return [self.get_x(which), self.get_y(which)]

    def set_x(self, x, which="lt"):
        if (which=="lt" or which=="lb" or which=="tl" or which=="bl"):
            self._rect.left = x
        elif (which=="rt" or which=="rb" or which=="tr" or which=="br"):
            self._rect.right = x
        elif (which=="c"):
            self._rect.centerx = x

    def set_y(self, y, which="lt"):
        if (which=="lt" or which=="rt" or which=="tl" or which=="tr"):
            self._rect.top = y
        elif (which=="lb" or which=="rb" or which=="bl" or which=="br"):
            self._rect.bottom = y
        if (which=="c"):
            self._rect.centery = y

    def set_xy(self, x, y, which="lt"):
        self.set_x(x, which)
        self.set_y(y, which)
        return self.get_xy(which)

    def set_xy_within(self, x, y, boundary, which="lt"):
        self.set_x(x, which)
        self.set_y(y, which)
        self._rect.clamp_ip(boundary)
        return self.get_xy(which)

    def collide_with(self, pygameImg):
        collide_rect = pygameImg.boundary()
        return self._rect.colliderect(collide_rect)

    def draw(self, surf):
        surf.blit(self._sprite_surf, self._rect)

class PyGameSprite_Image (PyGameSprite):
    def load_image(self, filename):
        self._sprite_surf = pygame.image.load(filename)
        self._rect = self._sprite_surf.get_rect()

class PyGameSprite_Text (PyGameSprite):
    def load_font(self, fontsize):
        self._font = pygame.font.Font(None, fontsize)

    def set_text(self, str, colour):
        self._text = str
        self._colour = colour
        self._sprite_surf = self._font.render(self._text, True, self._colour)
        self.set_xy(0, 0)

class PyGameSprite_Physics (PyGameSprite_Image):
    def __init__(self):
        super().__init__()
        self._speed = [0,0]

    def get_speed(self):
        return self._speed

    def set_speed(self, dx, dy):
        self._speed = [dx, dy]
        return self._speed

    def bounce_x(self):
        self._speed[0] = -self._speed[0]

    def bounce_y(self):
        self._speed[1] = -self._speed[1]

    def move_bounce(self, boundary):
        self._rect = self._rect.move(self._speed)
        if self._rect.left < 0 or self._rect.right > boundary.right:
            self.bounce_x()
        if self._rect.top < 0 or self._rect.bottom > boundary.bottom:
            self.bounce_y()
        return self.get_speed()

