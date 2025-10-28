<h1 align="center">
  🎧 yt2mp3    
</h2>

<p align="center">
 <a href="https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fl0n3m4n%2Fyt2mp3">
    <img src="https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fl0n3m4n%2Fyt2mp3&label=Visitors&countColor=%2337d67a" />
    </a>
    <a href="https://www.facebook.com/l0n3m4n">
        <img src="https://img.shields.io/badge/Facebook-%231877F2.svg?style=for-the-badge&logo=Facebook&logoColor=white" alt="Facebook">
    </a>
      <a href="https://www.twitter.com/l0n3m4n">
        <img src="https://img.shields.io/badge/Twitter-%23000000.svg?style=for-the-badge&logo=X&logoColor=white" alt="X">
    </a>
    <a href="https://medium.com/@l0n3m4n">
        <img src="https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white" alt="Medium">
    </a>
    <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python">
    </a>
</p>
<br>

## 📜 Description  
**yt2mp3** is a small project cli music downloader from youtube and convert into **mp3** using the powerful **yt-dlp** library.

"Converting YouTube videos on third party websites carries high risks, hackers can embed executable code or scripts within MP3 files. When you play or open such file, it could potentially execute malicious code and compromise your system."

 
📚 Table of Contents
- 📜 [Description](#-description)
- 🛠️ [Installation](#-installation)
- ⚙️ [Usage](#-usage)
- 💁 [References](#-references)
 

## 🛠️ Installation 
> Installing virtual environment
```bash
$ sudo apt install python3.11-venv
$ python3 -m pip install virtualenv 
$ python3 -m venv venv 
```

```bash
$ git clone https://github.com/l0n3m4n/yt2mp3.git
$ cd yt2mp3 && source venv/bin/activate
$ pip install -r requirements.txt
```

> **System Dependencies:**
> `yt-dlp` relies on `ffmpeg` for audio extraction and conversion. Please ensure it's installed on your system.
>
> **For Debian/Ubuntu-based systems:**
> ```bash
> sudo apt update
> sudo apt install ffmpeg
> ```
>
> **For Fedora/RHEL-based systems:**
> ```bash
> sudo dnf install ffmpeg
> ```
## ⚙️ Usage 
```shell
$ python3 yt2mp3.py -h, --help

        __   ______                  ______ 
.--.--.|  |_|__    |.--------.-----.|__    |
|  |  ||   _|    __||        |  _  ||__    |
|___  ||____|______||__|__|__|   __||______|
|_____|                      |__|           
                                                                         
        Author: l0n3m4n | ⚙️  v1.4.0

usage: yt2mp3.py [-h] [--url URL] [-o OUTPUT]

Download a YouTube video and convert to MP3.

options:
  -h  --help        Show this help message and exit
  -u  --url         YouTube video URL
  -o  --output      Output filename for MP3

Ex: python3 yt2mp3.py -u "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -o rick_astley.mp3
```

```shell
$ python3 yt2mp3.py -u "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -o /save/path/music_title.mp3
        __   ______                  ______ 
.--.--.|  |_|__    |.--------.-----.|__    |
|  |  ||   _|    __||        |  _  ||__    |
|___  ||____|______||__|__|__|   __||______|           
|_____|                      |__|           
                                                                         
        Author: l0n3m4n | ⚙️  v1.4.0
                                                                         
📥 Downloading and converting to MP3
[download]  35.1% of   73.32MiB at    2.84MiB/s ETA 00:16
🎧 Conversion complete. MP3 saved at: ./music/music_title.mp3
```
## 💁 References
- [**yt-dlp**](https://github.com/yt-dlp/yt-dlp) is a youtube-dl fork with additional features and fixes. It's used for downloading and converting videos.
- [**FFmpeg**](https://ffmpeg.org/) is a complete, cross-platform solution to record, convert and stream audio and video. `yt-dlp` uses it for post-processing.

## 📝 Todo
- [x] **Added progress bar (via yt-dlp's native output)**
- [ ] **Add multiple URL via command**
- [ ] **Add multiple URL in a one list e.q `music_list.txt`**
 

## 👨🏾‍⚖️ License
This project is under terms of the [MIT License](LICENSE). For fixing Bugs, create [issue](https://github.com/l0n3m4n/yt2mp3/issues/new)
