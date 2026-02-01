import sys
import os
import torch
import torchaudio
import soundfile as sf
import numpy as np
from tkinter import Tk, filedialog
from pydub import AudioSegment
from pydub.playback import play

# Add the local DeepFilterNet library to path
# Assuming the structure is ./DeepFilterNet/DeepFilterNet
# This allows 'import df' to work as expected by the library's internal modules
sys.path.append(os.path.join(os.getcwd(), 'DeepFilterNet', 'DeepFilterNet'))

try:
    from df.enhance import enhance, init_df, load_audio, save_audio
    from df.utils import get_device
except ImportError as e:
    print(f"Error importing DeepFilterNet: {e}")
    print("Ensure the DeepFilterNet submodule is present in 'DeepFilterNet/DeepFilterNet'")
    sys.exit(1)


def select_audio_file():
    """Open a file dialog to select an audio file (MacOS-safe)."""
    try:
        root = Tk()
        root.withdraw()  # Hide the main Tkinter window
        root.update()  # Ensure Tkinter is fully loaded

        file_path = filedialog.askopenfilename(
            title="Select an audio file",
            filetypes=[("Audio Files", "*.wav *.mp3 *.m4a *.flac"), ("All Files", "*.*")]
        )

        root.destroy()  # Properly close Tkinter
        return file_path if file_path else None
    except Exception as e:
        print(f"Error opening file dialog: {e}")
        return None


def convert_to_wav(input_path):
    """Convert MP3 or M4A file to WAV format if necessary."""
    wav_path = input_path.rsplit(".", 1)[0] + ".wav"

    if input_path.lower().endswith((".mp3", ".m4a")):
        print(f"Converting {input_path} to WAV...")
        audio = AudioSegment.from_file(input_path)
        audio = audio.set_frame_rate(48000).set_channels(1) # DeepFilterNet prefers 48k
        audio.export(wav_path, format="wav")
        return wav_path
    
    return input_path


def apply_deepfilternet(input_path, output_path):
    """Apply AI-based noise suppression using DeepFilterNet."""
    print("Loading DeepFilterNet model...")
    
    # Load default model (DeepFilterNet3 usually)
    # This automatically handles downloading if not present in cache
    model, df_state, _ = init_df()

    print(f"Processing {input_path}...")
    
    # Load audio using DF's utility which handles resampling to model's SR
    audio, _ = load_audio(input_path, sr=df_state.sr())

    # Denoise
    enhanced_audio = enhance(model, df_state, audio)

    # Save
    save_audio(output_path, enhanced_audio, df_state.sr())


def play_audio(file_path):
    """Play an audio file."""
    try:
        audio = AudioSegment.from_wav(file_path)
        play(audio)
    except Exception as e:
        print(f"Could not play audio: {e}")


def main():
    print("Select an audio file to clean and enhance with AI...")
    input_file = select_audio_file()
    if not input_file:
        print("No file selected. Exiting.")
        return

    # Convert to wav if needed (though DF's load_audio handles many formats, 
    # it's good to ensure we have a compatible path)
    wav_file = convert_to_wav(input_file)
    
    output_file = input_file.rsplit(".", 1)[0] + "_AI_enhanced.wav"

    print("Reducing noise and enhancing speech clarity using AI...")
    try:
        apply_deepfilternet(wav_file, output_file)
        print(f"✅ Enhanced audio saved to: {output_file}")
        
        # Play enhanced audio
        play_audio(output_file)
    except Exception as e:
        print(f"An error occurred during processing: {e}")


if __name__ == "__main__":
    main()

