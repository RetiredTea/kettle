from kivy.uix.label import Label
from kivy.clock import Clock

class Seconds(Label):
    
    def __init__(self,total,**kwargs):
        self.done = False
        self.current = 0
        self.total = total 
        self.text = "Прошло секунд: " + str(self.current)
        super().__init__(**kwargs)
    
    def start(self):
        Clock.schedule_interval(self.change, 1 )

    def change(self, dt):
        self.current += 1
        self.text = ("Прошло секунд: " + str(self.current))
        if self.current >= self.total :
            self.done = True 
            return False 