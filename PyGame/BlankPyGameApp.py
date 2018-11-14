from PyGameApp import *
from colour_constants import *

class MyPyGameApp(PyGameApp):
    def on_init(self):
        super().on_init()

    def on_event(self, event):
        super().on_event(event)
            
    def on_loop(self):
        super().on_loop()

    def on_render(self):
        super().on_render()
    
theApp = MyPyGameApp()
theApp.on_execute()
