from pytube import YouTube
from pytube import Playlist
from pytube import Channel
import os
from flask import Flask, render_template, request
def playlist(url):
    playlist = Playlist(url)
    print('Number of videos in playlist: %s' % len(playlist.video_urls))
    for video in playlist.videos:
        video.streams.filter(progressive=True,
                                   file_extension='mp4').order_by(
            'resolution').desc().first().download()
    print("Done!!")

def video(url):
        video_caller = YouTube(url)
        print(video_caller.title)
        video_caller.streams.filter(progressive=True, file_extension='mp4').order_by(
            'resolution').desc().first().download()
        print("Done!!")

def channel(url):
            channel_videos = Channel(url)
            print(f'Downloading videos by: {channel_videos.channel_name}')
            for video in channel_videos.videos:
                video.streams.filter(progressive=True,
                                     file_extension='mp4').order_by(
                    'resolution').desc().first().download()
            print("Done!!")
def video_voice_only(url):
    video_caller = YouTube(url)
    print(video_caller.title)
    audio = video_caller.streams.filter(only_audio=True).first()
    out_path = audio.download(output_path=video_caller.title)
    new_name = os.path.splitext(out_path)
    os.rename(out_path,new_name[0] + ".mp3")
    print("Done!!")
def picture_only(url):
    video_caller = YouTube(url)
    print(video_caller.title)
    video = video_caller.streams.filter(only_video=True).first()
    out_path = video.download(output_path=video_caller.title)
    new_name = os.path.splitext(out_path)
    os.rename(out_path,new_name[0] + ".mp4")
    print("Done!!")
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        required = request.form['required']
        if required == "playlist":
            playlist(url)
        elif required == "video":
            video(url)
        elif required == "channel":
            channel(url)
        elif required == "voice":
            video_voice_only(url)
        elif required == "picture":
            picture_only(url)
        else:
            print("Invalid")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)