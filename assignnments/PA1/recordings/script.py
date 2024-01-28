import os
import subprocess

def convert_m4a_to_mp3(source_folder, target_folder):
    # Ensure the target folder exists
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    for file in os.listdir(source_folder):
        if file.endswith(".m4a"):
            # Construct the full file paths
            source_path = os.path.join(source_folder, file)
            target_path = os.path.join(target_folder, os.path.splitext(file)[0] + ".mp3")
            
            # Construct the ffmpeg command for conversion
            cmd = [
                'ffmpeg',
                '-i', source_path,  # Input file
                '-ar', '16000',  # Set sampling rate to 16kHz
                '-ab', '128k',  # Set bitrate, adjust as needed
                '-map', 'a',  # Map audio streams
                target_path  # Output file
            ]
            
            # Execute the command
            subprocess.run(cmd, check=True)

source_folder = './'
target_folder = './converted'
convert_m4a_to_mp3(source_folder, target_folder)