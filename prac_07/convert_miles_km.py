"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to kilometres
Daniel Smith
18/09/2021
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

__author__ = 'Daniel Smith'

MILES_IN_KM = 1.6093444
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 200


class MilesToKilometresApp(App):
    """Miles To Kilometres App is a kivy application that converts miles to kilometres"""
    def build(self):
        """Build the Kivy app from kv file."""
        Window.size = (WINDOW_WIDTH, WINDOW_HEIGHT)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Handle the calculation and output the result to label"""
        value = self.get_valid_miles()
        self.root.ids.output_label.text = f"{value * MILES_IN_KM:.3f}"

    def handle_increment(self, increment):
        """Handle the up or down button press, update the text input with new value and call the calculate function"""
        self.root.ids.input_miles.text = str(self.get_valid_miles() + increment)
        self.handle_calculate()

    def get_valid_miles(self):
        """Get text from text input and convert to a float or 0 if an error raises"""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesToKilometresApp().run()