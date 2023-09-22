import kivy 
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider  
from settings import Settings
from EngimaGame import Color, EnigmaGame
kivy.require('2.0.0')

class EnigmaApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical', spacing=30, padding=100)
        self.widgets = {}
        self.create_menu_layout()  # Create initial layout
        self.settings = Settings()
        return self.root
    
    def create_menu_layout(self):
        self.root.clear_widgets()  # Clear existing widgets in the layout
        
        label_name = Label(text="Enigma", font_size=64, color=(100, 20, 30))
        self.root.add_widget(label_name)
        self.widgets["label_name"]=label_name

        play_button = Button(text="Play", font_size=32, size=(100, 50), on_press=self.change_layout) 
        self.root.add_widget(play_button)
        self.widgets["play_button"] = play_button
        
        settings_button = Button(text="Settings", font_size=32, size=(100, 50), on_press=self.change_layout)
        self.root.add_widget(settings_button)
        self.widgets["settings_button"] = settings_button
        
        quit_button = Button(text="Quit", font_size=32,on_press=self.change_layout)
        self.root.add_widget(quit_button)
        self.widgets["quit_button"]=quit_button
        
    def create_settings_layout(self):
        self.root.clear_widgets()
        windows = GridLayout(cols=4,rows=3)

        # Difficulty widgets
        label_diff = Label(text="Difficulty", font_size=32, color=(100, 20, 30))
        windows.add_widget(label_diff)
        self.widgets['label_diff'] = label_diff

        button_minus_diff = Button(text="-", font_size=32, size=(50, 50), on_press = self.change_setting)
        windows.add_widget(button_minus_diff)
        self.widgets['button_minus_diff'] = button_minus_diff

        button_plus_diff = Button(text="+", font_size=32, size=(50, 50),on_press = self.change_setting)
        windows.add_widget(button_plus_diff)
        self.widgets['button_plus_diff'] = button_plus_diff

        display_diff = Label(text=self.settings.mode, font_size=32, color=(100, 20, 30))
        windows.add_widget(display_diff)
        self.widgets['display_diff'] = display_diff

        # Code length widgets
        label_code_length = Label(text="Code length", font_size=32, color=(100, 20, 30))
        windows.add_widget(label_code_length)
        self.widgets["label_code_length"] = label_code_length

        button_minus_code_length = Button(text="-", font_size=32, size=(50, 50),on_press = self.change_setting)
        windows.add_widget(button_minus_code_length)
        self.widgets["button_minus_code_length"] = button_minus_code_length

        button_plus_code_length = Button(text="+", font_size=32, size=(50, 50),on_press = self.change_setting)
        windows.add_widget(button_plus_code_length)
        self.widgets["button_plus_code_length"] = button_plus_code_length

        display_code_length = Label(text=str(self.settings.code_length), font_size=32, color=(100, 20, 30))
        windows.add_widget(display_code_length)
        self.widgets["display_code_length"] = display_code_length

        # Number of colors widgets
        label_number_colors = Label(text="Colors", font_size=32, color=(100, 20, 30))
        windows.add_widget(label_number_colors)
        self.widgets["label_number_colors"] = label_number_colors

        button_minus_number_colors = Button(text="-", font_size=32, size=(50, 50),on_press = self.change_setting)
        windows.add_widget(button_minus_number_colors)
        self.widgets["button_minus_number_colors"] = button_minus_number_colors

        button_plus_number_colors = Button(text="+", font_size=32, size=(50, 50),on_press = self.change_setting)
        windows.add_widget(button_plus_number_colors)
        self.widgets["button_plus_number_colors"] = button_plus_number_colors

        display_number_colors = Label(text=str(self.settings.numbers_of_colors), font_size=32, color=(100, 20, 30))
        windows.add_widget(display_number_colors)
        self.widgets["display_number_colors"] = display_number_colors
    
        spacer_for_exit_button = BoxLayout(orientation='vertical', spacing=30, padding=100)
        spacer_for_exit_button.clear_widgets()
        menu_button = Button(text="menu", font_size=32, size=(50, 50),on_press = self.change_layout)
        spacer_for_exit_button.add_widget(menu_button)
        self.widgets["menu_button"] = menu_button
        self.root.add_widget(windows)        
        self.root.add_widget(spacer_for_exit_button)

    def change_layout(self, instance):
        if instance is self.widgets["play_button"]:
            pass
        elif instance is self.widgets["settings_button"]:
            self.create_settings_layout()
        elif instance is self.widgets["quit_button"]:
            quit()
        elif instance is  self.widgets["menu_button"]:
            self.create_menu_layout()

    def change_setting(self,instance):
        
        if instance is self.widgets["button_minus_diff"]:
            self.settings.mode = "EASY"
            self.widgets["display_diff"].text="EASY"
        
        elif instance is self.widgets["button_plus_diff"]:
            self.settings.mode = "HARD"
            self.widgets["display_diff"].text="HARD"
        
        elif instance is self.widgets["button_plus_code_length"]:
            current_length = self.settings.code_length
            if current_length < 5 :
                current_length = current_length + 1
                self.settings.code_length= current_length
                self.widgets["display_code_length"].text=str(self.settings.code_length)
        
        elif instance is self.widgets["button_minus_code_length"]:
            current_length = self.settings.code_length
            if current_length > 3 :
                current_length = current_length - 1
                self.settings.code_length= current_length
                self.widgets["display_code_length"].text=str(self.settings.code_length)
        
        elif instance is self.widgets["button_plus_number_colors"]:
            current_number = self.settings.numbers_of_colors
            if current_number < 12 :
                current_number = current_number + 1
                self.settings.numbers_of_colors= current_number
                self.widgets["display_number_colors"].text=str(self.settings.numbers_of_colors)
        
        elif instance is self.widgets["button_minus_number_colors"]:
            current_number = self.settings.numbers_of_colors
            if current_number > 3 :
                current_number = current_number - 1
                self.settings.numbers_of_colors= current_number
                self.widgets["display_number_colors"].text=str(self.settings.numbers_of_colors)



App = EnigmaApp()
App.run()
# class EnigmaApp(App):
#     def build(self):
#         return BoxLayout() 
    
# App = EnigmaApp()
# App.run()