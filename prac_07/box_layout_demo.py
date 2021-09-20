"""
CP1404 Practical
Kivy GUI demo program to practice box layouts
Daniel Smith
20/09/2021
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Daniel Smith'

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 200


class BoxLayoutDemo(App):
    """Box Layout is a kivy application that demos the box layout"""
    def build(self):
        """Build the Kivy app from kv file."""
        Window.size = (WINDOW_WIDTH, WINDOW_HEIGHT)
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle to the greet button press by outputting a welcome message to output label"""
        print("Test")
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def handle_clear(self):
        """Handle the clear button press, restore the input and output to default values"""
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = 'Enter your name'


BoxLayoutDemo().run()
