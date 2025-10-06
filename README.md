# Audio Conversation Summarizer & Topic Classifier

A comprehensive audio processing system that converts spoken audio into text, generates summaries, and classifies conversation topics using state-of-the-art NLP models.

## Features

- **Speech-to-Text**: Convert audio files or live microphone input to text using OpenAI Whisper
- **Text Summarization**: Generate concise summaries using BART/T5 models
- **Topic Classification**: Classify conversations into predefined categories using BART-MNLI
- **Interactive UI**: Web interface built with Streamlit
- **Real-time Processing**: Support for live microphone input

## Project Structure

```
Audio-Conversation-Summarizer/
├── src/
│   ├── audio_processing/     # Audio input and speech-to-text
│   ├── text_processing/      # Summarization and classification
│   ├── models/              # Model loading and management
│   ├── ui/                  # User interface components
│   └── utils/               # Helper functions and utilities
├── data/
│   ├── input_audio/         # Sample audio files
│   └── output/              # Generated results
├── config/                  # Configuration files
├── tests/                   # Unit tests
├── docs/                    # Documentation
└── main.py                  # Main entry point
```

## Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python main.py`

## Usage

### Command Line Interface
```bash
python main.py --audio input.wav
```

### Web Interface
```bash
streamlit run src/ui/streamlit_app.py
```

## Target Users

- Journalists & Researchers (quick audio summaries)
- Professionals (meeting minutes)
- Students (lecture summaries)
- General users (conversation recap)

## Technologies

- **Python 3.9+**
- **OpenAI Whisper** for speech-to-text
- **Transformers** for NLP models
- **Streamlit** for web interface
- **PyTorch** for model inference