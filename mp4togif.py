# sandy.g.cabanes
# Title: mp4togif.py
# Description: converts mp4 file to gif
# Date: August 3, 2024
# ------------------------------------------------------------
import os
from moviepy.editor import VideoFileClip

def convert_mp4_to_gif():
    # Input for MP4 file path and name
    mp4_path = input("Enter the path and filename of the MP4 file: ")

    # Input for output GIF path
    output_path = input("Enter the output path for the GIF file: ")

    # Extract filename without extension
    filename = os.path.splitext(os.path.basename(mp4_path))[0]

    # Create output GIF filename
    gif_filename = f"{filename}.gif"

    # Full path for output GIF
    gif_path = os.path.join(output_path, gif_filename)

    try:
        # Load the video clip
        video = VideoFileClip(mp4_path)

        # Write the GIF file
        video.write_gif(gif_path)

        print(f"Conversion complete! GIF saved as: {gif_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        # Close the video to release resources
        if 'video' in locals():
            video.close()

if __name__ == "__main__":
    convert_mp4_to_gif()