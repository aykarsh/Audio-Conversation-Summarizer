# API Documentation

## Audio Processing API

### AudioInputHandler

**Class**: `src.audio_processing.audio_input.AudioInputHandler`

Methods:
- `load_audio_file(file_path: str)` - Load audio from file
- `record_from_microphone(duration: int = 10)` - Record from microphone
- `validate_audio_format(file_path: str) -> bool` - Validate audio format

### SpeechToText

**Class**: `src.audio_processing.speech_to_text.SpeechToText`

Methods:
- `load_model()` - Load Whisper model
- `transcribe_audio(audio_data, language: str = None)` - Transcribe audio data
- `transcribe_file(file_path: str, language: str = None)` - Transcribe audio file

## Text Processing API

### TextSummarizer

**Class**: `src.text_processing.summarizer.TextSummarizer`

Methods:
- `load_model()` - Load summarization model
- `summarize_text(text: str, max_length: int = 150, min_length: int = 50)` - Generate summary
- `preprocess_text(text: str) -> str` - Preprocess text

### TopicClassifier

**Class**: `src.text_processing.topic_classifier.TopicClassifier`

Methods:
- `load_model()` - Load classification model
- `classify_topic(text: str, custom_topics: list = None)` - Classify topic
- `set_custom_topics(topics: list)` - Set custom topics
- `get_top_predictions(text: str, top_k: int = 3)` - Get top predictions

## Configuration

### AppConfig

**Class**: `config.settings.AppConfig`

Configuration sections:
- `audio: AudioConfig` - Audio processing settings
- `models: ModelConfig` - Model configuration
- `processing: ProcessingConfig` - Text processing settings
- `ui: UIConfig` - User interface settings

## Usage Examples

### Basic Usage

```python
from src.audio_processing.speech_to_text import SpeechToText
from src.text_processing.summarizer import TextSummarizer
from src.text_processing.topic_classifier import TopicClassifier

# Initialize components
stt = SpeechToText(model_size="base")
summarizer = TextSummarizer()
classifier = TopicClassifier()

# Load models
stt.load_model()
summarizer.load_model()
classifier.load_model()

# Process audio
transcript = stt.transcribe_file("audio.wav")
summary = summarizer.summarize_text(transcript)
topic = classifier.classify_topic(transcript)

print(f"Transcript: {transcript}")
print(f"Summary: {summary}")
print(f"Topic: {topic}")
```

### Streamlit Interface

```bash
streamlit run src/ui/streamlit_app.py
```

### Command Line Interface

```bash
python src/ui/cli.py --audio input.wav --model-size base --output results.json
```