from pytube import YouTube
import os

def mp3_download(yt):
    destination = '.'

    video = yt.streams.filter(only_audio=True).first()

    # download the file
    out_file = video.download(output_path=destination)
  
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

if __name__ == '__main__':
    link = input('insira o link do video: ')
    yt = YouTube(link)

    mp3_download(yt)
