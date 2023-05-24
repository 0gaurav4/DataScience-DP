import os
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from time import sleep
import pytube
from pathlib import Path

save_addr = f"{os.environ['USERPROFILE']}\Downloads\Youtube DL"
print(save_addr)

layout = BoxLayout

def youtube_dl(video,addr):
        video = str(video.text)
        try:
            yt = pytube.YouTube(video)
            ys = yt.streams.get_by_resolution('360p')
            ys.download(output_path=addr)
        except pytube.exceptions.RegexMatchError:
            print('The Regex pattern did not return any matches for the video: {}'.format(video))          
        except pytube.exceptions.ExtractError:
            print('An extraction error occurred for the video: {}'.format(video))         
        except pytube.exceptions.VideoUnavailable:
            print('The following video is unavailable: {}'.format(video))

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


class MyGrid(layout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = 20
        self.padding = [10, 10]
        self.cols = 1
        self.label = Label(text="Enter link of Video You Want to Download! and wait 1 minute 📝↡")
        self.add_widget(self.label)
        self.link = TextInput(hint_text="Example: youtube.com/watch?v=MXDHK_MqRsk", multiline=False)
        self.add_widget(self.link)
        self.btn = Button(text="OK!")
        self.btn.bind(on_press=lambda x:self.callback())
        self.add_widget(self.btn)
        sleep(3)

    def callback(self):
        def dl(video,addr,DL=True):
            try:
                yt = pytube.YouTube(video)
                if DL:
                    ys = yt.streams.get_by_resolution('360p')
                    cd(addr)
                    ys.download(output_path=addr)
            except pytube.exceptions.RegexMatchError:
                print('The Regex pattern did not return any matches for the video: {}'.format(video))          
            except pytube.exceptions.ExtractError:
                print('An extraction error occurred for the video: {}'.format(video))         
            except pytube.exceptions.VideoUnavailable:
                print('The following video is unavailable: {}'.format(video))
            return yt
        video = str(self.link.text)
        title = str(dl(video,self.link,DL=False).title)
        self.label.text = f"Download : \"{title}\" , Save in:"
        self.link.text = f"{save_addr}"
        self.btn.text = "Download video!"
        self.btn.bind(on_press=lambda x:dl(video,self.link.text))

class MyKivy(App):
        def build(self):
            return MyGrid()

if __name__ == "__main__":
    MyKivy().run()