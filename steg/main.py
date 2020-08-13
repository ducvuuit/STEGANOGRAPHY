from kivy.app import App
from kivy.factory import Factory
from kivy.uix.filechooser import FileChooser
from kivy.utils import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.actionbar import *


from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
# from core import Steganography
# Window.size=(405,720) # full-hd
# Window.clearcolor = (255,12,34,0.5)

class Root(BoxLayout):
    @staticmethod
    def hex(s):
        return get_color_from_hex(s)
    pass

class Header(ActionBar):
    pass




"""
Root:
    orientation: 'vertical'
    Header:
        canvas.before:
            Color:
                rgba: root.hex("00e676")
            Rectangle:
                pos: self.pos
                size: self.size
        size_hint: (1,0.1)
        Label:
            size_hint: (0.25,0.5)
            canvas.before:
                Color:
                    rgba: root.hex("00e676")
                Rectangle:
                    pos: self.pos
                    size: self.size
            text: 'Steggy'
            pos_hint: {'x': 0, 'y': 0.25}
            color: root.hex("000000")
            font_size: 50



    Button:
        text: 'aa'
"""



class LoadImage(FileChooser):
    pass


class Main(App):
    pass

class Selector(Label):
    pass


class Preview(BoxLayout):
    pass

class Header(Label):
    pass

Factory.register("Root",cls=Root)
Factory.register("Header",cls=Header)
Factory.register("Preview",cls=Preview)


if __name__ == '__main__':
    Main().run()
