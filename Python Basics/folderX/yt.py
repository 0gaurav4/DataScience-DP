from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from pytube import YouTube

class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text='📝 ↡↡'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.video = YouTube(self.username)



class yt(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    yt().run()