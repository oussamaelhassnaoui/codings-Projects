import os
import sys
from pytube import YouTube
from pytube import Playlist

# Function to download video
def download_video(url):
    try:
        yt = YouTube(url)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
        print("Video downloaded successfully!")
    except Exception as e:
        print("Error in downloading video: ", e)

# Function to download audio
def download_audio(url):
    try:
        yt = YouTube(url)
        yt.streams.filter(only_audio=True).first().download()
        print("Audio downloaded successfully!")
    except Exception as e:
        print("Error in downloading audio: ", e)

# Function to download playlist
def download_playlist(url):
    try:
        pl = Playlist(url)
        pl.download_all()
        print("Playlist downloaded successfully!")
    except Exception as e:
        print("Error in downloading playlist: ", e)

# HTML code for the webpage
html = """
<html>
<body>
    <form>
    Enter the URL of the video or playlist: <br>
    <input type="text" id="url" name="url"><br>
    <br>
    Select the type of download: <br>
    <input type="radio" id="video" name="download_type" value="video" checked> Video <br>
    <input type="radio" id="audio" name="download_type" value="audio"> Audio <br>
    <input type="radio" id="playlist" name="download_type" value="playlist"> Playlist <br>
    <br>
    <input type="button" value="Download" onclick="download()">
    </form>
    <script>
    function download() {
        var url = document.getElementById("url").value;
        var download_type = document.querySelector('input[name="download_type"]:checked').value;
        if (download_type == "video") {
            window.location = "http://localhost:8080/download_video?url=" + url;
        } else if (download_type == "audio") {
            window.location = "http://localhost:8080/download_audio?url=" + url;
        } else if (download_type == "playlist") {
            window.location = "http://localhost:8080/download_playlist?url=" + url;
        }
    }
    </script>
</body>
</html>
"""

# Starting the web server
from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/download_video"):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            url = self.path.split("=")[1]
           
