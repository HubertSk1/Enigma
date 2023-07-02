import kivy 
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
kivy.require('2.0.0')

class EnigmaApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical', spacing=30, padding=100)
        self.create_initial_layout()  # Create initial layout
        return self.root
    
    def create_initial_layout(self):
        self.root.clear_widgets()  # Clear existing widgets in the layout
        
        self.root.add_widget(Label(text="Enigma", font_size=64, color=(100, 20, 30)))
        self.root.add_widget(Button(text="Play", font_size=32, size=(100, 50), on_press=self.change_layout))
        self.root.add_widget(Button(text="Settings", font_size=32, size=(100, 50), on_press=self.change_layout))
        self.root.add_widget(Button(text="Quit", font_size=32,on_press=self.change_layout))

    def create_new_layout(self):
        self.root.clear_widgets()  # Clear existing widgets in the layout
        
        grid_layout = GridLayout(cols=3, rows=4, spacing=10)  # Create the grid layout
        
        for x in range(grid_layout.cols*grid_layout.rows):
            grid_layout.add_widget(Button(text=str(x), font_size=32, size=(10,20 ), on_press=self.change_layout))
        

        self.root.add_widget(grid_layout)
    
    def change_layout(self, instance):
        if instance.text == "Play":
            self.create_new_layout()
        else:
            pass

App = EnigmaApp()
App.run()
# class EnigmaApp(App):
#     def build(self):
#         return BoxLayout() 
    
# App = EnigmaApp()
# App.run()