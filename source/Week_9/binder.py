from IPython.display import display, HTML, Javascript
from time import sleep
from threading import Thread
import json

class Binder:
    instance = None
    
    
    @staticmethod
    def render():
        display(HTML('<canvas id="game" width="600px" height="600px" style="background: url(http://giphygifs.s3.amazonaws.com/media/sIIhZliB2McAo/200.gif); background-size: cover;"></canvas>\
        <img id="sprites" style="display:none" src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/da113cba-7663-4d97-9cd6-f832ffc6f79f/d1dpbih-c9e042fb-c81a-43c6-9652-2f1fabb57dad.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2RhMTEzY2JhLTc2NjMtNGQ5Ny05Y2Q2LWY4MzJmZmM2Zjc5ZlwvZDFkcGJpaC1jOWUwNDJmYi1jODFhLTQzYzYtOTY1Mi0yZjFmYWJiNTdkYWQuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.q6ov5px5-ayc6XGUII47foBqdq0vkyMSKc-4r0I5L0k"/>'))
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
