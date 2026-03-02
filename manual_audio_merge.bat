@echo off
echo ================================
echo   Manual Audio-Video Merger
echo ================================
echo.

REM Check if FFmpeg is available
where ffmpeg >nul 2>&1
if %errorlevel% equ 0 (
    echo ✓ FFmpeg found in PATH
    goto :merge_audio
) else (
    echo ❌ FFmpeg not found in PATH
    echo.
    echo Please install FFmpeg manually:
    echo 1. Download from: https://github.com/BtbN/FFmpeg-Builds/releases
    echo 2. Extract to C:\ffmpeg
    echo 3. Add C:\ffmpeg\bin to your system PATH
    echo 4. Restart command prompt and run this script again
    echo.
    pause
    exit /b 1
)

:merge_audio
echo.
echo Merging audio files with video...
echo.

REM FFmpeg command to merge all audio files with video
ffmpeg -i "media\videos\1\1080p60\MathViralVideo.mp4" ^
       -i "click.wav" ^
       -i "pop.wav" ^
       -i "whoosh.wav" ^
       -i "reveal.wav" ^
       -i "success.wav" ^
       -filter_complex "[1:a][2:a][3:a][4:a][5:a]amix=inputs=5:duration=longest[a]" ^
       -map "0:v:0" ^
       -map "[a]" ^
       -c:v copy ^
       -shortest ^
       "MathViralVideo_WithAudio.mp4"

if %errorlevel% equ 0 (
    echo.
    echo ✅ SUCCESS: Audio merged successfully!
    echo Final video: MathViralVideo_WithAudio.mp4
) else (
    echo.
    echo ❌ ERROR: Failed to merge audio
    echo Check if all files exist:
    echo - media\videos\1\1080p60\MathViralVideo.mp4
    echo - click.wav, pop.wav, whoosh.wav, reveal.wav, success.wav
)

echo.
pause