import os
import numpy as np
from scipy.io import wavfile
from scipy import signal
import soundfile as sf

def create_click_sound():
    """Create a subtle click sound for appearance effects"""
    sample_rate = 44100
    duration = 0.1
    t = np.linspace(0, duration, int(sample_rate * duration))
    
    # Generate a short click with exponential decay
    click = np.sin(2 * np.pi * 1000 * t) * np.exp(-50 * t)
    click *= 0.3  # Reduce volume
    
    wavfile.write("click.wav", sample_rate, click)

def create_pop_sound():
    """Create a pop sound for square appearances"""
    sample_rate = 44100
    duration = 0.15
    t = np.linspace(0, duration, int(sample_rate * duration))
    
    # Generate a pop sound with frequency sweep
    pop = np.sin(2 * np.pi * (800 + 2000 * t) * t) * np.exp(-30 * t)
    pop *= 0.4
    
    wavfile.write("pop.wav", sample_rate, pop)

def create_whoosh_sound():
    """Create a whoosh sound for transformations"""
    sample_rate = 44100
    duration = 0.3
    t = np.linspace(0, duration, int(sample_rate * duration))
    
    # Generate a whoosh sound with decreasing frequency
    whoosh = np.sin(2 * np.pi * (2000 - 1500 * t) * t) * np.exp(-15 * t)
    whoosh *= 0.35
    
    wavfile.write("whoosh.wav", sample_rate, whoosh)

def create_reveal_sound():
    """Create a magical reveal sound for formula appearance"""
    sample_rate = 44100
    duration = 0.4
    t = np.linspace(0, duration, int(sample_rate * duration))
    
    # Generate a magical sound with multiple frequencies
    reveal = (np.sin(2 * np.pi * 800 * t) + 
              np.sin(2 * np.pi * 1200 * t) * 0.5 +
              np.sin(2 * np.pi * 2000 * t) * 0.3) * np.exp(-8 * t)
    reveal *= 0.4
    
    wavfile.write("reveal.wav", sample_rate, reveal)

def create_success_sound():
    """Create a success/fanfare sound for conclusion"""
    sample_rate = 44100
    duration = 0.8
    t = np.linspace(0, duration, int(sample_rate * duration))
    
    # Generate a triumphant success sound
    success = (np.sin(2 * np.pi * 523.25 * t) +  # C5
              np.sin(2 * np.pi * 659.25 * t) * 0.7 +  # E5
              np.sin(2 * np.pi * 783.99 * t) * 0.5) * np.exp(-3 * t)  # G5
    success *= 0.3
    
    wavfile.write("success.wav", sample_rate, success)

if __name__ == "__main__":
    print("Creating sound effects for your animation...")
    create_click_sound()
    create_pop_sound()
    create_whoosh_sound()
    create_reveal_sound()
    create_success_sound()
    print("Sound files created: click.wav, pop.wav, whoosh.wav, reveal.wav, success.wav")
    print("Place these files in the same directory as your animation script.")