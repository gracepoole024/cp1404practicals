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
        self.message = "Convert miles to km"
        return self.root

    def receive_miles(self):
        miles_value = float(self.root.ids.input_miles.text)
        return miles_value

    def handle_calculations(self):
        """Handle changes to the text input by updating the model from the view."""
        self.message = self.root.ids.user_input.text
        miles_value = self.receive_miles()
        kilometers_result = miles_value * MILES_TO_KILOMETERS
        self.root.ids.output_label.text = str(kilometers_result)


# create and start the App running
MilesKilometersApp().run()
