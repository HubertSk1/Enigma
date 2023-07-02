from settings import Settings
from random import randint
from copy import copy
import colorsys

class Color:
    def __init__(self,name,ID,color):
        self.name = name
        self.ID = ID
        self.color = color

class EnigmaGame:
    def __init__(self,settings:Settings):
       self.settings = settings
       self.colors = self.get_colors()
       self.code = self.get_code()
    
    def get_code(self):
        code=[]
        for a in range (self.settings.code_length):    
            code.append(randint(a=1,b=self.settings.numbers_of_colours))
        return(code)
    
    def get_colors(self):
        colors = []
        for i in range(self.settings.numbers_of_colours):
            hue = i / self.settings.numbers_of_colours  
            r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
            r = int(r * 255)
            g = int(g * 255)
            b = int(b * 255)
            C = Color(None,i+1,(r, g, b))
            colors.append(C)
        return colors

    def guess_password(self,code:list,guess:list):
        if self.settings.mode == "HARD":
            correct_place, wrong_place, misses = 0,0,0
            # Check digits in the correct place
            for i in range(len(code)):
                if code[i] == guess[i]:
                    correct_place += 1

            # Check digits in the wrong place
            code_digits = list(code)
            for i in range(len(code)):
                if code[i] != guess[i] and guess[i] in code_digits:
                    wrong_place += 1
                    code_digits.remove(guess[i])
            #Check misses
            misses = len(code) - correct_place - wrong_place            
            result=[2] * correct_place + [1] * wrong_place + [0] * misses  
        
        if self.settings.mode == "EASY":
            availabe_digits = copy(code)
            # availabe_digits.reverse()
            result=[0]* len(code)
            for index, ele in enumerate (guess):
                if ele == code[index]:
                    result[index] = 2
                    availabe_digits.remove(ele)
            for index, ele in enumerate (guess):
                if ele in availabe_digits and ele !=code[index]:
                    result[index] = 1
                    availabe_digits.remove(ele)
            # for index, ele in enumerate (guess):
            #     if ele not in availabe_digits and ele !=code[index]:
            #         result[index] = 0
        return(result)
    
set = Settings()
game = EnigmaGame(set)

print(game.guess_password(game.code,[1,2,3,4]))
print(game.guess_password(game.code,[6,6,7,8]))

