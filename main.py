from kivy.app import App
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import os
import glob
import face_recognition

import numpy as np
import shutil
from organization import organize_images_by_face



class MainApp(App):
    def build(self):
        return RootWidget()

class RootWidget(BoxLayout):
    def build(self):
        self.filechooser = FileChooserIconView(dirselect=True)
        select_button = Button(text="Select", on_release=self.select)

        self.add_widget(self.filechooser)
        self.add_widget(select_button)

        return self
    


    def select(self, *args):
        print(self.ids.filechooser.selection)
        organize_images_by_face(self.ids.filechooser.selection[0])
        



class MyApp(App):
    

    def select(self, *args):
        print(self.filechooser.selection)  # prints the selected directory path


if __name__ == '__main__':
    MainApp().run()