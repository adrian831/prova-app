from kivymd.app import MDApp
from kivy.lang import Builder

KV = """
Screen:
    GridLayout:
        rows: 2
        
        MDLabel:
            id: mdlab
            text: "Welcome in perfect habits"
            halign: "center"
            font_style: "H3"
        
        MDRaisedButton:
            id: mdraised
            text: "Welcome people"
            font_size: "20"
            on_press: app.obbiettivi_button()

"""



class MainApp(MDApp):

    def build(self):
        self.title = "Hello Kivy"
        self.theme_cls.theme_style = "Dark" # Light
        self.theme_cls.primary_palette = "Amber"
        return Builder.load_string(KV)


    def obbiettivi_button(self):
        self.root.ids["mdlab"].text="Corri"

MainApp().run()
