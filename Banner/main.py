from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.toast import toast

kv = """

MDScreen: 

    MDBanner:
        id: banner
        over_widget: screen
        vertical_pad: toolbar.height
        text: ['665686968']

    MDTopAppBar:
        id: toolbar
        title: "Astro MDBanner"
        elevation: 4
        pos_hint: {'top': 1}

    MDGridLayout:
        id: screen
        cols: 1
        size_hint_y: None
        padding: 10
        spacing: 10
        height: Window.height - toolbar.height

        OneLineListItem:
            text: "One line Banner without actions"
            on_release: 
                banner.type= "one-line"
                banner.text = ["One line string text example without actions."]
                banner.left_action= []
                banner.right_action= []
                banner.show()

        OneLineListItem:
            text: "One line Banner With actions"
            on_release: 
                banner.type= "one-line"
                banner.text= ["One line string text example with actions."]
                banner.left_action= ["CANCEL", lambda x: banner.hide()]
                banner.right_action= ["CLOSE", lambda x: banner.hide()]
                banner.show()

        OneLineListItem:
            text: "Two line Banner With actions"
            on_release: 
                banner.type= "two-line"
                banner.text= ["One line string text example with actions.", "This is the second line of the banner message."]
                banner.left_action= ["CANCEL", lambda x: banner.hide()]
                banner.right_action= ["CLOSE", lambda x: banner.hide()]
                banner.show()

        OneLineListItem:
            text: "Three line Banner With actions"
            on_release: 
                banner.type= "three-line"
                banner.text= ["One line string text example with actions.",\
                     "This is the second line of the banner message." ,\
                    "and this is the third line of the banner message."]
                banner.left_action= ["CANCEL", lambda x: banner.hide()]
                banner.right_action= ["CLOSE", lambda x: banner.hide()]
                banner.show()

        OneLineListItem:
            text: "Banner With actions and Icon"
            on_release: 
                banner.type= "two-line-icon"
                banner.text= ["Astro Coder","Like Share and Subscribe."]
                banner.left_action= ["CANCEL", lambda x: banner.hide()]
                banner.icon = "icon.png"
                banner.right_action= ['[color=ff0000]SUBSCRIBE[/color]', lambda x: app.Subscribe()]
                banner.show()

        Widget:
"""

class KivyBanner(MDApp):
    def build(self):
        return Builder.load_string(kv)

    def Subscribe(self):
        self.root.ids.banner.hide()
        toast("Astro Coder Channel Subscribed..")

KivyBanner().run()