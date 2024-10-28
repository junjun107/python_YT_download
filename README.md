# YouTube Video Downloader Script

This Python script automates the process of downloading the highest quality MP4 video from a list of YouTube URLs using `yt-dlp`. It selects the last MP4 video-only format (typically the highest quality available) and downloads it for each URL in the list.

## Prerequisites

Ensure you have the following installed on your system before running the script:

1. **Python**: Make sure Python is installed. You can download it from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. **yt-dlp**: This script relies on `yt-dlp`, a YouTube download tool. You can install it via pip:

   ```bash
   pip install yt-dlp
   ```

**A file with YouTube URLs**: Create a text file named urls.txt in the same directory as this script. Each line should contain a single YouTube URL you want to download. 3. A file with YouTube URLs: Create a text file named urls.txt in the same directory as this script. Each line should contain a single YouTube URL you want to download.

## Usage

1. Prepare the URL list:

Create a text file named urls.txt.
Add all the YouTube video URLs you want to download, one per line.
Run the script:

Open a terminal or command prompt in the folder where the script is located. 2. Run the script using Python:
`python your_script_name.py`

3. Downloading process:

The script will read through urls.txt and for each URL, it will:
Find the available formats using yt-dlp.
Select the last MP4 format available (usually the highest quality).
Download the selected format.

4. Output:

The downloaded videos will be saved in the **current working** directory.

## Troubleshooting

1. No suitable MP4 format found: If you get a message saying no suitable MP4 format was found for a URL, check if the video is available in MP4 format. You can manually inspect the available formats using the following command:

`python -m yt-dlp -F <YouTube-URL>`

2. Update yt-dlp: If the script isn't working as expected, ensure that yt-dlp is up to date:

`pip install -U yt-dlp`
