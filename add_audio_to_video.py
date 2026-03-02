import os
import sys

def check_moviepy():
    """Check if MoviePy is installed"""
    try:
        import moviepy.editor as mp
        return True
    except ImportError:
        return False

def combine_audio_with_moviepy(video_path, audio_files, output_path):
    """Combine video with multiple audio files using MoviePy"""
    try:
        import moviepy.editor as mp
        
        print(f"Loading video: {video_path}")
        video = mp.VideoFileClip(video_path)
        
        # Create audio clips with proper timing
        audio_clips = []
        
        # Adjust these timings based on when sounds should play in your animation
        sound_timings = [
            ("click.wav", 1.0),    # After triangle appears
            ("pop.wav", 3.0),      # After squares appear  
            ("whoosh.wav", 5.0),   # During transformation
            ("reveal.wav", 7.0),   # When formula appears
            ("success.wav", 9.0)   # Final conclusion
        ]
        
        for audio_file, start_time in sound_timings:
            if os.path.exists(audio_file):
                audio_clip = mp.AudioFileClip(audio_file).set_start(start_time)
                audio_clips.append(audio_clip)
                print(f"Added {audio_file} at {start_time}s")
        
        if not audio_clips:
            print("No audio files found to combine!")
            return False
        
        # Combine all audio clips
        final_audio = mp.CompositeAudioClip(audio_clips)
        
        # Set audio to video
        final_video = video.set_audio(final_audio)
        
        # Export final video
        print("Exporting video with audio (this may take a few minutes)...")
        final_video.write_videofile(output_path, verbose=False, logger=None)
        
        print(f"Successfully created: {output_path}")
        return True
        
    except Exception as e:
        print(f"Error combining audio with MoviePy: {e}")
        return False

def main():
    # Check if MoviePy is installed
    if not check_moviepy():
        print("MoviePy is not installed. Please install it first:")
        print("pip install moviepy")
        return
    
    # Video file path
    video_file = r"media\videos\1\1080p60\MathViralVideo.mp4"
    
    if not os.path.exists(video_file):
        print(f"Video file not found: {video_file}")
        print("Please make sure you've rendered the video first with: manim -pql 1.py MathViralVideo")
        return
    
    # Audio files to combine
    audio_files = ["click.wav", "pop.wav", "whoosh.wav", "reveal.wav", "success.wav"]
    
    # Check if audio files exist
    missing_files = [f for f in audio_files if not os.path.exists(f)]
    if missing_files:
        print(f"Missing audio files: {missing_files}")
        print("Please run: python create_sounds.py")
        return
    
    # Output file
    output_file = "MathViralVideo_WithAudio.mp4"
    
    # Combine audio with video using MoviePy
    print("Using MoviePy to combine audio with video...")
    success = combine_audio_with_moviepy(video_file, audio_files, output_file)
    
    if success:
        print(f"\n🎉 Done! Your video with audio is saved as: {output_file}")
        print("You can now play this file with any media player!")
    else:
        print("Failed to combine audio with video.")

if __name__ == "__main__":
    main()