from kivy.lang import Builder
from kivy.factory import Factory
from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivy.core.window import Window

Builder.load_string(
    """
<AppUI@BoxLayout>:
    orientation: "vertical"

    MDToolbar:
        id: toolbar
        title: app.title
        md_bg_color: app.theme_cls.primary_color
        background_palette: "Primary"
        elevation: 10
        left_action_items: [["menu", lambda x: None]]

    ScrollView:
        size_hint_x: None
        width: box.width
        pos_hint: {"center_x": .5}
        bar_width: 0

        BoxLayout:
            id: box
            padding: dp(10)
            size_hint: None, None
            size: self.minimum_size
            spacing: dp(10)
            orientation: "vertical"
            pos_hint: {"center_x": .5}

            BoxLayout:
                size_hint: None, None
                width: self.minimum_width
                height: dp(56)
                spacing: "10dp"

            MDRoundFlatIconButton:
                text: "Upload container image"
                icon: "file-upload"
                width: dp(200)
                pos_hint: {"center_x": .5}
                on_release: app.file_manager_open()

            MDRoundFlatIconButton:
                text: "Upload data image"
                icon: "file-upload"
                width: dp(200)
                pos_hint: {"center_x": .5}
                on_release: app.file_manager_open()

            MDRectangleFlatButton:
                text: "Process"
                pos_hint: {"center_x": .5}
                on_release: app.process()

            Line:
                

"""
)


class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "STEGANOGRAPHY"
        self.theme_cls.primary_palette = "Green"
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager, 
            select_path=self.select_path, 
        )

    def build(self):
        self.root = Factory.AppUI()
    
    def file_manager_open(self):
        self.file_manager.show('/')
        self.manager_open = True

    def select_path(self, path):
        self.exit_manager()
        toast(path)

    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True
    
    def process(self):
        '''
        PROCESS VIET O DAY
        '''
        pass

if __name__ == "__main__":
    MainApp().run()