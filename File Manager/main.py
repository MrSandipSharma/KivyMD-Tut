import os
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager

Window.size = (300, 580)

KV = '''
MDBoxLayout:
    orientation: "vertical"
    spacing: 25

    MDTopAppBar:
        title: "MDFileManager"
        left_action_items: [["menu", lambda x: None]]
        elevation: 3

    MDBoxLayout:
        orientation: "vertical"
        padding: 15
        size_hint: 1, .5
        pos_hint: {"center_x": .5}
        AsyncImage:
            size_hint: .5, .3
            pos_hint: {"center_x": .5}
            id: img
            source: "logo.png"

        MDLabel:
            id: text
            font_style: "H6"
            halign: "center"
            text: ""
            size_hint: .8, .2

    MDFloatLayout:
        size_hint: .8, .2
        pos_hint: {"center_x": .5}
        MDRoundFlatIconButton:
            text: "Open manager"
            icon: "folder"
            pos_hint: {"center_y": 1, "center_x": .5}
            on_release: app.file_manager_open()
'''


class Example(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager, select_path=self.select_path
        )

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def file_manager_open(self):
        self.file_manager.show(os.path.expanduser("~")) 
        self.manager_open = True

    def select_path(self, path: str):
        self.root.ids.img.source = path
        self.root.ids.text.text = path
        self.exit_manager()

    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True


Example().run()