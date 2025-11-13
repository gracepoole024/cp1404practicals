"""
Kivy example for CP1404/CP5632, IT@JCU
This shows the use of a StringProperty object to store the "model" of MVC
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KILOMETERS = 1.60934


class MilesKilometersApp(App):
    """The class variable in the app is the 'model'."""
    message = StringProperty()

    def build(self):
        """Construct the app."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = "Convert miles to kilometers"
        return self.root

    def receive_miles(self):
        """Receive miles from user and return float."""
        text = self.root.ids.input_miles.text
        try:
            return float(text)
        except ValueError:
            return 0.0

    def handle_calculations(self):
        """Handle changes to the text input by updating the model from the view."""
        miles_value = self.receive_miles()
        kilometers_result = miles_value * MILES_TO_KILOMETERS
        self.root.ids.output_label.text = str(kilometers_result)

    def handle_increment(self, change):
        """Add positive or negative increment to received miles."""
        miles_value = self.receive_miles() + change
        self.root.ids.input_miles.text = str(miles_value)
        self.handle_calculations()


# create and start the App running
MilesKilometersApp().run()
