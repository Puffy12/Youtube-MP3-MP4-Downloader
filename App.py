# IMPORTANT  to activate the environment imports run 
#  .\Scripts\activate        
#  deactivate 

import customtkinter as ctk
from tkinter import ttk
from pytubefix import YouTube
from pytubefix.cli import on_progress
import os


MillSecond_clear_Delay = 7000 

def Download_Video():

    url = entry_url.get()
    download_format = format_var.get()
    resolution = Resolution_var.get()
    
    progress_label.pack(pady="10p 5p")
    progress_bar.pack(pady="10p 5p")
    status_label.pack(pady="10p 5p")
    
    try:
        
        if download_format == "MP3":
            video = YouTube(url, on_progress_callback=on_progress)
            title = video.title
            
            # Download audio 
            os.path.join("downloads", f"{title}.mp3")
            stream = video.streams.filter(only_audio=True).first() 
            out_file = stream.download(output_path="downloads")
            
            # save the file and convert to mp3 
            base, ext = os.path.splitext(out_file) 
            new_file = base + '.mp3'
            os.rename(out_file, new_file) 
            
            status_label.configure(text="Mp3 Download Successful", text_color="white", fg_color="green")
            
        else:
            
            video = YouTube(url, on_progress_callback=on_progress)
            title = video.title
            
            # Download video to path
            stream = video.streams.filter(res=resolution).first()
            os.path.join("downloads", f"{title}.mp4")
            stream.download(output_path="downloads")
            
            status_label.configure(text="Mp4 Download Successful", text_color="white", fg_color="green")
        
        
        root.after(MillSecond_clear_Delay, clear_status_label)  # Clear status label 
        
    except Exception as e:
        status_label.configure(text=f"Error: {str(e)}", text_color="white", fg_color="red")
        root.after(MillSecond_clear_Delay, clear_status_label)  # Clear status label 
        
# Download_Video End

def clear_status_label():
    status_label.configure(text="")
    progress_bar.set(0)
    progress_label.configure(text="0%")
    
# clear_status_label End

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = bytes_downloaded / total_size * 100
    
    progress_label.configure(text= str(int(percentage)) + "%")
    progress_label.update()
    
    progress_bar.set(float(percentage / 100))
# on_progress End

def delete_downloads():
    download_folder = "downloads"  #downloads folder
    for file_name in os.listdir(download_folder):
        file_path = os.path.join(download_folder, file_name)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")   
    
    status_label.configure(text="All Downloadeds Deleted Successfully", text_color="white", fg_color="red")
    root.after(MillSecond_clear_Delay, clear_status_label)  # Clear status label 
            
# end delete_downloads

# create root window
root = ctk.CTk()

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")
# Title of window
root.title("Youtuber Downloader")

# Set Window Width and Height
root.geometry("720x480")
root.minsize(720, 480)
root.maxsize(1080, 720)

# Create a frame that holds content
content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

# Create label and entry widget for video url
url_label = ctk.CTkLabel(content_frame, text="Enter the Youtube URL : ")
entry_url = ctk.CTkEntry(content_frame, width=400, height=40)
url_label.pack(pady="10p 5p")
entry_url.pack(pady="10p 5p")

# Dowload Button
download_button = ctk.CTkButton(content_frame, text="Download", command=Download_Video)
download_button.pack(pady="10p 5p")

# Create Resolution Box
Resolutions = ["1080p","720p","360p","240p"]
Resolution_var = ctk.StringVar()
Resolution_Combobox = ttk.Combobox(content_frame, values=Resolutions, textvariable=Resolution_var)
Resolution_Combobox.pack(pady="10p 5p")
Resolution_Combobox.set("720p")

# Create Dowload progress bar
progress_label = ctk.CTkLabel(content_frame, text="0%")
progress_label.pack(pady="10p 5p")

progress_bar = ctk.CTkProgressBar(content_frame, width=400)
progress_bar.set(0)

# Create status label
status_label = ctk.CTkLabel(content_frame, text="")

# Create button for choosing format
format_label = ctk.CTkLabel(content_frame, text="Choose Download Format:")
format_label.pack(pady="10p 5p")

format_var = ctk.StringVar()
format_radio_mp3 = ctk.CTkRadioButton(content_frame, text="MP3", variable=format_var, value="MP3")
format_radio_mp3.pack(pady="5p")
format_radio_mp4 = ctk.CTkRadioButton(content_frame, text="MP4", variable=format_var, value="MP4")
format_radio_mp4.pack(pady="5p")

# Default format selection
format_var.set("MP4")

# Create red button at bottom left to delete all files in the downloads folder
delete_button = ctk.CTkRadioButton(content_frame, text="Delete All Files", bg_color="red", command=delete_downloads)
delete_button.pack(side="bottom", anchor="se", pady=5, padx=5)


# Starts the app
root.mainloop()