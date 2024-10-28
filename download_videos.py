import os
import subprocess

# text file containing the list of video URLs 
url_file = 'urls.txt'

# Function to get the highest quality MP4 format (select the last MP4 format)
def get_best_format(url):
    result = subprocess.run(['python', '-m', 'yt_dlp', '-F', url], capture_output=True, text=True)
    
    # Parse the result to find the highest quality MP4 format
    formats = result.stdout.splitlines()
    
    best_format = None
    for line in reversed(formats):  # Loop in reverse to get the last MP4 format
        if 'mp4' in line and 'video only' in line:
            best_format = line.split()[0]  # Get the format code 
            break
    
    return best_format

# Function to download the best format
def download_video(url, format_code):
    if format_code:
        subprocess.run(['python', '-m', 'yt_dlp', '-f', format_code, url])
    else:
        print(f"Could not find MP4 format for {url}")

# Main script to process each URL
with open(url_file, 'r') as file:
    urls = file.readlines()

for url in urls:
    url = url.strip() 
    print(f"Processing {url}...")
    
   
    best_format = get_best_format(url)
    
    if best_format:
        print(f"Downloading best MP4 format {best_format} for {url}")
        download_video(url, best_format)
    else:
        print(f"No suitable MP4 format found for {url}")
