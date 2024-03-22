from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.properties import NumericProperty


class TimerApp(App):
    time_seconds = NumericProperty(0)

    def build(self):
        self.label = Label(text='00:00', font_size=80)
        start_button = Button(text='Start')
        start_button.bind(on_release=self.start_timer)

        stop_button = Button(text='Stop')
        stop_button.bind(on_release=self.stop_timer)

        reset_button = Button(text='Reset')
        reset_button.bind(on_release=self.reset_timer)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.label)
        layout.add_widget(start_button)
        layout.add_widget(stop_button)
        layout.add_widget(reset_button)

        return layout

    def start_timer(self, instance):
        Clock.schedule_interval(self.update_time, 1)

    def stop_timer(self, instance):
        Clock.unschedule(self.update_time)

    def reset_timer(self, instance):
        self.time_seconds = 0
        self.label.text = '00:00'
        Clock.unschedule(self.update_time)

    def update_time(self, dt):
        self.time_seconds += 1
        minutes = self.time_seconds // 60
        seconds = self.time_seconds % 60
        self.label.text = '{:02d}:{:02d}'.format(minutes, seconds)


if __name__ == '__main__':
    TimerApp().run()
