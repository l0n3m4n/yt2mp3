#!/usr/bin/python3

import argparse
import os
import subprocess
import sys
import re

####################################
# Author: l0n3m4n                  #
# Description: Youtube converter   #
# Version: 1.4.0 (yt-dlp native)   #
####################################


class colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"


def download_and_convert(url, output_path):
    try:
        print(f"{colors.CYAN}📥 Downloading and converting to MP3{colors.RESET}")

        command = [
            "yt-dlp",
            "-x",
            "--audio-format", "mp3",
            "-o", output_path,
            url
        ]

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

        last_progress_line = ""
        for line in process.stdout:
            if "[download]" in line and ("%" in line or "ETA" in line):
                match = re.search(r'(\d+\.\d+%)|\[download\]\s*(\d+)%', line)
                if match:
                    percentage_str = match.group(1) if match.group(1) else match.group(2) + '%'
                    colored_percentage = f"{colors.GREEN}{percentage_str}{colors.RESET}"
                    colored_line = line.replace(percentage_str, colored_percentage)
                    last_progress_line = colored_line.strip()
                else:
                    last_progress_line = line.strip()  

                print(f"\r{last_progress_line}", end="")
                sys.stdout.flush()
            elif "[ExtractAudio]" in line and "file is already in target format" in line:
                print(f"\r{line.strip()}") 
                last_progress_line = "" 
            elif "[download] Destination:" in line:
                print(f"\r{line.strip()}")
                last_progress_line = ""

        process.wait() 

        if last_progress_line:
            print("\n", end="") 

        if process.returncode != 0:
            print(f"{colors.RED}yt-dlp failed. Check yt-dlp's output for details.{colors.RESET}")
            return False

        print(f"{colors.CYAN}🎧 Conversion complete. MP3 saved at: {output_path}{colors.RESET}")
        return True

    except KeyboardInterrupt:
        print(f'\n{colors.RED}Download interrupted by user.{colors.RESET}')
        return False
    except Exception as e:
        print(f"{colors.RED}Unexpected error occurred: {e}{colors.RESET}")
        return False


def main(url, output_filename):
    output_dir = './music'
    os.makedirs(output_dir, exist_ok=True)
    mp3_output_path = os.path.join(output_dir, output_filename)

    if not download_and_convert(url, mp3_output_path):
        print(f"{colors.RED}\nFailed to download and convert video.{colors.RESET}")
        return


if __name__ == "__main__":
    print(f"{colors.CYAN}", end="")
    print(r'''
        __   ______                  ______
.--.--.|  |_|__    |.--------.-----.|__    |
|  |  ||   _|    __||        |  _  ||__    |
|___  ||____|______||__|__|__|   __||______| 
|_____|                      |__|
        Author: l0n3m4n | ⚙️  v1.4
''', end="")
    print(f"{colors.RESET}")

    parser = argparse.ArgumentParser(
        description='Download a YouTube video and convert to MP3.',
        epilog=f'{colors.CYAN}Ex:   python3 yt2mp3.py -u 'https://www.youtube.com/watch?v=id' -o music_title.mp3{colors.RESET}'
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