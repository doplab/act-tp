from IPython.display import display, HTML, Javascript
from time import sleep
from threading import Thread
import json

class Binder:
    instance = None
    
    
    @staticmethod
    def render():
        display(HTML('<canvas id="game" width="400px" height="400px" style="background: url(https://i.pinimg.com/564x/68/72/6a/68726ab4f1e421b7dd328f7917e7be7a.jpg);"></canvas>'))
        with open("./game.js", "r") as file:
            code = file.read()
            display(Javascript(code))
    
    @staticmethod
    def register_callback(callback):
        if Binder.instance is None:
            Binder.render()
            Binder.instance = Binder(callback)
            display(Javascript("window.game.start()"))
        else:
            display(Javascript("if(window.game) window.game.stop()"))
            Binder.instance.callback = callback
            Binder.render()
            display(Javascript("window.game.start()"))
    
    @staticmethod
    def update(data):
        Binder.instance.update(data)
    
    def __init__(self, callback):
        self.callback = callback
        
    def update_data(self, data):
        new_data = self.callback(data)
        print(json.dumps(new_data))        

def start(callback):
    Binder.register_callback(callback)
