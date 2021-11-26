from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.tab import MDTabsBase,MDTabs
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.widget import Widget
import re, math

Window.size = (300,550)
# ====================================================Class4
class Tab_Math_Class4(MDBoxLayout, MDTabsBase):
    '''content'''
class Screen_Topic_M4(MDScreen):
    pass
class Screen_Math_Logic(MDScreen):
    '''content'''
class Screen_Math_Probability(MDScreen):
    pass


class Tab_Physics_Class4(MDBoxLayout, MDTabsBase):
    '''content'''
class Screen_Topic_P4(MDScreen):
    pass
class Screen_Physics_Motion(MDScreen):
    '''content'''
class Screen_Physics_Force(MDScreen):
    pass

class Tab_Chemistry_Class4(MDBoxLayout, MDTabsBase):
    '''content'''
class Screen_Topic_C4(MDScreen):
    pass
class Screen_Chemistry_Mole_Conversion(MDScreen):
    '''content'''
class Screen_Chemistry_Gas_theory(MDScreen):
    pass
# ====================================================Class5
class Tab_Math_Class5(MDBoxLayout, MDTabsBase):
    '''content'''
class Tab_Physics_Class5(MDBoxLayout, MDTabsBase):
    '''content'''
class Tab_Chemistry_Class5(MDBoxLayout, MDTabsBase):
    '''content'''
# ====================================================Class6
class Tab_Math_Class6(MDBoxLayout, MDTabsBase):
    '''content'''
class Tab_Physics_Class6(MDBoxLayout, MDTabsBase):
    '''content'''
class Tab_Chemistry_Class6(MDBoxLayout, MDTabsBase):
    '''content'''



class BC_Calc(BoxLayout):
    def clear(self):
        self.ids.calc_input.text = "0"

    # Remove the last character
    def remove_last(self):
        prev_number = self.ids.calc_input.text
        prev_number = prev_number[:-1]
        self.ids.calc_input.text = prev_number

    # Getting the button value
    def button_press(self, number):
        prev_number = self.ids.calc_input.text

        if "wrong equation" in prev_number:
            prev_number = ''

        if prev_number == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f"{number}"

        else:
            self.ids.calc_input.text = f"{prev_number}{number}"


    def sings(self, add):
        prev_number = self.ids.calc_input.text
        self.ids.calc_input.text = f"{prev_number}{add}"

    # Getting decimal value
    def dot(self):
        prev_number = self.ids.calc_input.text
        num_list = re.split("\+|\*|\-|\/|\**", prev_number)

        if ("+" in prev_number or "-" in prev_number or "*" in prev_number or "/"  in prev_number or "**" in prev_number) and "." not in num_list[-1]:
            prev_number = f"{prev_number}."
            self.ids.calc_input.text = prev_number

        elif '.' in prev_number:
            pass

        else:
            prev_number = f'{prev_number}.'
            self.ids.calc_input.text = prev_number
    def sqrt(self):
        prev_number = self.ids.calc_input.text
        x = math.sqrt(int(prev_number))
        self.ids.calc_input.text = str(x)
    def negpow(self):
        prev_number = self.ids.calc_input.text
        x = 1/(int(prev_number))
        self.ids.calc_input.text = str(x)




    # Calculate the result
    def results(self):
        prev_number = self.ids.calc_input.text
        try:
            result = eval(prev_number)
            self.ids.calc_input.text = str(result)
        except:
            self.ids.calc_input.text = "wrong equation"

    # Positive to negative
    def positive_negative(self):
        prev_number = self.ids.calc_input.text
        if "-" in prev_number:
            self.ids.calc_input.text = f"{prev_number.replace('-', '')}"
        else:
            self.ids.calc_input.text = f"-{prev_number}"
    


class List(MDScreen):
    pass

class main(MDApp):
    def build(self):
        
        self.theme_cls.accent_palette = "Gray"
        self.theme_cls.primary_palette = "Brown"
        
        return Builder.load_file('Calc.kv')


        
        
    def on_start(self):
        self.root.ids.Tabs_Class4.add_widget(Tab_Math_Class4(text="Math"))
        self.root.ids.Tabs_Class4.add_widget(Tab_Physics_Class4(text="Physics"))
        self.root.ids.Tabs_Class4.add_widget(Tab_Chemistry_Class4(text="Chemistry"))

        self.root.ids.Tabs_Class5.add_widget(Tab_Math_Class5(text="Math"))
        self.root.ids.Tabs_Class5.add_widget(Tab_Physics_Class5(text="Physics"))
        self.root.ids.Tabs_Class5.add_widget(Tab_Chemistry_Class5(text="Chemistry"))

        self.root.ids.Tabs_Class6.add_widget(Tab_Math_Class6(text="Math"))
        self.root.ids.Tabs_Class6.add_widget(Tab_Physics_Class6(text="Physics"))
        self.root.ids.Tabs_Class6.add_widget(Tab_Chemistry_Class6(text="Chemistry"))



main().run()