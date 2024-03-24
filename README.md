# Youtube-MP3-MP4-Downloader

Video downloader application with a modern graphical user interface (GUI) using Python.

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

4. **Run the script:**

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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
