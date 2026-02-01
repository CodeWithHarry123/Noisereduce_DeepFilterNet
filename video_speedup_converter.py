import ffmpeg as ff
import argparse
import sys
import os

def convert_and_speedup_mkv(input_file, output_file, speed=1.5):
    """
    Speeds up a video and its audio by the given factor using ffmpeg.
    
    Args:
        input_file (str): Path to the input video file.
        output_file (str): Path where the output video will be saved.
        speed (float): Speedup factor (e.g., 1.5 for 1.5x speed).
    """
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        return

    try:
        print(f"Starting conversion and speed-up: {input_file} -> {output_file} (Speed: {speed}x)")

        # Create input stream
        inp = ff.input(input_file)

        # Video filter: set presentation timestamps (PTS) to speed up video
        # PTS/speed makes the timestamps smaller, making the video play faster
        video = inp.video.filter('setpts', f'PTS/{speed}')

        # Audio filter: atempo filter (1.5 is within allowed range: 0.5 to 2.0)
        # For speeds outside 0.5-2.0, multiple atempo filters might be needed, 
        # but for typical usage this is fine.
        audio = inp.audio.filter('atempo', speed)

        # Combine video and audio into output file
        stream = ff.output(video, audio, output_file,
                           vcodec='libx264', acodec='aac',
                           format='matroska', strict='experimental')
        
        # Run ffmpeg
        ff.run(stream, overwrite_output=True)
        print("Conversion successful:", output_file)

    except ff.Error as e:
        print("FFmpeg error:", e.stderr.decode('utf8') if e.stderr else str(e))
    except Exception as e:
        print("Error during conversion:", e)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Speed up a video file (MKV/MP4/etc) using FFmpeg.")
    parser.add_argument("input_file", help="Path to the input video file")
    parser.add_argument("output_file", help="Path to the output video file")
    parser.add_argument("--speed", type=float, default=1.5, help="Speedup factor (default: 1.5)")

    args = parser.parse_args()

    convert_and_speedup_mkv(args.input_file, args.output_file, args.speed)