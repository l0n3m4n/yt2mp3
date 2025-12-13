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
**yt2mp3** is a small project cli music downloader from youtube and convert into various audio formats using the powerful **yt-dlp** library.

"Converting YouTube videos on third party websites carries high risks, hackers can embed executable code or scripts within MP3 files. When you play or open such file, it could potentially execute malicious code and compromise your system."

## ✨ Features
- **Automatic Title Extraction**: Automatically uses the video title as the filename.
- **Playlist Support**: Download entire YouTube playlists.
- **Format Selection**: Choose from various audio formats like mp3, flac, wav.
- **Quality Control**: Specify the audio quality.
- **Metadata Embedding**: Embeds thumbnail and other metadata into the audio file.
- **Duplicate Check**: Avoids re-downloading already existing files.
- **Interactive Mode**: A user-friendly interactive mode for a better experience.

## 📚 Table of Contents
- 📜 [Description](#-description)
- ✨ [Features](#-features)
- 🛠️ [Installation](#-installation)
- ⚙️ [Usage](#-usage)
- 💁 [References](#-references)
- 📝 [Todo](#-todo)
- 👨🏾‍⚖️ [License](#-license)

## 🛠️ Installation
> dependencies (python3 latest)
```bash
sudo apt install python3.11-venv
python3 -m venv venv-yt2mp3
```

```bash
git clone https://github.com/l0n3m4n/yt2mp3.git
cd yt2mp3 && source venv-yt2mp3/bin/activate
pip install -r requirements.txt
```

## ⚙️ Usage
![usage_gif](assets/yt2mp3.gif)
```bash
$ python3 yt2mp3.py --help

        __   ______                  ______
.--.--.|  |_|__    |.--------.-----.|__    |
|  |  ||   _|    __||        |  _  ||__    |
|___  ||____|______||__|__|__|   __||______|
|_____|                      |__|
        Author: l0n3m4n | ⚙️  v1.5.0

usage: yt2mp3.py [-h] [-u URL] [-o ] [-f FORMAT] [-q QUALITY] [-i]

Download a YouTube video and convert to MP3.

options:
  -h, --help             show this help message and exit
  -u, --url URL          YouTube video URL
  -o, --output           Output filename for MP3 (default: video title)
  -f, --format FORMAT    Audio format (e.g., mp3, flac, wav)
  -q, --quality QUALITY  Audio quality (e.g., 192, 320)
  -i, --interactive      Enable interactive mode

Examples:
  Download a single video:
    yt2mp3.py -u "https://www.youtube.com/watch?v=id"

  Download a single video with a specific filename:
    yt2mp3.py -u "https://www.youtube.com/watch?v=id" -o "my_song.mp3"

  Download a playlist to the default music directory:
    yt2mp3.py -u "https://www.youtube.com/playlist?list=id"

  Download a playlist to a specific directory:
    yt2mp3.py -u "https://www.youtube.com/playlist?list=id" -o "my_playlist"

  Download a video in FLAC format with 320 quality:
    yt2mp3.py -u "https://www.youtube.com/watch?v=id" -f flac -q 320
```

## 💁 References
- [**yt-dlp**](https://github.com/yt-dlp/yt-dlp) is a youtube-dl fork with additional features and fixes. It's used for downloading and converting videos.

## 📝 Todo
- [x] **Added progress bar (via yt-dlp's native output)**
- [x] **Playlist Support**
- [x] **Automatic Title Extraction**
- [x] **Metadata Embedding**
- [x] **Format and Quality Selection**
- [x] **Duplicate Song Check**
- [x] **Interactive Mode**
- [x] **Add multiple URL via command**
- [x] **Add multiple URL in a one list e.q `music_list.txt`**

## 👨🏾‍⚖️ License
This project is under terms of the [MIT License](LICENSE). For fixing Bugs, create [issue](https://github.com/l0n3m4n/yt2mp3/issues/new)
