from kivy.app import App
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import StringProperty
from organization import organize_images_by_face

class MainApp(App):
    def build(self):
        return RootWidget()

class RootWidget(BoxLayout):
    status_text = StringProperty("Please select a directory and press 'Select'")

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)


    def select(self, *args):
        try:
            self.status_text = "Processing..."
            organize_images_by_face(self.ids.filechooser.selection[0])
            self.status_text = "Photos sorted successfully!"
        except Exception as e:
            self.status_text = "An error occurred!"
            popup = Popup(title='Error', content=Label(text=str(e)), size_hint=(None, None), size=(400, 400))
            popup.open()

class MyApp(App):
    def select(self, *args):
        print(self.filechooser.selection)  # prints the selected directory path

if __name__ == '__main__':
    MainApp().run()