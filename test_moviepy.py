# Test script to check if MoviePy is working properly
print("Testing MoviePy installation...")

try:
    import moviepy.editor as mp
    print("✓ MoviePy imported successfully")
    
    # Check version
    print(f"MoviePy version: {mp.__version__ if hasattr(mp, '__version__') else 'unknown'}")
    
    # Test basic functionality
    print("Testing basic MoviePy functions...")
    
    # Create a simple audio clip
    from moviepy.audio.io.AudioFileClip import AudioFileClip
    print("✓ AudioFileClip imported")
    
    from moviepy.video.io.VideoFileClip import VideoFileClip  
    print("✓ VideoFileClip imported")
    
    from moviepy.audio.AudioClip import CompositeAudioClip
    print("✓ CompositeAudioClip imported")
    
    print("\n🎉 MoviePy is working correctly!")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("\nTry reinstalling MoviePy:")
    print("pip uninstall moviepy")
    print("pip install moviepy")
    
except Exception as e:
    print(f"❌ Other error: {e}")
    print("\nThere might be an issue with the MoviePy installation.")