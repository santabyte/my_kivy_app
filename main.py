from kivy.app import App
from kivy.uix.button import Button

class SimpleApp(App):
    def build(self):
        return Button(text='ساخته شده با GitHub!', font_size=50)

if __name__ == '__main__':
    SimpleApp().run()
