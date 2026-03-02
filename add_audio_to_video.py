import os
import subprocess
import sys

def check_ffmpeg():
    """Check if FFmpeg is installed and available"""
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def combine_audio_with_video(video_path, audio_files, output_path):
    """Combine video with multiple audio files using FFmpeg"""
    
    # Create filter complex string for multiple audio files
    audio_filters = []
    audio_inputs = []
    
    for i, audio_file in enumerate(audio_files):
        if os.path.exists(audio_file):
            audio_inputs.extend(["-i", audio_file])
            audio_filters.append(f"[{i+1}:a]adelay={i*1000}|{i*1000}[a{i+1}]")
    
    if not audio_inputs:
        print("No audio files found to combine!")
        return False
    
    # Combine all audio streams
    filter_complex = ";".join(audio_filters)
    filter_complex += f";{'|'.join([f'a{i+1}' for i in range(len(audio_filters))])}amix=inputs={len(audio_filters)}:duration=longest"
    
    # FFmpeg command
    cmd = [
        "ffmpeg", "-i", video_path,
        *audio_inputs,
        "-filter_complex", filter_complex,
        "-c:v", "copy",  # Copy video stream without re-encoding
        "-map", "0:v:0", # Map video from first input
        "-map", f"[{len(audio_filters)}]a", # Map mixed audio
        "-shortest",
        output_path
    ]
    
    try:
        print(f"Combining audio with video: {video_path}")
        subprocess.run(cmd, check=True)
        print(f"Successfully created: {output_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error combining audio: {e}")
        return False

def main():
    # Check if FFmpeg is installed
    if not check_ffmpeg():
        print("FFmpeg is not installed. Please install it first:")
        print("1. Download from: https://ffmpeg.org/download.html")
        print("2. Or install using chocolatey: choco install ffmpeg")
        print("3. Add FFmpeg to your system PATH")
        return
    
    # Video file path (assuming the latest rendered video)
    video_file = r"media\videos\1\1080p60\MathViralVideo.mp4"
    
    if not os.path.exists(video_file):
        print(f"Video file not found: {video_file}")
        print("Please make sure you've rendered the video first with: manim -pql 1.py MathViralVideo")
        return
    
    # Audio files to combine
    audio_files = ["click.wav", "pop.wav", "whoosh.wav", "reveal.wav", "success.wav"]
    
    # Output file
    output_file = "MathViralVideo_WithAudio.mp4"
    
    # Combine audio with video
    success = combine_audio_with_video(video_file, audio_files, output_file)
    
    if success:
        print(f"\nDone! Your video with audio is saved as: {output_file}")
        print("You can now play this file with any media player.")

if __name__ == "__main__":
    main()