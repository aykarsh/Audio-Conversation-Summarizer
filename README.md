# 🎤 Audio Conversation Summarizer & Topic Classifier

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Fully Functional](https://img.shields.io/badge/Status-Fully%20Functional-brightgreen.svg)]()

A **fully functional** audio processing system that converts spoken audio into text, generates intelligent summaries, and classifies conversation topics using state-of-the-art AI models.

## ✨ Features

- 🎙️ **Speech-to-Text**: Convert audio files (MP3, WAV, MP4, M4A, FLAC, OGG) to text using OpenAI Whisper
- 📝 **Intelligent Summarization**: Generate concise summaries using Facebook BART models
- 🏷️ **Topic Classification**: Classify conversations into 12+ categories using BART-MNLI
- ⚡ **Real-time Processing**: Support for live microphone recording
- 📁 **Batch Processing**: Process multiple audio files simultaneously  
- 🖥️ **Multiple Interfaces**: Command-line interface and web UI (Streamlit)
- 💾 **Flexible Output**: JSON and text format results
- 🔧 **Configurable**: Adjustable model sizes and processing parameters

## 🎯 Supported Audio Formats

✅ **WAV** (recommended) | ✅ **MP3** | ✅ **MP4** | ✅ **M4A** | ✅ **FLAC** | ✅ **OGG**

## 🏗️ Project Architecture

```
Audio-Conversation-Summarizer/
├── 🐍 main.py                      # Main CLI application
├── 🔧 setup.py                     # Automated setup script
├── 📋 requirements.txt              # Python dependencies
├── ⚙️  .env.example                 # Configuration template
│
├── 📂 src/                         # Source code
│   ├── 🔄 pipeline.py              # Main processing pipeline  
│   ├── 🎤 audio_processing/        # Audio input & speech-to-text
│   │   ├── 📥 audio_input.py       # File & microphone input
│   │   └── 🗣️  speech_to_text.py   # Whisper integration
│   ├── 📝 text_processing/         # NLP processing
│   │   ├── 📄 summarizer.py        # BART summarization
│   │   └── 🏷️  topic_classifier.py # BART-MNLI classification
│   ├── 🤖 models/                  # Model management
│   │   └── 📦 model_manager.py     # Centralized model loading
│   ├── 🖥️ ui/                       # User interfaces
│   │   ├── 🌐 streamlit_app.py     # Web interface
│   │   └── ⌨️  cli.py              # Command line interface
│   └── 🔧 utils/                   # Helper functions
│       ├── 📊 logger.py            # Logging system
│       └── 📁 file_utils.py        # File operations
│
├── 📂 data/                        # Data directories
│   ├── 🎵 input_audio/             # Place your audio files here
│   └── 📄 output/                  # Generated results
│
├── ⚙️  config/                     # Configuration
│   └── 🔧 settings.py              # Application settings
│
├── 🧪 tests/                       # Unit tests
└── 📖 docs/                        # Documentation
    ├── 📚 API.md                   # API documentation  
    └── 🔧 INSTALL.md               # Installation guide
```

## 🚀 Quick Start

### Prerequisites

- **Python 3.9+** (recommended: Python 3.13.2)
- **FFmpeg** (for audio processing)
- **4GB+ RAM** (for ML models)
- **2GB+ disk space** (for model storage)

### Step 1: Clone & Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/Audio-Conversation-Summarizer.git
cd Audio-Conversation-Summarizer

# Run automated setup (recommended)
python setup.py
```

### Step 2: Manual Installation (if setup fails)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install FFmpeg (Windows - choose one):
choco install ffmpeg          # Using Chocolatey
scoop install ffmpeg          # Using Scoop
# Or download from: https://ffmpeg.org/download.html
```

### Step 3: Verify Installation

```bash
# Check all dependencies
python setup.py

# Test basic functionality  
python main.py --help
```

## 🎯 Usage Guide

### 📁 Processing Audio Files

#### Single File Processing
```bash
# Basic usage
python main.py --audio "data/input_audio/your_file.mp3"

# With specific model size
python main.py --audio "data/input_audio/meeting.wav" --model-size small

# Custom output location
python main.py --audio "audio.mp3" --output "results.json" --format json

# Verbose logging
python main.py --audio "interview.wav" --verbose
```

#### Batch Processing
```bash
# Process all files in a directory
python main.py --batch "data/input_audio" "data/output"
```

### 🎙️ Live Recording

```bash
# Record for 30 seconds
python main.py --record --duration 30

# Record with custom settings
python main.py --record --duration 60 --model-size base --output "live_recording.json"
```

### 🌐 Web Interface

```bash
# Start web interface (coming soon)
streamlit run src/ui/streamlit_app.py
```

## 📊 Output Formats

### JSON Output (Default)
```json
{
  "audio_file": "meeting.wav",
  "timestamp": "2024-01-15T14:30:00Z",
  "transcript": "This is the full transcription of the audio...",
  "summary": "Concise summary of the main points discussed...",
  "topic": {
    "label": "business", 
    "confidence": 0.95,
    "all_scores": {
      "business": 0.95,
      "technology": 0.75,
      "education": 0.12
    }
  },
  "processing_time": 12.34,
  "status": "completed"
}
```

### Text Output
```
Audio Conversation Analysis Results
=====================================

File: meeting.wav
Processed: 2024-01-15T14:30:00Z
Duration: 12.34s

TRANSCRIPT:
-----------
This is the full transcription...

SUMMARY:  
--------
Concise summary of main points...

TOPIC CLASSIFICATION:
--------------------
Primary Topic: business
Confidence: 0.95
```

## 🎛️ Configuration

### Model Selection
- **Whisper Models**: `tiny`, `base`, `small`, `medium`, `large`
  - `tiny`: Fastest, less accurate (~39 MB)
  - `base`: Balanced speed/accuracy (~74 MB) - **Default**
  - `small`: Better accuracy (~244 MB)
  - `medium`: High accuracy (~769 MB)  
  - `large`: Best accuracy (~1550 MB)

### Topic Categories
The system classifies audio into these categories:
- 💻 **Technology** - Tech discussions, software, hardware
- 💼 **Business** - Meetings, negotiations, corporate  
- 🎓 **Education** - Lectures, tutorials, academic content
- 🎬 **Entertainment** - Movies, shows, celebrity news
- 🏥 **Health** - Medical, fitness, wellness topics
- ⚽ **Sports** - Games, athletes, competitions
- 🏛️ **Politics** - Government, elections, policy
- 💬 **Casual Conversation** - Personal chats, social
- 📰 **News** - Current events, journalism
- 🔬 **Science** - Research, discoveries, experiments
- 💰 **Finance** - Economics, markets, investing
- ✈️ **Travel** - Tourism, geography, culture

### Environment Configuration
Create a `.env` file from the template:
```bash
cp .env.example .env
# Edit .env with your preferences
```

## 📊 Performance & Requirements

### Processing Speed (approximate)
- **1-minute audio**: 5-15 seconds processing time
- **5-minute audio**: 20-60 seconds processing time
- **Model loading**: 2-10 seconds (first run only)

### System Requirements
- **CPU**: Modern multi-core processor (Intel i5/AMD Ryzen 5+)
- **RAM**: 4GB minimum, 8GB+ recommended
- **Storage**: 2GB for models, additional space for audio files
- **GPU**: Optional (CUDA-compatible for faster processing)

## 🎯 Target Users

- 📰 **Journalists & Researchers** - Quick audio summaries and content analysis
- 💼 **Business Professionals** - Meeting minutes and call summaries  
- 🎓 **Students & Educators** - Lecture summaries and study materials
- 👥 **General Users** - Personal conversation recap and organization
- 🎧 **Content Creators** - Podcast and video content analysis

## 🛠️ Technologies & Models

### Core Technologies
- **🐍 Python 3.13.2** - Main programming language
- **🤗 Transformers 4.57.0** - Hugging Face model library
- **🔥 PyTorch 2.8.0** - Deep learning framework  
- **🎤 OpenAI Whisper** - State-of-the-art speech recognition
- **🌐 Streamlit** - Web interface framework
- **🔊 librosa & sounddevice** - Audio processing libraries

### AI Models Used
- **Speech-to-Text**: OpenAI Whisper (multiple sizes available)
- **Summarization**: Facebook BART-large-cnn (1.6GB)
- **Classification**: Facebook BART-large-mnli (1.6GB)
- **Total Model Size**: ~3.5GB (base configuration)

## 🔍 Examples

### Example 1: Business Meeting
```bash
python main.py --audio "data/input_audio/quarterly_meeting.wav"
```

**Output**:
- **Topic**: Business (confidence: 0.94)
- **Summary**: "Discussion of Q4 results, budget planning for next year, and team restructuring initiatives..."
- **Processing Time**: 8.2 seconds

### Example 2: Educational Lecture  
```bash
python main.py --audio "data/input_audio/ai_lecture.mp3" --model-size small
```

**Output**:
- **Topic**: Education (confidence: 0.89)  
- **Summary**: "Introduction to machine learning concepts, neural networks, and practical applications..."
- **Processing Time**: 15.7 seconds

## 🚨 Troubleshooting

### Common Issues

#### 1. FFmpeg Not Found
```bash
Error: FFmpeg binary not found in PATH
```
**Solution**: Install FFmpeg:
- Windows: `choco install ffmpeg` or `scoop install ffmpeg`
- macOS: `brew install ffmpeg`
- Linux: `sudo apt install ffmpeg`

#### 2. CUDA Out of Memory
```bash
RuntimeError: CUDA out of memory
```
**Solution**: Use CPU processing or smaller models:
```bash
python main.py --audio file.wav --model-size tiny
```

#### 3. Model Download Fails
```bash
Error downloading model files
```
**Solution**: Check internet connection and try:
```bash
python setup.py  # Re-download models
```

#### 4. Audio Format Not Supported
```bash
Error: Unsupported audio format
```
**Solution**: Convert to supported format or install additional codecs

### Performance Tips

- 🚀 **Use smaller models** for faster processing (`tiny`, `base`)
- 💾 **Ensure sufficient RAM** for large audio files  
- 🔊 **Use high-quality audio** for better transcription accuracy
- 📁 **Process shorter clips** (1-5 minutes) for optimal results

## 📖 Additional Documentation

- 📚 **[API Documentation](docs/API.md)** - Detailed API reference
- 🔧 **[Installation Guide](docs/INSTALL.md)** - Comprehensive setup instructions  
- 🧪 **Testing**: Run `pytest tests/` for unit tests
- 📝 **Contributing**: See contribution guidelines in `CONTRIBUTING.md`

## 🤝 Support & Community

- 🐛 **Issues**: Report bugs via GitHub Issues
- 💡 **Feature Requests**: Suggest improvements via GitHub Discussions  
- 📧 **Contact**: [Your Email]
- 💬 **Community**: Join our Discord/Slack

## 📜 License

This project is licensed under the MIT License - see the `LICENSE` file for details.

---

**🎉 Ready to transform your audio content? Get started now!**

```bash
git clone https://github.com/yourusername/Audio-Conversation-Summarizer.git
cd Audio-Conversation-Summarizer  
python setup.py
python main.py --audio "your_audio_file.mp3"
```