from IPython.display import display, HTML, Javascript
from time import sleep
from threading import Thread
import json

class Binder:
    instance = None
    
    
    @staticmethod
    def render():
        display(HTML('<canvas id="game" width="600px" height="600px" style="background: url(https://thumbs.gfycat.com/HardtofindWildBarasingha-small.gif); background-size: cover;"></canvas>\
        <img id="sprites1" style="display:none" src="https://raw.githubusercontent.com/doplab/act-tp/master/images/sprites/frame_0_delay-0.25s.gif"/>\
        <img id="sprites2" style="display:none" src="https://raw.githubusercontent.com/doplab/act-tp/master/images/sprites/frame_1_delay-0.25s.gif"/>'))
        with open("./game.js", "r") as file:
            code = file.read()
            display(Javascript(code))
    
    @staticmethod
    def register_callback(count, callback):
        if Binder.instance is None:
            Binder.render()
            Binder.instance = Binder(callback)
            display(Javascript("window.game.start(%d)" % count))
        else:
            display(Javascript("if(window.game) window.game.stop()"))
            Binder.instance.callback = callback
            Binder.render()
            display(Javascript("window.game.start(%d)" % count))
    
    @staticmethod
    def update(data):
        Binder.instance.update(data)
    
    def __init__(self, callback):
        self.callback = callback
        
    def update_data(self, data):
        new_data = self.callback(data)
        print(json.dumps(new_data))        

def start(count, callback):
    Binder.register_callback(count, callback)
