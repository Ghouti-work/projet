from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

class FirstPage(BoxLayout):
    def __init__(self, **kwargs):
        super(FirstPage, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(Label(text="MediTalk", font_size=40, halign="center"))
        welcome_button = Button(text="Welcome", size_hint=(0.5, 0.2), pos_hint={"center_x": 0.5, "center_y": 0.5})
        welcome_button.bind(on_press=self.go_to_home)
        self.add_widget(welcome_button)

    def go_to_home(self, instance):
        self.parent.current = "Home"

class HomePage(BoxLayout):
    def __init__(self, **kwargs):
        super(HomePage, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(Label(text="MediTalk", font_size=20, halign="center"))
        maladie_button = Button(text="Maladie", size_hint=(0.3, 0.1), pos_hint={"center_x": 0.3, "center_y": 0.3})
        maladie_button.bind(on_press=self.go_to_maladie)
        self.add_widget(maladie_button)
        lang_bluetooth_button = Button(text="Langage & Bluetooth", size_hint=(0.3, 0.1), pos_hint={"center_x": 0.3, "center_y": 0.1})
        lang_bluetooth_button.bind(on_press=self.go_to_lang_bluetooth)
        self.add_widget(lang_bluetooth_button)
        guide_button = Button(text="Guide", size_hint=(0.3, 0.1), pos_hint={"center_x": 0.3, "center_y": 0.1})
        guide_button.bind(on_press=self.go_to_guide)
        self.add_widget(guide_button)
        important_button = Button(text="Important", size_hint=(0.3, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.1})
        important_button.bind(on_press=self.go_to_important)
        self.add_widget(important_button)

    def go_to_maladie(self, instance):
        self.parent.current = "Maladie"

    def go_to_lang_bluetooth(self, instance):
        self.parent.current = "Lang_Bluetooth"

    def go_to_guide(self, instance):
        self.parent.current = "Guide"

    def go_to_important(self, instance):
        self.parent.current = "Important"

class MaladiePage(BoxLayout):
    def __init__(self, **kwargs):
        super(MaladiePage, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(Label(text="You need to turn bluetooth on", size_hint=(1, 0.2)))
        dropdown = DropDown()
        for choice in ["choice1", "choice2", "choice3", "choice4"]:
            btn = Button(text=choice, size_hint_y=None, height=40)
            btn.bind(on_release=lambda btnn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
        dropdown_button = Button(text="Select", size=(0.3, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.3})
        dropdown_button.bind(on_release=dropdown.open)
        self.add_widget(dropdown_button)
        back_button = Button(text="Back", size_hint=(0.2, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.3})
        back_button.bind(on_press=self.go_to_home)
        self.add_widget(back_button)

    def go_to_home(self, instance):
        self.parent.current = "Home"

class LangBluetoothPage(BoxLayout):
    def __init__(self, **kwargs):
        super(LangBluetoothPage, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.output_label = Label(text="The message will be displayed here", size_hint=(1, 0.8))
        self.add_widget(self.output_label)
        back_button = Button(text="Back", size_hint=(0.5, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.1})
        back_button.bind(on_press=self.go_to_home)
        self.add_widget(back_button)

    def go_to_home(self, instance):
        self.parent.current = "Home"

    def set_output_message(self, message):
        self.output_label.text = message

class GuidePage(BoxLayout):
    def __init__(self, **kwargs):
        super(GuidePage, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(Label(text="Title1", font_size=20))
        self.add_widget(Label(text="text for title1"))
        self.add_widget(Label(text="Title2", font_size=20))
        self.add_widget(Label(text="text for title 2"))
        back_button = Button(text="Back", size_hint=(0.5, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.1})
        back_button.bind(on_press=self.go_to_home)
        self.add_widget(back_button)

    def go_to_home(self, instance):
        self.parent.current = "Home"

class ImportantPage(BoxLayout):
    def __init__(self, **kwargs):
        super(ImportantPage, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(Label(text="Important information goes here", size_hint=(1, 0.8)))
        back_button = Button(text="Back", size_hint=(0.5, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.1})
        back_button.bind(on_press=self.go_to_home)
        self.add_widget(back_button)

    def go_to_home(self, instance):
        self.parent.current = "Home"

class MediTalkApp(App):
    def build(self):
        self.icon="doctor.png"
        screen_manager = ScreenManager()
        screen_manager.add_widget(Screen(name="First"))
        screen_manager.add_widget(Screen(name="Home"))
        screen_manager.add_widget(Screen(name="Maladie"))
        screen_manager.add_widget(Screen(name="Lang_Bluetooth"))
        screen_manager.add_widget(Screen(name="Guide"))
        screen_manager.add_widget(Screen(name="Important"))
        return screen_manager

if __name__ == "__main__":
    MediTalkApp().run()
