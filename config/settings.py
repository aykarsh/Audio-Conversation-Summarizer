"""
Configuration Settings

Application configuration and settings management.
"""

import os
from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class AudioConfig:
    """Audio processing configuration."""
    sample_rate: int = 16000
    chunk_size: int = 1024
    max_file_size_mb: int = 100
    supported_formats: List[str] = None
    
    def __post_init__(self):
        if self.supported_formats is None:
            self.supported_formats = [".wav", ".mp3", ".m4a", ".flac", ".ogg"]


@dataclass
class ModelConfig:
    """Model configuration."""
    whisper_model_size: str = "base"
    summarizer_model: str = "facebook/bart-large-cnn"
    classifier_model: str = "facebook/bart-large-mnli"
    device: str = "auto"  # auto, cpu, cuda
    cache_dir: str = "./models_cache"


@dataclass
class ProcessingConfig:
    """Text processing configuration."""
    max_summary_length: int = 150
    min_summary_length: int = 50
    topic_confidence_threshold: float = 0.5
    predefined_topics: List[str] = None
    
    def __post_init__(self):
        if self.predefined_topics is None:
            self.predefined_topics = [
                "technology", "sports", "health", "politics", "business",
                "entertainment", "education", "casual conversation", "news", "science"
            ]


@dataclass
class UIConfig:
    """User interface configuration."""
    streamlit_port: int = 8501
    theme: str = "light"
    max_upload_size_mb: int = 50


@dataclass
class AppConfig:
    """Main application configuration."""
    audio: AudioConfig = None
    models: ModelConfig = None
    processing: ProcessingConfig = None
    ui: UIConfig = None
    debug: bool = False
    log_level: str = "INFO"
    
    def __post_init__(self):
        if self.audio is None:
            self.audio = AudioConfig()
        if self.models is None:
            self.models = ModelConfig()
        if self.processing is None:
            self.processing = ProcessingConfig()
        if self.ui is None:
            self.ui = UIConfig()


def load_config() -> AppConfig:
    """
    Load configuration from environment variables or defaults.
    
    Returns:
        AppConfig: Application configuration
    """
    return AppConfig(
        debug=os.getenv("DEBUG", "false").lower() == "true",
        log_level=os.getenv("LOG_LEVEL", "INFO")
    )