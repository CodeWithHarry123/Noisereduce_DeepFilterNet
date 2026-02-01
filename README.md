# Noise Reduce & Video Tools

This project provides tools for audio noise reduction using Deep AI models (DeepFilterNet) and video manipulation (speed up).

## Features

1.  **Audio Noise Reduction**: Uses `DeepFilterNet` to clean noisy audio files (WAV, MP3, etc.).
2.  **Video Speedup**: Uses `ffmpeg` to increase playback speed of video files while maintaining pitch.
3.  **Experimental NSNet2**: Includes experimental code for noise reduction using Microsoft's NSNet2 (onnx).

## Prerequisites

-   **Python 3.8+**
-   **FFmpeg** installed on your system (required for video tools and audio conversion).
    -   MacOS: `brew install ffmpeg`
    -   Ubuntu: `sudo apt install ffmpeg`
    -   Windows: Download and add to PATH.

## Installation

1.  Clone the repository (if not already).
2.  Install Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    *Note: The project relies on a local copy of `DeepFilterNet`. Ensure the `DeepFilterNet` folder is present in the root directory.*

## Usage

### 1. Audio Noise Reduction

Run the main script to select an audio file via a dialog box and apply noise reduction.

```bash
python main.py
```

-   Select your file (WAV, MP3, M4A).
-   The script will generate a new file ending in `_AI_enhanced.wav`.
-   It will attempt to play the enhanced audio automatically.

### 2. Video Speed Up

Use the `video_speedup_converter.py` script to speed up videos.

```bash
python video_speedup_converter.py input.mkv output.mkv --speed 1.5
```

-   `input.mkv`: Path to source video.
-   `output.mkv`: Path to save the result.
-   `--speed`: Speed multiplier (default 1.5).

### 3. Experimental

`experimental_noise_reduce.py` contains alternative noise reduction logic using `noisereduce` and `ONNX`. It is currently provided as a reference/snippet.

## Structure

-   `main.py`: Main entry point for audio enhancement.
-   `video_speedup_converter.py`: Video processing utility.
-   `DeepFilterNet/`: Contains the DeepFilterNet library code and models.
-   `assets/` / `models/`: (If present) Storage for model weights.

## License

This project uses `DeepFilterNet`. Please check `DeepFilterNet/LICENSE` for licensing details regarding the AI model and code.