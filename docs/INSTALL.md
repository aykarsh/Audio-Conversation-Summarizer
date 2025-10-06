# Installation Guide

## Prerequisites

- Python 3.9 or higher
- FFmpeg (for audio processing)
- Git

## System Requirements

### Windows
- Windows 10 or higher
- Visual Studio Build Tools (for some packages)

### macOS
- macOS 10.15 or higher
- Xcode Command Line Tools

### Linux
- Ubuntu 18.04+ / CentOS 7+ / Similar distributions
- Build essentials package

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Audio-Conversation-Summarizer.git
cd Audio-Conversation-Summarizer
```

### 2. Create Virtual Environment

```bash
# Using venv
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### 3. Install FFmpeg

#### Windows
Download from [FFmpeg website](https://ffmpeg.org/download.html) or use:
```bash
# Using chocolatey
choco install ffmpeg

# Using scoop
scoop install ffmpeg
```

#### macOS
```bash
# Using Homebrew
brew install ffmpeg
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install ffmpeg
```

### 4. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 5. Environment Configuration

Copy the example environment file and configure:
```bash
cp .env.example .env
```

Edit `.env` file with your preferred settings.

### 6. Verify Installation

```bash
python main.py --help
```

## Optional: GPU Support

For faster processing with NVIDIA GPU:

### Install PyTorch with CUDA
```bash
# CUDA 11.8
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu118

# CUDA 12.1
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu121
```

### Verify GPU Support
```python
import torch
print(torch.cuda.is_available())
print(torch.cuda.device_count())
```

## Troubleshooting

### Common Issues

1. **FFmpeg not found**: Ensure FFmpeg is in your system PATH
2. **PyAudio installation fails**: Install system audio libraries first
3. **CUDA out of memory**: Use smaller model sizes or CPU processing
4. **Import errors**: Verify all dependencies are installed correctly

### Audio Library Issues (Windows)

If PyAudio installation fails:
```bash
pip install pipwin
pipwin install pyaudio
```

Or download pre-compiled wheels from [Christoph Gohlke's site](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio).

### Model Download Issues

Models are downloaded automatically on first use. Ensure you have:
- Stable internet connection
- Sufficient disk space (models can be 1-3GB each)
- No firewall blocking Hugging Face Hub

## Development Setup

For development, install additional dependencies:
```bash
pip install -r requirements-dev.txt
```

Set up pre-commit hooks:
```bash
pre-commit install
```

Run tests:
```bash
pytest tests/
```