"""
File Utilities

Helper functions for file operations and validation.
"""

import os
from pathlib import Path
from typing import List


class FileUtils:
    """
    Utility class for file operations.
    """
    
    SUPPORTED_AUDIO_FORMATS = [".wav", ".mp3", ".m4a", ".flac", ".ogg"]
    
    @staticmethod
    def validate_audio_file(file_path: str) -> bool:
        """
        Validate if file exists and has supported audio format.
        
        Args:
            file_path (str): Path to audio file
            
        Returns:
            bool: True if file is valid
        """
        if not os.path.exists(file_path):
            return False
        
        file_ext = Path(file_path).suffix.lower()
        return file_ext in FileUtils.SUPPORTED_AUDIO_FORMATS
    
    @staticmethod
    def create_output_directory(base_dir: str) -> str:
        """
        Create output directory if it doesn't exist.
        
        Args:
            base_dir (str): Base directory path
            
        Returns:
            str: Created directory path
        """
        output_dir = Path(base_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        return str(output_dir)
    
    @staticmethod
    def get_file_size(file_path: str) -> int:
        """
        Get file size in bytes.
        
        Args:
            file_path (str): Path to file
            
        Returns:
            int: File size in bytes
        """
        return os.path.getsize(file_path)
    
    @staticmethod
    def list_audio_files(directory: str) -> List[str]:
        """
        List all audio files in directory.
        
        Args:
            directory (str): Directory path
            
        Returns:
            List[str]: List of audio file paths
        """
        audio_files = []
        for ext in FileUtils.SUPPORTED_AUDIO_FORMATS:
            audio_files.extend(Path(directory).glob(f"*{ext}"))
        
        return [str(f) for f in audio_files]