from flask import Flask, request, render_template
from pytube import YouTube

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        yt = YouTube(url)
        stream = yt.streams.first()
        if request.form['type'] == 'video':
            stream = yt.streams.filter(file_extension='mp4').first()
        elif request.form['type'] == 'audio':
            stream = yt.streams.filter(only_audio=True).first()
        elif request.form['type'] == 'playlist':
            for video in yt.playlist:
                video.streams.first().download()
        else:
            return 'Invalid type specified'
        stream.download()
        return 'Download complete!'
    return render_template('index.html')

if __name__ == '__main__':
    app.run()