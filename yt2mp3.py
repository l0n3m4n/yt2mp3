import argparse
import os
import sys
import requests
from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable
from moviepy.editor import VideoFileClip
from tqdm import tqdm

# Global colors
class colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"


# Downloading youtube video
def download_video(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(file_extension='mp4').first()
        total_bytes = stream.filesize
        
        print(f"{colors.CYAN}📥 Downloading video...{colors.RESET}")

        # Download with progress bar
        response = requests.get(stream.url, stream=True)
        with open(os.path.join(output_path, 'temp_video.mp4'), 'wb') as f:
            total_size = int(response.headers.get('content-length', 0))
            with tqdm(total=total_size, unit='B', unit_scale=True, desc=f"{colors.GREEN}Progress{colors.RESET}", ascii=True) as pbar:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        pbar.update(len(chunk))

        print(f"{colors.CYAN}💾 Video downloaded.{colors.RESET}")
        return True, os.path.join(output_path, 'temp_video.mp4')  # Return the path to the downloaded video
    except (RegexMatchError, VideoUnavailable) as e:
        print(f"{colors.RED}Error: {e}{colors.RESET}")
        return False, None
    except Exception as e:
        print(f"{colors.RED}Unexpected error occurred: {e}{colors.RESET}")
        return False, None
    
# Removing Moviepy output
class SuppressOutput:
    def __enter__(self):
        # Suppress stdout
        self.original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Restore stdout
        sys.stdout.close()
        sys.stdout = self.original_stdout

# Coverting temp_video.mp4 to mp3
def convert_to_mp3(video_path, output_path):
    try:
        if not os.path.isfile(video_path):
            raise FileNotFoundError(f"The file {video_path} could not be found!")

        video = VideoFileClip(video_path)
        audio = video.audio
        duration = video.duration

        print(f"{colors.CYAN}🔄 Converting to MP3...{colors.RESET}")

        # Call SuppressOutput class to suppress MoviePy output.
        with SuppressOutput(), tqdm(total=duration, unit='s', desc=f"{colors.GREEN}Progress{colors.RESET}", ascii=True) as pbar:
            def update_progress(current_time):
                pbar.update(current_time - pbar.n)

            # Write audio to file
            audio.write_audiofile(output_path, verbose=False)

        print(f"{colors.CYAN}🎧 Conversion complete. MP3 saved at: {output_path}{colors.RESET}")
        return True
    except (OSError, IOError, FileNotFoundError) as e:
        print(f"Error converting to MP3: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error occurred during conversion: {e}")
        return False

# This area is for future enhancement

# Todo: Adding multiple URL
def AddMultipleUrl():
    return None

# Todo: Extract mp3 Metadata encluding Title, Genre, Date, Name, Year and etc.
def MetadataExtraction():
    return None

# Todo: GUI Integration 
def yt3mp3_GUI():
    return None



# main function 
def main(url, output_filename):
    output_dir = './music'
    os.makedirs(output_dir, exist_ok=True)

    download_success, mp4_output_path = download_video(url, output_dir)
    if not download_success:
        print(f"{colors.RED}Failed to download video. Exiting...{colors.RESET}")
        return

    mp3_output_path = os.path.join(output_dir, output_filename)

    # Convert to MP3
    if not convert_to_mp3(mp4_output_path, mp3_output_path):
        print(f"{colors.RED}Failed to convert video to MP3. Exiting...{colors.RESET}")
        return

    # Clean up temporary video file
    try:
        os.remove(mp4_output_path)
        print(f"{colors.CYAN}🚮 Temporary video file deleted.{colors.RESET}")
    except Exception as e:
        print(f"{colors.RED}Error deleting temporary file: {e}{colors.RESET}")

if __name__ == "__main__":
    # yt2mp3 banner
    print(f"{colors.CYAN}", end="")     
    print(r'''                                       
               ,--.   ,---.                  ,----.  
    ,--. ,--.,-'  '-.'.-.  \,--,--,--.,---. '.-.  | 
    \  '  / '-.  .-' .-' .'|        || .-. |  .' <  
     \   '    |  |  /   '-.|  |  |  || '-' '/'-'  | 
    .-'  /     `--'  '-----'`--`--`--'|  |-' `----'  
    `---'                             `--'                                                                        
            💻 ALDrin / ⚔️ l0n3m4n / ⚙️ v1.0.1                                                                        
''', end="")                                    
    print(f"{colors.RESET}")
    parser = argparse.ArgumentParser(description='Download a YouTube video and convert to MP3.',
                                     epilog='Example usage: python3 yt2mp3.py --url https://www.youtube.com/watch?v=_sw22iEp9WU --output music_name.mp3')
    
    parser.add_argument('--url', type=str, default='https://www.youtube.com/watch?v=_sw22iEp9WU', help='YouTube video URL')
    parser.add_argument('-o', '--output', type=str, default='output.mp3', help='Output filename for MP3')
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


