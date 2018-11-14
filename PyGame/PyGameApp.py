import pygame
 
class PyGameApp:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._size = self._width, self._height = 800, 600
        self._framerate = 100
        self._sprites = {}
 
    def boundary(self):
        return (self._display_surf.get_rect())

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self._size)
        #self._display_surf = pygame.display.set_mode(self._size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._clock = pygame.time.Clock()
        self._running = True

    def add_sprite(self, name, sprite):
        self._sprites[name] = sprite

    def sprite(self, name):
        return self._sprites[name]

    def exit_app(self):
        self._running = False

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.exit_app()

    def on_loop(self):
        pass
    
    def on_render(self):
        for name, sprite in self._sprites.items():
            sprite.draw(self._display_surf)
    
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            self._clock.tick(self._framerate)
            
        self.on_cleanup()

