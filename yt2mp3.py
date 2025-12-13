#!/usr/bin/python3

import argparse
import os
import subprocess
import sys
import re
import yt_dlp
import colorama
from colorama import Fore, Style

####################################
# Author: l0n3m4n                  #
# Description: Youtube converter   #
# Version: 1.5.0 (yt-dlp native)   #
####################################



colorama.init(autoreset=True)

class colors:
    RESET = Style.RESET_ALL
    BOLD = Style.BRIGHT
    GREEN = Fore.LIGHTGREEN_EX
    RED = Fore.LIGHTRED_EX
    YELLOW = Fore.LIGHTYELLOW_EX
    CYAN = Fore.LIGHTCYAN_EX
    MAGENTA = Fore.LIGHTMAGENTA_EX
    BLUE = Fore.LIGHTBLUE_EX


class AlignedHelpFormatter(argparse.HelpFormatter):
    def __init__(self, prog, indent_increment=2, max_help_position=30, width=None):
        super().__init__(prog, indent_increment, max_help_position, width)

    def _format_action_item(self, action):
        item = super()._format_action_item(action)
        if action.help:
            item = item.replace('\n', ' ')
        return item

    def _format_action(self, action):
        if action.help:
            action.help = action.help.replace('\n', ' ')
        return super()._format_action(action)


class CustomFormatter(AlignedHelpFormatter, argparse.RawDescriptionHelpFormatter):
    def _format_usage(self, usage, actions, groups, prefix):
        usage_text = super()._format_usage(usage, actions, groups, prefix)
        return f"{colors.CYAN}{usage_text}{colors.RESET}"

    def _format_action_invocation(self, action):
        if not action.option_strings:
            return f"{colors.YELLOW}{super()._format_action_invocation(action)}{colors.RESET}"
        else:
            return f"{colors.YELLOW}{', '.join(action.option_strings)}{colors.RESET}"

    def _expand_help(self, action):
        return f"{colors.BLUE}{super()._expand_help(action)}{colors.RESET}"


def download_and_convert(url, output_dir, output_filename, audio_format, audio_quality):
    try:
        ydl_opts_info = {'quiet': True, 'no_warnings': True}
        with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
            info_dict = ydl.extract_info(url, download=False)

        print(f"{colors.CYAN}📥 Downloading and converting to {audio_format.upper()}{colors.RESET}")

        is_playlist = info_dict.get('_type') == 'playlist'

        if is_playlist:
            if output_filename:
                output_dir = os.path.join(output_dir, output_filename)
                os.makedirs(output_dir, exist_ok=True)
            
            output_template = os.path.join(output_dir, '%(title)s')
            final_message_path = output_dir
        else:  
            if not output_filename:
                video_title = info_dict.get('title', None)
                if video_title:
                    output_filename = re.sub(r'[\\/*?:"<>|]', "", video_title)
                else:
                    print(f"{colors.RED}Could not retrieve video title.{colors.RESET}")
                    return False
            else:
                if output_filename.endswith(f'.{audio_format}'):
                    output_filename = output_filename[:-len(audio_format)-1]
            
            output_template = os.path.join(output_dir, output_filename)
            final_message_path = f"{output_template}.{audio_format}"

        def progress_hook(d):
            if d['status'] == 'downloading':
                total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
                downloaded_bytes = d.get('downloaded_bytes', 0)
                if total_bytes > 0:
                    percent = downloaded_bytes / total_bytes * 100
                    speed = d.get('speed')
                    eta = d.get('eta')

                    status_line = f"\r{colors.CYAN}Downloading: {colors.GREEN}{percent:.1f}%{colors.RESET}"
                    if speed:
                        status_line += f" at {speed / 1024 / 1024:.2f}MiB/s"
                    if eta is not None:
                        status_line += f" ETA {eta}s"
                    sys.stdout.write(status_line)
                    sys.stdout.flush()
            elif d['status'] == 'finished':
                sys.stdout.write(f"\r{colors.CYAN}Download complete. Post-processing...{colors.RESET}\n")
                sys.stdout.flush()

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': audio_format,
                'preferredquality': audio_quality,
            }],
            'embedthumbnail': True,
            'addmetadata': True,
            'outtmpl': output_template,
            'progress_hooks': [progress_hook],
            'quiet': True,   
            'no_warnings': True,
            'extractor_args': {'youtube': {'player_client': ['default']}},
            'download_archive': 'downloaded.txt',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        if is_playlist:
            print(f"{colors.CYAN}🎧 Playlist conversion complete. {audio_format.upper()}s saved in: {final_message_path}{colors.RESET}")
        else:
            print(f"{colors.CYAN}🎧 Conversion complete. {audio_format.upper()} saved at: {final_message_path}{colors.RESET}")
        return True

    except yt_dlp.utils.DownloadError as e:
        print(f"{colors.RED}Error during download: {e}{colors.RESET}")
        return False
    except yt_dlp.utils.ExtractorError as e:
        print(f"{colors.RED}Error extracting video information: {e}{colors.RESET}")
        return False
    except FileNotFoundError:
        print(f"{colors.RED}Error: yt-dlp or ffmpeg not found. Please ensure yt-dlp and ffmpeg are installed and in your system's PATH.{colors.RESET}")
        return False
    except KeyboardInterrupt:
        print(f'\n{colors.RED}Download interrupted by user.{colors.RESET}')
        return False
    except Exception as e:
        print(f"{colors.RED}Unexpected error occurred: {e}{colors.RESET}")
        return False


def main(url, output_filename, audio_format, audio_quality):
    output_dir = './music'
    os.makedirs(output_dir, exist_ok=True)

    if not download_and_convert(url, output_dir, output_filename, audio_format, audio_quality):
        print(f"{colors.RED}\nFailed to download and convert.{colors.RESET}")
        return


if __name__ == "__main__":
    print(f"{colors.CYAN}", end="")
    print(r'''
        __   ______                  ______
.--.--.|  |_|__    |.--------.-----.|__    |
|  |  ||   _|    __||        |  _  ||__    |
|___  ||____|______||__|__|__|   __||______| 
|_____|                      |__|
        Author: l0n3m4n | ⚙️  v1.5.0
''', end="")
    print(f"{colors.RESET}")

    parser = argparse.ArgumentParser(
        description='Download a YouTube video and convert to MP3.',
        epilog=f"""
{colors.MAGENTA}Examples:{colors.RESET}
  {colors.MAGENTA}Download a single video:{colors.RESET}
    yt2mp3.py -u "https://www.youtube.com/watch?v=id"

  {colors.MAGENTA}Download a single video with a specific filename:{colors.RESET}
    yt2mp3.py -u "https://www.youtube.com/watch?v=id" -o "my_song.mp3"

  {colors.MAGENTA}Download a playlist to the default music directory:{colors.RESET}
    yt2mp3.py -u "https://www.youtube.com/playlist?list=id"

  {colors.MAGENTA}Download a playlist to a specific directory:{colors.RESET}
    yt2mp3.py -u "https://www.youtube.com/playlist?list=id" -o "my_playlist"

  {colors.MAGENTA}Download a video in FLAC format with 320 quality:{colors.RESET}
    yt2mp3.py -u "https://www.youtube.com/watch?v=id" -f flac -q 320
""",
        formatter_class=CustomFormatter
    )

    parser.add_argument('-u', '--url', type=str, help='YouTube video URL')
    parser.add_argument('-o', '--output', type=str, required=False, metavar='', help='Output filename for MP3 (default: video title)')
    parser.add_argument('-f', '--format', type=str, default='mp3', help='Audio format (e.g., mp3, flac, wav)')
    parser.add_argument('-q', '--quality', type=str, default='192', help='Audio quality (e.g., 192, 320)')
    parser.add_argument('-i', '--interactive', action='store_true', help='Enable interactive mode')
    args = parser.parse_args()

    if args.interactive:
        try:
            url = input("Enter the YouTube URL: ")
            if not url:
                print(f"{colors.RED}URL cannot be empty.{colors.RESET}")
                exit()
            
            output_filename = input("Enter the output filename (optional, press Enter for auto): ")
            audio_format = input("Enter the audio format (default: mp3): ") or 'mp3'
            audio_quality = input("Enter the audio quality (default: 192): ") or '192'

            main(url, output_filename, audio_format, audio_quality)

        except KeyboardInterrupt:
            print(f"\n{colors.RED}Process interrupted by user.{colors.RESET}")
        except Exception as e:
            print(f"\n{colors.RED}An error occurred: {e}{colors.RESET}")

    elif args.url:
        try:
            main(args.url, args.output, args.format, args.quality)
        except KeyboardInterrupt:
            print(f"\n{colors.RED}Process interrupted by user.{colors.RESET}")
        except Exception as e:
            print(f"\n{colors.RED}An error occurred: {e}{colors.RESET}")
    else:
        parser.print_help()