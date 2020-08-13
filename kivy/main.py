from kivy.app import App
from kivy.factory import Factory
from kivy.uix.filechooser import FileChooser
from kivy.utils import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.actionbar import *
from kivy.uix.popup import Popup

from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner

from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label


# from core import Steganography
# Window.size=(405,720) # full-hd
# Window.clearcolor = (255,12,34,0.5)

class FileDialog(FloatLayout):
    pass


class Root(BoxLayout):
    @staticmethod
    def hex(s):
        return get_color_from_hex(s)

    def load(self):
        content = FileDialog()
        self._popup = Popup(title="Load an Image", content=content, size_hint=(0.9, 0.9))
        self._popup.open()


class Header(ActionBar):
    pass


class ImageButton(ButtonBehavior, Image):
    pass


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
