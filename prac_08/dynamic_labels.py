"""CP1404 Practical 8 - Dynamic Labels"""

from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder


class DynamicLabelsApp(App):
    """Main program - Kivy app for dynamic label widget creation."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data for list of names
        self.names = ["John", "Paul", "George", "Ringo"]

    def build(self):
        """Build Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create dynamic labels from data and add them to GUI."""
        for name in self.names:
            label = Label(text=name)
            self.root.ids.entries_box.add_widget(label)


DynamicLabelsApp().run()
