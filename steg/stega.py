from kivy.lang import Builder

from kivy.factory import Factory

from kivymd.app import MDApp



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

        left_action_items: [["dots-vertical", lambda x: None]]



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



            MDRoundFlatIconButton:

                text: "Upload data image"

                icon: "file-upload"

                width: dp(200)

                pos_hint: {"center_x": .5}



            MDRectangleFlatButton:

                text: "Process"

                pos_hint: {"center_x": .5}



"""

)





class MainApp(MDApp):

    def __init__(self, **kwargs):

        self.title = "STEGANOGRAPHY"

        self.theme_cls.primary_palette = "Green"

        super().__init__(**kwargs)



    def build(self):

        self.root = Factory.AppUI()



if __name__ == "__main__":

    MainApp().run()
