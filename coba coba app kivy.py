import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class DataCalculator(App):
    def build(self):
        self.input1 = TextInput()
        self.input2 = TextInput()
        self.label = Label(text="Hasil penjumlahan ditampilkan di sini.")
        self.button = Button(text="Hitung")
        self.button.bind(on_press=self.calculate)
        
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.input1)
        layout.add_widget(self.input2)
        layout.add_widget(self.label)
        layout.add_widget(self.button)
        
        return layout
    
    def calculate(self, instance):
        try:
            num1 = float(self.input1.text)
            num2 = float(self.input2.text)
            result = num1 + num2
            self.label.text = f"Hasil penjumlahan: {result}"
        except ValueError:
            self.label.text = "Mohon masukkan angka yang valid!!!."

if __name__ == '__main__':
    DataCalculator().run()
