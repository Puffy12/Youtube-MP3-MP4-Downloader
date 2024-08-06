# Youtube-MP3-MP4-Downloader

YouTube Downloader is a Python application that allows users to download YouTube videos or extract audio from videos quickly and easily. It provides a simple graphical user interface (GUI) built using the Tkinter library for Python.

## Features

    - Download Videos: Download YouTube videos directly to your local machine.
    - Extract Audio: Convert YouTube videos to MP3 format and save them as audio files.
    - Customizable Resolution: Choose from different resolutions (1080p, 720p, 360p, 240p) for video downloads.
    - Download Progress: Monitor the download progress with a progress bar and percentage display.
    - Error Handling: Provides error messages for invalid URLs or failed downloads.
    - File Management: Option to delete all downloaded files with a single click.

## Run 

    -This will Run the application with the GUI
    ```
    python3 App.py
    ```

## Prerequisites

- Python 3.x
- `pytube` library (install via `pip install pytube`)

## Usage

1. **Clone this repository to your local machine:**

    ```
    git clone https://github.com/your_username/YouTube-Downloader.git
    ```

2. **Navigate to the project directory:**

    ```
    cd YouTube-Downloader
    ```

3. **Activate a virtual environment (optional but recommended):**

    - On Windows:
    
        ```
        .\Scripts\activate
        ```
    
    - On macOS/Linux:
    
        ```
        source venv/bin/activate
        ```


4. **Using API:**

    - To download a video:
    
        ```
        python Download_api.py <YouTube Link> <Format> [<Quality>]
        ```

        - Example: Download an MP4 video in 720p quality
          
            ```
            python Download_api.py https://www.youtube.com/watch?v=VIDEO_ID MP4 720p
            ```

    - To delete all downloads:
    
        ```
        python Download_api.py delete
        ```

5. Follow the prompts to download the video or delete all downloads.

### IMPORTANT

To activate the environment imports, run the following commands:

- Activate the environment:
  
    ```
    .\Scripts\activate
    ```

- Deactivate the environment:
  
    ```
    deactivate
    ```

