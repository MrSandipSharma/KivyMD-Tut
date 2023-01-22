from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivymd.uix.toolbar import MDTopAppBar
from kivy.core.window import Window

Window.size = (300,580)

kv = """
#:import SliverToolbar __main__.SliverToolbar

<CardItem>
    size_hint_y: None
    height: "86dp"
    elevation: 3
    padding: "4dp"
    radius: 12

    FitImage:
        source: "logo.png"
        radius: root.radius
        size_hint_x: None
        width: root.height

    MDBoxLayout:
        orientation: "vertical"
        adaptive_height: True
        spacing: "6dp"
        padding: "12dp", 0, 0, 0
        pos_hint: {"center_y": .5}

        MDLabel:
            text: "Astro Coder"
            font_style: "H5"
            bold: True
            adaptive_height: True

        MDLabel:
            text: "Like Share Subscribe"
            theme_text_color: "Hint"
            adaptive_height: True

MDScreen:
    MDSliverAppbar:
        background_color: "2d4a50"
        radius: 26
        toolbar_cls: SliverToolbar()

        MDSliverAppbarHeader:
            MDRelativeLayout:
                FitImage:
                    source: "logo.png"

        MDSliverAppbarContent:
            id: content
            orientation: "vertical"
            padding: "12dp"
            spacing: "12dp"
            adaptive_height: True

"""

class CardItem(MDCard):
    pass

class SliverToolbar(MDTopAppBar):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shadow_color = (0, 0, 0, 0)
        self.type_height = "small"
        self.title = "Astro Coder"
        self.left_action_items = [["arrow-left", lambda x: x]]
        self.right_action_items = [
            ["attachment", lambda x: x],
            ["dots-vertical", lambda x: x],
        ]

class AstroSilverApp(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        return Builder.load_string(kv)

    def on_start(self):
        for x in range(10):
            self.root.ids.content.add_widget(CardItem())

AstroSilverApp().run()