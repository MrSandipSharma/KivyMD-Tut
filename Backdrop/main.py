from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.toast import toast

kv = """
MDScreen:
    MDBoxLayout:
        orientation: "vertical"
        MDBackdrop:
            id: backdrop
            title: "Astro MDBackdrop"
            radius_left: "25dp"
            radius_right: "25dp"
            back_layer_color: 0,0,1,.7
            header_text: "Subscribe Youtube Channel"

            MDBackdropBackLayer:
                MDBoxLayout:
                    orientation: "vertical"
                    size_hint: 1, .4
                    pos_hint: {"top": .95}
                    padding: 15
                    MDTextField:
                        id: name
                        hint_text: "First Name"
                        size_hint: .8, .4
                        line_color_normal: 1,1,1,1
                        line_color_focus: 1,1,1,1
                        hint_text_color_normal: 1,1,1,1
                        hint_text_color_focus: 1,1,1,1
                        text_color_normal: 1,1,1,1
                        text_color_focus: 1,1,1,1
                        font_size: 27
                        pos_hint: {"center_x": .5}
                    MDTextField:
                        id: lname
                        hint_text: "Last Name"
                        size_hint: .8, .4
                        font_size: 27
                        line_color_normal: 1,1,1,1
                        line_color_focus: 1,1,1,1
                        hint_text_color_normal: 1,1,1,1
                        hint_text_color_focus: 1,1,1,1
                        text_color_normal: 1,1,1,1
                        text_color_focus: 1,1,1,1
                        pos_hint: {"center_x": .5}
                    MDRaisedButton:
                        text: "SUBSCRIBE"
                        md_bg_color: 1,0,0,1
                        pos_hint: {"center_x": .7}
                        on_press: app.sub(name.text, lname.text)

            MDBackdropFrontLayer:
                MDCard:
                    pos_hint: {"center_x": .5, "top": 1}
                    size_hint: .5, .3
                    md_bg_color: 1,1,0,1
                    spacing: 15
                    FitImage:
                        size_hint: 1, 1
                        source: "logo.png"

                    MDBoxLayout:
                        orientation: "vertical"
                        padding: 15
                        spacing: 10
                        MDLabel:
                            text: "Astro Coder"
                            font_style: "H6"

                        MDLabel:
                            text: "Python Kivy KivyMD"
                            font_style: "Subtitle1"

                        MDRaisedButton:
                            text: "SUBSCRIBE"
                            elevation: 0
                            md_bg_color: 1,0,0,1
                            on_press: app.subscribe()



"""

class AstroBackdrop(MDApp):
    def build(self):
        return Builder.load_string(kv)

    def subscribe(self):
        self.root.ids.backdrop.open()

    def sub(self, n, ln):
        self.root.ids.backdrop.close()
        toast(f"{n} {ln} Subscribed")

AstroBackdrop().run()