from kivy.app import App
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.uix.filechooser import FileChooser
from kivy.uix.widget import Widget
from kivy.graphics import *

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
# from core import Steganography
Window.size=(405,720) # full-hd
Window.clearcolor = (255,0,0,1)


class LoadImage(FileChooser):
    pass


class SteganoGraphyApp(App):
    pass

class Root(BoxLayout):
    orientation = "vertical"
    pass
class Preview(BoxLayout):
    orientation = 'vertical'
class Header(Label):
    pass

Factory.register("Root",cls=Root)
Factory.register("Header",cls=Header)
Factory.register("Preview",cls=Preview)
if __name__ == '__main__':
    SteganoGraphyApp().run()
