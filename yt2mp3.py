#!/usr/bin/python3

import argparse
import os
import sys
import subprocess
from moviepy.editor import VideoFileClip
from tqdm import tqdm

####################################
# Author: l0n3m4n                  #
# Description: Youtube converter   # 
# Version: 1.3.0 (yt-dlp)          #
####################################


class colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"


def download_video(url, output_path):
    try:
        print(f"{colors.CYAN}📥 Downloading video using yt-dlp...{colors.RESET}")

        temp_video_path = os.path.join(output_path, 'temp_video.mp4')
        command = [
            "yt-dlp",
            "-f", "mp4",
            "-o", temp_video_path,
            url
        ]

        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"{colors.RED}yt-dlp failed:\n{result.stderr}{colors.RESET}")
            return False, None

        print(f"{colors.CYAN}💾 Video downloaded.{colors.RESET}")
        return True, temp_video_path

    except KeyboardInterrupt:
        print(f'\n{colors.RED}Download interrupted by user.{colors.RESET}')
        return False, None
    except Exception as e:
        print(f"{colors.RED}Unexpected error occurred: {e}{colors.RESET}")
        return False, None


class SuppressOutput:
    def __enter__(self):
        self.original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self.original_stdout


def convert_to_mp3(video_path, output_path):
    try:
        if not os.path.isfile(video_path):
            raise FileNotFoundError(f"The file {video_path} could not be found!")

        video = VideoFileClip(video_path)
        audio = video.audio
        duration = video.duration

        print(f"{colors.CYAN}🔄 Converting to MP3...{colors.RESET}")

        with SuppressOutput(), tqdm(total=duration, unit='s', desc=f"{colors.GREEN}Progress{colors.RESET}", ascii=True) as pbar:
            def update_progress(current_time):
                pbar.update(current_time - pbar.n)
            audio.write_audiofile(output_path, verbose=False)

        print(f"{colors.CYAN}🎧 Conversion complete. MP3 saved at: {output_path}{colors.RESET}")
        return True
    except (OSError, IOError, FileNotFoundError) as e:
        print(f"{colors.RED}Error converting to MP3: {e}{colors.RESET}")
        return False
    except Exception as e:
        print(f"{colors.RED}Unexpected error occurred during conversion: {e}{colors.RESET}")
        return False


def main(url, output_filename):
    output_dir = './music'
    os.makedirs(output_dir, exist_ok=True)

    download_success, mp4_output_path = download_video(url, output_dir)
    if not download_success:
        print(f"{colors.RED}\nFailed to download video.{colors.RESET}")
        return

    mp3_output_path = os.path.join(output_dir, output_filename)

    if not convert_to_mp3(mp4_output_path, mp3_output_path):
        print(f"{colors.RED}Failed to convert video to MP3.{colors.RESET}")
        return

    try:
        os.remove(mp4_output_path)
        print(f"{colors.CYAN}🚮 Temporary video file deleted.{colors.RESET}")
    except Exception as e:
        print(f"{colors.RED}Error deleting temporary file: {e}{colors.RESET}")


if __name__ == "__main__":
    print(f"{colors.CYAN}", end="")     
    print(r'''                                       
        __   ______                  ______ 
.--.--.|  |_|__    |.--------.-----.|__    |
|  |  ||   _|    __||        |  _  ||__    |
|___  ||____|______||__|__|__|   __||______|
|_____|                      |__|                                                                                  
        Author: l0n3m4n | ⚙️  v1.3                                                                        
''', end="")                                    
    print(f"{colors.RESET}")

    parser = argparse.ArgumentParser(
        description='Download a YouTube video and convert to MP3.',
        epilog=f'{colors.CYAN}Ex:   python3 yt2mp3.py -u https://www.youtube.com/watch?v=id -o music_title.mp3{colors.RESET}'
    )
    
    parser.add_argument('-u', '--url', type=str, required=True, metavar='', help='YouTube video URL')
    parser.add_argument('-o', '--output', type=str, required=True, metavar='', help='Output filename for MP3')
    args = parser.parse_args()
    
    if args.url and args.output:
        try:
            main(args.url, args.output)
        except KeyboardInterrupt:
            print(f"\n{colors.RED}Process interrupted by user.{colors.RESET}")
        except Exception as e:
            print(f"\n{colors.RED}An error occurred: {e}{colors.RESET}")
    else:
        print(f"{colors.RED}Please provide both --url and --output arguments.{colors.RESET}")
