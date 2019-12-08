from IPython.display import display, HTML, Javascript
from time import sleep
from threading import Thread
import json

class Binder:
    instance = None
    
    
    @staticmethod
    def render():
        display(HTML('<canvas id="game" width="600px" height="600px" style="background: black;"></canvas>\
        <br/><button style="background-color: rgba(50, 50, 255, 0.6); margin-left: calc(50% - 50px); color: white; border-radius: 20px; border: none; width: 100px; height:50px; " onclick="window.game.stop()">STOP</button>\
        <div style="padding: 20px; background-color: white; border-radius: 20px; border: 1px solid rgba(200, 200, 200, 0.5);" id="console"></div>\
        <br/><div style="padding: 20px; color:red; background-color: rgba(255, 100, 100, .3); border-radius: 20px; border: 1px solid black;" id="errors"></div>'))
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
        try:
            new_data = self.callback(data)
            print(json.dumps(new_data))
        except Exception as err:
            print("JUPYTER_EXCEPTION")
            print(repr(err))
            print("END_JUPYTER_EXCEPTION")

def start(callback):
    Binder.register_callback(callback)
