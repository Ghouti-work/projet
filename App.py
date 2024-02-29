from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image



# Define the KV language string with improved formatting and error correction
screen_helper = """
ScreenManager:
    FirstPage:
    HomePage:
    MaladiePage:
    LangBluetoothPage:
    GuidePage:
    ImportantPage:

<FirstPage>:

    name: 'FirstPage'

    AsyncImage:
        source: "MediTalk3.png"
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        size_hint : (0.6, 0.4)

    

    MDRectangleFlatButton:
        text: 'Welcome'
        text_color: 'white'
        
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        on_press: root.manager.current = 'HomePage'
        theme_text_color: 'Custom'
        md_bg_color: 54/255, 79/255, 107/255, 5
        line_color: 0,0,0,0
        
        



<HomePage>:
    name: 'HomePage'
    AsyncImage:
        source: "MediTalk4.png"
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}
        size_hint : (0.6, 0.4)

    MDRectangleFlatButton:
        text: 'Maladie'
        text_color: 'white'
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        on_press: root.manager.current = 'MaladiePage'
        theme_text_color: 'Custom'
        md_bg_color: 54/255, 79/255, 107/255, 5
        line_color: 0,0,0,0

    MDRectangleFlatButton:
        text: 'Connection & Bluetooth'
        text_color: 'white'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_press: root.manager.current = 'LangBluetoothPage'
        theme_text_color: 'Custom'
        md_bg_color: 54/255, 79/255, 107/255, 5
        line_color: 0,0,0,0

    MDRectangleFlatButton:
        text: 'Guide'
        text_color: 'white'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        on_press: root.manager.current = 'GuidePage'
        theme_text_color: 'Custom'
        md_bg_color: 54/255, 79/255, 107/255, 5
        line_color: 0,0,0,0

    MDRectangleFlatButton:
        text: 'Important'
        text_color: 'white'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_press: root.manager.current = 'Important'     
        theme_text_color: 'Custom'
        md_bg_color: 54/255, 79/255, 107/255, 5     
        line_color: 0,0,0,0   


<MaladiePage>:
    name: 'MaladiePage'
    MDRectangleFlatButton:
        text: 'Back'
        text_color: 'white'
        pos_hint: {'center_x': 0.2, 'center_y': 0.2}
        on_press: root.manager.current = 'HomePage'  
        theme_text_color: 'Custom'
        md_bg_color: 54/255, 79/255, 107/255, 5    
        line_color: 0,0,0,0


<LangBluetoothPage>:
    name: 'LangBluetoothPage'
    MDRectangleFlatButton:
        text: 'Back'
        text_color: 'white'
        pos_hint: {'center_x': 0.2, 'center_y': 0.2}
        on_press: root.manager.current = 'HomePage'    
        theme_text_color: 'Custom'
        md_bg_color: 54/255, 79/255, 107/255, 5    
        line_color: 0,0,0,0


<GuidePage>:
    name: 'GuidePage'
    MDRectangleFlatButton:
        text: 'Back'
        text_color: 'white'
        pos_hint: {'center_x': 0.2, 'center_y': 0.2}
        on_press: root.manager.current = 'HomePage'  
        theme_text_color: 'Custom'
        md_bg_color: 54/255, 79/255, 107/255, 5    
        line_color: 0,0,0,0


<ImportantPage>:
    name: 'Important'
    MDRectangleFlatButton:
        text: 'Back'
        text_color: 'white'
        pos_hint: {'center_x': 0.2, 'center_y': 0.2}
        on_press: root.manager.current = 'HomePage'    
        theme_text_color: 'Custom'
        md_bg_color: 54/255, 79/255, 107/255, 5  
        line_color: 0,0,0,0  


"""


# Class definitions remain the same
class FirstPage(Screen):
    pass


class HomePage(Screen):
    pass


class MaladiePage(Screen):
    pass


class LangBluetoothPage(Screen):
    pass


class GuidePage(Screen):
    pass


class ImportantPage(Screen):
    pass


sm = ScreenManager()
sm.add_widget(FirstPage(name='FirstPage'))
sm.add_widget(FirstPage(name='HomePage'))
sm.add_widget(FirstPage(name='MaladiePage'))
sm.add_widget(FirstPage(name='LangBluetoothPage'))
sm.add_widget(FirstPage(name='GuidePage'))
sm.add_widget(FirstPage(name='ImportantPage'))


class MediTalk(MDApp):
    def build(self):
        self.icon = "doctor.png"
        # search how to compile to an python app to apk file
        screen = Builder.load_string(screen_helper)
        return screen


if __name__ == '__main__':
    MediTalk().run()
