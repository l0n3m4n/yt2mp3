<p align="right"><img src="https://visitor-badge.laobi.icu/badge?page_id=l0n3m4n" alt="badge"/></p>

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
> Music is my life
## 🛠️ Installation 
>If virtual environment is not installed yet, follow to instruction below.
```bash
# installing python3 virtual environment
$ sudo apt install python3.11-venv
$ python3 -m pip install virtualenv 
$ python3 -m venv venv 
```

```bash
# cloning repository
$ git clone https://github.com/l0n3m4n/yt2mp3.git
$ cd yt3mp3 && source venv/bin/activate
$ pip install -r requirements.txt
```
## ⚙️ Usage 
```shell
$ python3 yt2mp3.py -h, --help

              ,--.   ,---.                  ,----.  
    ,--. ,--.,-'  '-.'.-.  \,--,--,--.,---. '.-.  | 
    \  '  / '-.  .-' .-' .'|        || .-. |  .' <  
     \   '    |  |  /   '-.|  |  |  || '-' '/'-'  | 
    .-'  /     `--'  '-----'`--`--`--'|  |-' `----'  
    `---'                             `--'   
         💻 ALDrin / ⚔️ l0n3m4n / ⚙️ v1.0.1  

usage: yt2mp3.py [-h] [--url URL] [-o OUTPUT]

Download a YouTube video and convert to MP3.

options:
  -h, --help            show this help message and exit
  --url URL             YouTube video URL
  -o OUTPUT, --output OUTPUT
                        Output filename for MP3

Example usage: python3 yt2mp3.py --url https://www.youtube.com/watch?v=byCgohS7feE --output test.mp3
```

```shell
$ python3 yt2mp3.py --url https://www.youtube.com/watch?v=byCgohS7feE --output music_title.mp3
              ,--.   ,---.                  ,----.  
    ,--. ,--.,-'  '-.'.-.  \,--,--,--.,---. '.-.  | 
    \  '  / '-.  .-' .-' .'|        || .-. |  .' <  
     \   '    |  |  /   '-.|  |  |  || '-' '/'-'  | 
    .-'  /     `--'  '-----'`--`--`--'|  |-' `----'  
    `---'                             `--'   
         💻 ALDrin / ⚔️ l0n3m4n / ⚙️ v1.0.1  

📥 Downloading video...
Downloading: 100%|############################| 3.67M/3.67M [00:00<00:00, 9.25MB/s]
💾 Video downloaded.
🎵 Converting to MP3...
Converting: 0%|##########################################| 0/179.05 [00:07<?, ?s/s]
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
- [ ] **Extract mp3 Metadata**
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
