"""
Test Configuration and Fixtures

Common test utilities and fixtures for the test suite.
"""

import pytest
from pathlib import Path


@pytest.fixture
def sample_audio_file():
    """
    Fixture for sample audio file path.
    """
    return "data/input_audio/sample.wav"


@pytest.fixture
def sample_text():
    """
    Fixture for sample text content.
    """
    return """
    This is a sample conversation about artificial intelligence and machine learning.
    The discussion covers various aspects of AI technology, including natural language
    processing, computer vision, and deep learning algorithms. The participants
    share their thoughts on the future of AI and its impact on society.
    """


@pytest.fixture
def config():
    """
    Fixture for test configuration.
    """
    from config.settings import AppConfig
    return AppConfig(debug=True)