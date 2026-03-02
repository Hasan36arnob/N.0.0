# Audio-Video Merge Guide
# This script provides step-by-step instructions for merging your audio files with video

import os

def check_files():
    """Check if all required files exist"""
    print("🔍 Checking required files...")
    
    # Video file
    video_file = r"media\videos\1\1080p60\MathViralVideo.mp4"
    video_exists = os.path.exists(video_file)
    print(f"Video file: {video_file} - {'✅ Found' if video_exists else '❌ Missing'}")
    
    # Audio files
    audio_files = ["click.wav", "pop.wav", "whoosh.wav", "reveal.wav", "success.wav"]
    all_audio_exist = True
    
    for audio_file in audio_files:
        exists = os.path.exists(audio_file)
        print(f"Audio file: {audio_file} - {'✅ Found' if exists else '❌ Missing'}")
        if not exists:
            all_audio_exist = False
    
    return video_exists and all_audio_exist

def main():
    print("=" * 50)
    print("          AUDIO-VIDEO MERGE GUIDE")
    print("=" * 50)
    print()
    
    # Check if files exist
    files_ok = check_files()
    
    if not files_ok:
        print("\n❌ Some files are missing. Please ensure:")
        print("1. You've rendered the video: manim -pql 1.py MathViralVideo")
        print("2. You've created sound files: python create_sounds.py")
        return
    
    print("\n✅ All files are ready!")
    print()
    
    # Option 1: Manual FFmpeg installation
    print("OPTION 1: Install FFmpeg manually")
    print("-" * 40)
    print("1. Download FFmpeg from: https://github.com/BtbN/FFmpeg-Builds/releases")
    print("2. Download 'ffmpeg-master-latest-win64-gpl.zip'")
    print("3. Extract to C:\\ffmpeg")
    print("4. Add C:\\ffmpeg\\bin to your system PATH")
    print("5. Restart command prompt")
    print("6. Run: manual_audio_merge.bat")
    print()
    
    # Option 2: Use online tools
    print("OPTION 2: Use online video editors")
    print("-" * 40)
    print("1. Go to https://www.kapwing.com/")
    print("2. Upload your video file: media/videos/1/1080p60/MathViralVideo.mp4")
    print("3. Upload all audio files: click.wav, pop.wav, whoosh.wav, reveal.wav, success.wav")
    print("4. Adjust audio timing manually")
    print("5. Export and download the final video")
    print()
    
    # Option 3: Use Windows Video Editor
    print("OPTION 3: Use Windows built-in Video Editor")
    print("-" * 40)
    print("1. Open Windows Video Editor")
    print("2. Import your video file")
    print("3. Add audio tracks and adjust timing")
    print("4. Export the final video")
    print()
    
    print("💡 Recommendation: Option 1 (FFmpeg) will give you the best results!")
    print("   Run 'manual_audio_merge.bat' after installing FFmpeg")

if __name__ == "__main__":
    main()