bot_token = "1895553984:AAGScuPHiJd7SF3mYG2QB8ZYMhE4GwLq8wY"
from rich import print
from rich.console import Console
from speedtest import Speedtest

class test():
    def network(f=None):
        console = Console()
        st = Speedtest()

        with console.status("[bold green]Замеряю скорость интернета...") as status:
            dl_speed = int(st.download() / 8000)
            up_speed = int(st.upload() / 8000)

        print(f"Скорость закачки: {dl_speed} kb/s \nСкорость выгрузки: {up_speed} kb/s")

    def networktts(f=True):
        from gtts import gTTS

        def textToAudio(str):
            audio = gTTS(str)
            audio.save('networktest.mp3')

        console = Console()
        st = Speedtest()

        with console.status("[bold green]Замеряю скорость интернета...") as status:
            dl_speed = int(st.download() / 8000)
            up_speed = int(st.upload() / 8000)
        textToAudio(f'network speed download {dl_speed} kilobite upload {up_speed} kilobite')
        #textToAudio(f'Скорость закачки: {dl_speed} kilobite Скорость выгрузки: {up_speed} kilobite')


