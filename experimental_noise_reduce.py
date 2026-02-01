"""
EXPERIMENTAL / ARCHIVE CODE
This file contains an alternative implementation of noise reduction using NSNet2 and ONNX Runtime.
It is currently preserved for reference.
"""

'''import os
import torch
import torchaudio
import librosa
import noisereduce as nr
import soundfile as sf
import numpy as np
import pydub
from pydub import AudioSegment
from pydub.playback import play
from tkinter import Tk, filedialog
import onnxruntime as ort


def select_audio_file():
    """Open a file dialog to select an audio file."""
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    root.destroy()
    return file_path


def convert_to_wav(input_path):
    """Convert MP3 or M4A file to WAV format with high-quality settings."""
    wav_path = input_path.rsplit(".", 1)[0] + ".wav"

    if input_path.endswith(".mp3") or input_path.endswith(".m4a"):
        audio = AudioSegment.from_file(input_path)
        audio = audio.set_frame_rate(44100).set_channels(1)  # Ensure standard format
        audio.export(wav_path, format="wav")
    else:
        return input_path  # No conversion needed

    return wav_path


def apply_nsnet2(y, sr):
    """Apply AI-based noise suppression using NSNet2."""
    model_path = "https://github.com/microsoft/NSNet2/raw/main/nsnet2.onnx"
    session = ort.InferenceSession(model_path)

    # Reshape input to match NSNet2 model requirements
    y = y.astype(np.float32).reshape(1, 1, -1)
    enhanced_audio = session.run(None, {session.get_inputs()[0].name: y})[0]

    return enhanced_audio.flatten()


def reduce_noise(input_path, output_path):
    """Perform AI-based noise reduction and speech enhancement using NSNet2."""
    input_path = convert_to_wav(input_path)  # Convert if necessary

    # Load audio file with high precision
    y, sr = librosa.load(input_path, sr=44100, mono=True, dtype='float32')

    # Apply AI-based noise reduction
    enhanced_audio = apply_nsnet2(y, sr)

    # Save cleaned and enhanced audio in high quality
    sf.write(output_path, enhanced_audio, sr, format='WAV', subtype='PCM_16')


def play_audio(file_path):
    """Play an audio file."""
    audio = AudioSegment.from_wav(file_path)
    play(audio)


def main():
    print("Select an audio file to clean and enhance with AI...")
    input_file = select_audio_file()
    if not input_file:
        print("No file selected. Exiting.")
        return

    output_file = input_file.rsplit(".", 1)[0] + "_AI_enhanced.wav"

    print("Reducing noise and enhancing speech clarity using AI...")
    reduce_noise(input_file, output_file)
    print(f"Enhanced audio saved to: {output_file}")

    # Play enhanced audio
    play_audio(output_file)


if __name__ == "__main__":
    main()'''
'''