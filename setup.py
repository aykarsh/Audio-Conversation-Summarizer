"""
Setup Script for Audio Conversation Summarizer

This script helps initialize the project and download required models.
"""

import os
import sys
from pathlib import Path


def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 9):
        print("❌ Error: Python 3.9 or higher is required.")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version}")
    return True


def check_dependencies():
    """Check if required dependencies are installed."""
    required_packages = [
        "torch", "transformers", "whisper", "streamlit", 
        "numpy", "librosa", "sounddevice"
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} is installed")
        except ImportError:
            missing_packages.append(package)
            print(f"❌ {package} is missing")
    
    if missing_packages:
        print(f"\n🔧 Install missing packages with:")
        print(f"pip install {' '.join(missing_packages)}")
        return False
    
    return True


def check_ffmpeg():
    """Check if FFmpeg is available."""
    try:
        import subprocess
        result = subprocess.run(
            ["ffmpeg", "-version"], 
            capture_output=True, 
            text=True
        )
        if result.returncode == 0:
            print("✅ FFmpeg is installed")
            return True
    except FileNotFoundError:
        pass
    
    print("❌ FFmpeg is not installed or not in PATH")
    print("📋 Install FFmpeg:")
    print("   Windows: choco install ffmpeg or download from https://ffmpeg.org")
    print("   macOS: brew install ffmpeg") 
    print("   Linux: sudo apt install ffmpeg")
    return False


def create_directories():
    """Create necessary directories."""
    directories = [
        "data/input_audio",
        "data/output", 
        "models_cache",
        "logs"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"📁 Created directory: {directory}")


def download_sample_models():
    """Download and cache sample models."""
    print("\n🔄 Downloading sample models...")
    
    try:
        # Test Whisper model download
        import whisper
        print("📥 Downloading Whisper base model...")
        model = whisper.load_model("base")
        print("✅ Whisper model cached successfully")
        
        # Test transformers model download
        from transformers import pipeline
        print("📥 Downloading summarization model...")
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        print("✅ Summarization model cached successfully")
        
        print("📥 Downloading classification model...")
        classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
        print("✅ Classification model cached successfully")
        
    except Exception as e:
        print(f"⚠️  Warning: Could not download models: {e}")
        print("Models will be downloaded on first use.")


def create_env_file():
    """Create .env file if it doesn't exist."""
    env_file = Path(".env")
    if not env_file.exists():
        env_example = Path(".env.example")
        if env_example.exists():
            import shutil
            shutil.copy(env_example, env_file)
            print("📄 Created .env file from .env.example")
        else:
            with open(".env", "w") as f:
                f.write("# Audio Conversation Summarizer Configuration\n")
                f.write("DEBUG=false\n")
                f.write("LOG_LEVEL=INFO\n")
                f.write("WHISPER_MODEL_SIZE=base\n")
            print("📄 Created basic .env file")
    else:
        print("✅ .env file already exists")


def main():
    """Main setup function."""
    print("🎤 Audio Conversation Summarizer Setup")
    print("=" * 50)
    
    success = True
    
    # Check requirements
    if not check_python_version():
        success = False
    
    if not check_dependencies():
        success = False
    
    if not check_ffmpeg():
        success = False
    
    if not success:
        print("\n❌ Setup incomplete. Please resolve the issues above.")
        return
    
    # Create project structure
    print("\n📁 Setting up project structure...")
    create_directories()
    create_env_file()
    
    # Download models (optional)
    print("\n🤖 Would you like to download models now? (y/n): ", end="")
    response = input().lower().strip()
    
    if response in ['y', 'yes']:
        download_sample_models()
    else:
        print("⏭️  Skipping model download. Models will be downloaded on first use.")
    
    print("\n✅ Setup completed successfully!")
    print("\n🚀 Next steps:")
    print("1. Run: python main.py --help")
    print("2. Or start web interface: streamlit run src/ui/streamlit_app.py")
    print("3. Place audio files in: data/input_audio/")


if __name__ == "__main__":
    main()