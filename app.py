from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup


class HarvestAI(App):

    def show_message(self, feature):
        content = Label(
            text=f"{feature}\n\nThis feature will be added soon!",
            halign="center"
        )

        popup = Popup(
            title="HarvestAI",
            content=content,
            size_hint=(0.8, 0.4)
        )

        popup.open()

    def build(self):

        main = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=12
        )

        title = Label(
            text="HarvestAI",
            font_size=30,
            bold=True,
            size_hint_y=None,
            height=60
        )

        subtitle = Label(
            text="Smart Farming Assistant",
            font_size=18,
            size_hint_y=None,
            height=40
        )

        main.add_widget(title)
        main.add_widget(subtitle)

        features = [
            "Leaf Doctor",
            "Crop Disease Detection",
            "Weather Forecast",
            "Crop Recommendation",
            "Pest Identification",
            "Farming Tips",
            "Expense & Profit Tracker"
        ]

        for feature in features:

            button = Button(
                text=feature,
                font_size=17,
                size_hint_y=None,
                height=55
            )

            button.bind(
                on_press=lambda instance, f=feature:
                self.show_message(f)
            )

            main.add_widget(button)

        return main


if __name__ == "__main__":
    HarvestAI().run()
