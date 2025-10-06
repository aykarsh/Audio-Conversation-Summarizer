"""
Command Line Interface

Console interface for the Audio Conversation Summarizer.
"""

import argparse


class CLI:
    """
    Command line interface for the audio processing pipeline.
    """
    
    def __init__(self):
        """Initialize the CLI."""
        self.parser = self._create_parser()
    
    def _create_parser(self):
        """
        Create argument parser for CLI.
        
        Returns:
            ArgumentParser: Configured argument parser
        """
        parser = argparse.ArgumentParser(
            description="Audio Conversation Summarizer & Topic Classifier"
        )
        
        parser.add_argument(
            "--audio", 
            type=str, 
            help="Path to audio file"
        )
        
        parser.add_argument(
            "--record", 
            action="store_true", 
            help="Record audio from microphone"
        )
        
        parser.add_argument(
            "--duration", 
            type=int, 
            default=10, 
            help="Recording duration in seconds"
        )
        
        parser.add_argument(
            "--model-size", 
            type=str, 
            default="base", 
            choices=["tiny", "base", "small", "medium", "large"],
            help="Whisper model size"
        )
        
        parser.add_argument(
            "--output", 
            type=str, 
            help="Output file path for results"
        )
        
        return parser
    
    def run(self):
        """
        Run the CLI application.
        """
        args = self.parser.parse_args()
        
        # Process arguments and run pipeline
        pass


def main():
    """Main CLI entry point."""
    cli = CLI()
    cli.run()


if __name__ == "__main__":
    main()