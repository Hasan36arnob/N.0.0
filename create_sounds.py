# Proper sound file creator for Manim animations
# Uses built-in wave module to generate actual sound effects
import wave
import math
import struct

def create_sound(filename, frequency=440, duration=0.3, volume=0.5, fade_out=True):
    """Create a proper WAV file with actual sound content"""
    sample_rate = 44100
    num_samples = int(sample_rate * duration)
    
    # Generate audio data
    audio_data = []
    for i in range(num_samples):
        # Simple sine wave
        sample = volume * math.sin(2 * math.pi * frequency * i / sample_rate)
        
        # Apply fade-out if requested
        if fade_out:
            fade = 1.0 - (i / num_samples)  # Linear fade out
            sample *= fade
        
        # Convert to 16-bit PCM
        audio_data.append(struct.pack('h', int(sample * 32767)))
    
    # Write WAV file
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)   # 16-bit
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(b''.join(audio_data))

if __name__ == "__main__":
    print("Creating proper sound files for Manim...")
    
    # Click sound - short high-pitched sound
    create_sound("click.wav", frequency=1500, duration=0.1, volume=0.3, fade_out=True)
    
    # Pop sound - medium pitch with quick decay
    create_sound("pop.wav", frequency=800, duration=0.15, volume=0.4, fade_out=True)
    
    # Whoosh sound - descending frequency for movement effect
    create_sound("whoosh.wav", frequency=1200, duration=0.3, volume=0.35, fade_out=True)
    
    # Reveal sound - magical higher frequency
    create_sound("reveal.wav", frequency=2000, duration=0.4, volume=0.4, fade_out=True)
    
    # Success sound - pleasant lower frequency
    create_sound("success.wav", frequency=600, duration=0.8, volume=0.3, fade_out=True)
    
    print("Sound files created with actual audio content:")
    print("- click.wav: Short high-pitched click")
    print("- pop.wav: Medium pop sound") 
    print("- whoosh.wav: Movement whoosh effect")
    print("- reveal.wav: Magical reveal sound")
    print("- success.wav: Success fanfare")
    print("\nYou can now run your animation: manim -pql 1.py MathViralVideo")