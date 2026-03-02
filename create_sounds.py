# Simple sound file creator - creates empty sound files for Manim
# These will work with the add_sound() function in your animation

def create_empty_sound(filename, duration_ms=100):
    """Create a minimal WAV file that Manim can use"""
    with open(filename, 'wb') as f:
        # Minimal WAV header for empty sound
        f.write(b'RIFF\x24\x00\x00\x00WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00')
        f.write(b'\x44\xac\x00\x00\x88\x58\x01\x00\x02\x00\x10\x00data\x00\x00\x00\x00')

if __name__ == "__main__":
    print("Creating placeholder sound files for Manim...")
    create_empty_sound("click.wav")
    create_empty_sound("pop.wav") 
    create_empty_sound("whoosh.wav")
    create_empty_sound("reveal.wav")
    create_empty_sound("success.wav")
    print("Sound files created: click.wav, pop.wav, whoosh.wav, reveal.wav, success.wav")
    print("These are placeholder files - replace them with real sound files later.")
    print("You can now run your animation: manim -pql 1.py MathViralVideo")