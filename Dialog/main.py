from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.list import OneLineAvatarListItem, OneLineAvatarIconListItem
from kivy.properties import StringProperty
from kivy.core.window import Window

Window.size = (300,580)

kv = """
<Content>:
    orientation: "vertical"
    radius: 15
    spacing: 12
    size_hint_y: None
    height: "120dp"

    MDTextField:
        id: Name
        hint_text: "Write Your First Name here!"
        line_anim: True
        text_color_normal: 1,1,1,1
        text_color_focus: 1,1,1,1
        line_color_normal: 1,1,1,1
        hint_text_color_normal: 1,1,1,1
        hint_text_color_focus: 1,1,1,1
        line_color_focus: 1,1,1,1

    MDTextField:
        id: lastN
        hint_text: "Write Your Last Name here!"
        line_anim: True
        text_color_normal: 1,1,1,1
        text_color_focus: 1,1,1,1
        line_color_normal: 1,1,1,1
        hint_text_color_normal: 1,1,1,1
        hint_text_color_focus: 1,1,1,1
        line_color_focus: 1,1,1,1

<ItemConfirm>
    on_release: root.set_icon(check)

    CheckboxLeftWidget:
        id: check
        group: "check"

<Item>

    ImageLeftWidget:
        source: root.source

MDScreen:
    MDBoxLayout:
        orientation: "vertical"
        spacing: 55
        MDTopAppBar:
            title: "Astro Dialog"

        MDBoxLayout:
            orientation: "vertical"
            size_hint: 1, .6
            spacing: 15
            MDLabel: 
                id: text
                text: "Result"
                halign: "center"
                font_style: "H6"
            MDRaisedButton:
                text: "Simple"
                pos_hint: {"center_x": .5}
                size_hint: .8, .1
                font_style: "H6"
                on_press: app.simple_Dialog()
            MDRaisedButton:
                text: "Confirmation"
                size_hint: .8, .1
                font_style: "H6"
                pos_hint: {"center_x": .5}
                on_press: app.confirmation_Dialog()
            MDRaisedButton:
                text: "Custom"
                size_hint: .8, .1
                font_style: "H6"
                pos_hint: {"center_x": .5}
                on_press: app.custom_Dialog()
        
        MDBoxLayout:
            size_hint: .8, .4


"""

class Content(MDBoxLayout):
    pass

class ItemConfirm(OneLineAvatarIconListItem):
    divider = None

    def set_icon(self, instance_check):
        instance_check.active = True
        check_list = instance_check.get_widgets(instance_check.group)
        for check in check_list:
            if check != instance_check:
                check.active = False

class Item(OneLineAvatarListItem):
    divider = None
    source = StringProperty()

class AstroDialog(MDApp):
    dialog = None
    dialog2 = None
    dialog3 = None
    def build(self):
        return Builder.load_string(kv)
    
    def simple_Dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                    text="[color=000000ff]Simple Dialog",
                    type="simple",
                    items=[
                        Item(text="KivyMD", source="data/logo/kivy-icon-128.png",
                        ),
                        Item(text="Astro Coder", source="icon.png",
                        ),
                    ],
                    buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_press = self.cancelD
                    ),
                    MDFlatButton(
                        text="DISCARD",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_press = self.Printf
                    ),
                ],
            )

        self.dialog.open()

    def confirmation_Dialog(self):
        if not self.dialog2:
            self.dialog2 = MDDialog(
                title="Phone ringtone",
                type="confirmation",
                items=[
                    ItemConfirm(text="Callisto"),
                    ItemConfirm(text="Luna"),
                    ItemConfirm(text="Night"),
                    ItemConfirm(text="Solo"),
                    ItemConfirm(text="Phobos"),
                    ItemConfirm(text="Diamond"),
                    ItemConfirm(text="Sirena"),
                    ItemConfirm(text="Red music"),
                    ItemConfirm(text="Allergio"),
                    ItemConfirm(text="Magic"),
                    ItemConfirm(text="Tic-tac"),
                ],
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_press= self.cancelD2
                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_press = self.Printf
                    ),
                ],
            )
        self.dialog2.open()

    def custom_Dialog(self):
        if not self.dialog3:
            self.dialog3 = MDDialog(
                    title = '[color=ffffff]Custom Dialog[/color]',
                    type= "custom",
                    radius=[20, 7, 20, 7],
                    md_bg_color = self.theme_cls.primary_color,
                    content_cls=Content(),
                    buttons=[
                    MDRaisedButton(
                        text="CANCEL",
                        md_bg_color= (1,0,0,1),
                        on_press= self.cancelD3,
                    ),
                    MDRaisedButton(
                        text="PRINT",
                        md_bg_color = (69/255,55/255,86/255,1),
                        on_press = self.Printf
                    ),
                ],

            )
        self.dialog3.open()

    def cancelD(self, *args):
        self.dialog.dismiss()

    def cancelD2(self, *args):
        self.dialog2.dismiss()

    def cancelD3(self, *args):
        self.dialog3.dismiss()
    
    def Printf(self, *args):
        First = self.dialog3.content_cls.ids.Name.text
        Last = self.dialog3.content_cls.ids.lastN.text
        self.root.ids.text.text = f"{First} {Last}"
        self.dialog3.dismiss()

AstroDialog().run()