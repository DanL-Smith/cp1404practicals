"""
Kivy example for CP1404/CP5632, IT@JCU
Dynamically create labels based on content of lists
Daniel Smith
20/09/2021
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

__author__ = 'Daniel Smith'

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 200


class DynamicLabelsApp(App):
    """Dynamic Labels is a kivy application that demos dynamic labels in kivy"""

    def __init__(self, *args):
        """Construct main app."""
        super().__init__(*args)
        self.names = ["John", "Bob", "Jimmy"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels from list entries and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
