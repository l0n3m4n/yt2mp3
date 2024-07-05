<div align="right">
  <a href="https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fl0n3m4n%2Fyt2mp3">
    <img src="https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fl0n3m4n%2Fyt2mp3&label=Visitors&countColor=%2337d67a" />
  </a>
</div>

# 🎧 yt2mp3     
📚 Table of Contents
- 📜 [Description](#-description)
- 🛠️ [Installation](#-installation)
- ⚙️ [Usage](#-usage)
- 💁 [References](#-references)
- 📌 [Author](#-author)
- 👨🏾‍⚖️ [License](#-license)

## Description  
**yt2mp3** is a small project cli music downloader from youtube and convert into **mp3** using **pytube, moviepy and tqdm** python libraries.

"Converting YouTube videos on third party websites carries high risks, hackers can embed executable code or scripts within MP3 files. When you play or open such file, it could potentially execute malicious code and compromise your system."

## 🛠️ Installation 
> Installing virtual environment
```bash
$ sudo apt install python3.11-venv
$ python3 -m pip install virtualenv 
$ python3 -m venv venv 
```

```bash
$ git clone https://github.com/l0n3m4n/yt2mp3.git
$ cd yt3mp3 && source venv/bin/activate
$ pip install -r requirements.txt
```
## ⚙️ Usage 
```shell
$ python3 yt2mp3.py -h, --help

        __   ______                  ______ 
.--.--.|  |_|__    |.--------.-----.|__    |
|  |  ||   _|    __||        |  _  ||__    |
|___  ||____|______||__|__|__|   __||______|
|_____|                      |__|           
                                                                         
        Author: l0n3m4n | ⚙️  v1.1 

usage: yt2mp3.py [-h] [--url URL] [-o OUTPUT]

Download a YouTube video and convert to MP3.

options:
  -h  --help        Show this help message and exit
  -u  --url         YouTube video URL
  -o  --output      Output filename for MP3

Ex: python3 yt2mp3.py -u https://www.youtube.com/watch?v=id -o music_title.mp3
```

```shell
$ python3 yt2mp3.py --url https://www.youtube.com/watch?v=byCgohS7feE --output music_title.mp3
        __   ______                  ______ 
.--.--.|  |_|__    |.--------.-----.|__    |
|  |  ||   _|    __||        |  _  ||__    |
|___  ||____|______||__|__|__|   __||______|
|_____|                      |__|           
                                                                         
        Author: l0n3m4n | ⚙️  v1.1 

📥 Downloading video...
Progress: 100%|############################| 3.67M/3.67M [00:00<00:00, 9.25MB/s]
💾 Video downloaded.
🎵 Converting to MP3...
Progress: 0%|##########################################| 0/179.05 [00:07<?, ?s/s]
💽 Conversion complete. MP3 saved at: ./music/music_title.mp3                                                                               
🚮 Temporary video file deleted.
```
## 💁 References
- [**pytube**](https://pypi.org/project/pytube/) is a genuine, lightweight, dependency-free Python library (and command-line utility) for downloading YouTube videos.
- [**Moviepy**](https://pypi.org/project/moviepy/) allows to extract audio from a video file (like MP4) and save it as an audio file (like MP3).
- [**tqdm**](https://pypi.org/project/tqdm/) Instantly make your loops show a smart progress meter - just wrap any iterable with tqdm(iterable), and you’re done!

## 📝 Todo
- [x] **~~Adding progress bar~~**
- [ ] **Add multiple URL**
- [ ] **Extract MP3 metadata for investigative purposes**
- [ ] **Adding song title automatically**
- [ ] **GUI integration, flask, tkinker**
- [ ] **UI design, additional features**



## 📌 Author
- [Facebook](https://facebook.com/l0n3m4n)
- [Twitter (X)](https://twitter.com/l0n3m4n)
- [Medium](https://medium.com/l0n3m4n)
- [Website](https://l0n3m4n.github.io)

## 👨🏾‍⚖️ License
This project is under terms of the [MIT License](LICENSE). For fixing Bugs, create [issue](https://github.com/l0n3m4n/yt2mp3/issues/new)
