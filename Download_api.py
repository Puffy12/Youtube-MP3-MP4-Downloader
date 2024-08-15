# API call examples
# python Download_api.py https://www.youtube.com/watch?v=VIDEO_ID MP4 720p
# python Download_api.py delete
# IMPORTANT  to activate the environment imports run 
#  .\Scripts\activate        
#  deactivate 

import sys
import os
from pytubefix import YouTube
from pytubefix.cli import on_progress

def download_youtube_video(link, format_type, quality="720p"):
    url = link
    download_format = format_type.upper()
    resolution = quality

    try:
        if download_format == "MP3":
            video = YouTube(url, on_progress_callback=on_progress)
            title = video.title
            print("Downloading MP3...")
            
            # Download audio 
            os.path.join("downloads", f"{title}.mp3")
            stream = video.streams.filter(only_audio=True).first() 
            out_file = stream.download(output_path="downloads")
            
            # save the file and convert to mp3 
            base, ext = os.path.splitext(out_file) 
            new_file = base + '.mp3'
            os.rename(out_file, new_file) 
             
        elif download_format == "MP4":
            print(f"Downloading MP4 in {quality}...")
            video = YouTube(url, on_progress_callback=on_progress)
            title = video.title
    
            # Download video to path
            stream = video.streams.filter(res=resolution).first()
            os.path.join("downloads", f"{title}.mp4")
            stream.download(output_path="downloads")
            
        else:
            print("Invalid format type. Please specify either MP3 or MP4.")
            return
        
        print("Download completed successfully!")
    except Exception as e:
        print(f"Error: {e}")
        
# download_youtube_video End 

def delete_downloads():
    download_folder = "downloads"  #downloads folder
    for file_name in os.listdir(download_folder):
        file_path = os.path.join(download_folder, file_name)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                print(f"Deleted {file_path}")
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")
            
# delete_downloads End 

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = bytes_downloaded / total_size * 100
    
    print(f"{round(percentage, 2)}%")

# delete_on_progress End

if __name__ == "__main__":
    if sys.argv[1] == "delete":
        print("Delete all downloads")
        delete_downloads()
    elif len(sys.argv) < 3:
        print("Invalid Argument")
        print("Usage: python Download_api.py <YouTube Link> <Format> [<Quality>]")
        print("Example: python Download_api.py https://www.youtube.com/watch?v=VIDEO_ID MP4 720p")
        print("To delete all downloads: python Download_api.py delete")
    else:
        print("Download Started")
        link = sys.argv[1]
        format_type = sys.argv[2]
        quality = sys.argv[3] if len(sys.argv) >= 4 else "720p"
        download_youtube_video(link, format_type, quality)
