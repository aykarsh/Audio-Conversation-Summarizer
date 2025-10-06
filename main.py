"""
Main entry point for Audio Conversation Summarizer & Topic Classifier
"""

import argparse
import sys
from pathlib import Path

# Add src to path for imports
sys.path.append(str(Path(__file__).parent / "src"))

from pipeline import AudioProcessingPipeline
from config.settings import load_config
from src.utils.logger import setup_logging, get_logger


def create_parser():
    """Create command line argument parser."""
    parser = argparse.ArgumentParser(
        description="Audio Conversation Summarizer & Topic Classifier",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py --audio data/input_audio/meeting.wav
  python main.py --record --duration 30
  python main.py --batch data/input_audio data/output
  python main.py --setup
        """
    )
    
    # Input options
    input_group = parser.add_mutually_exclusive_group()
    input_group.add_argument(
        "--audio", "-a",
        type=str,
        help="Path to audio file to process"
    )
    input_group.add_argument(
        "--record", "-r",
        action="store_true",
        help="Record audio from microphone"
    )
    input_group.add_argument(
        "--batch", "-b",
        nargs=2,
        metavar=("INPUT_DIR", "OUTPUT_DIR"),
        help="Batch process audio files in directory"
    )
    input_group.add_argument(
        "--setup", "-s",
        action="store_true",
        help="Run setup and model download"
    )
    
    # Configuration options
    parser.add_argument(
        "--duration", "-d",
        type=int,
        default=10,
        help="Recording duration in seconds (default: 10)"
    )
    
    parser.add_argument(
        "--output", "-o",
        type=str,
        help="Output file path"
    )
    
    parser.add_argument(
        "--model-size",
        type=str,
        default="base",
        choices=["tiny", "base", "small", "medium", "large"],
        help="Whisper model size (default: base)"
    )
    
    parser.add_argument(
        "--format",
        type=str,
        default="json",
        choices=["json", "text"],
        help="Output format (default: json)"
    )
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging"
    )
    
    return parser


def run_setup():
    """Run project setup."""
    try:
        import setup
        setup.main()
    except ImportError:
        print("❌ Setup script not found. Please ensure setup.py exists.")
        return False
    except Exception as e:
        print(f"❌ Setup failed: {e}")
        return False
    
    return True


def main():
    """
    Main function to orchestrate the audio processing pipeline
    """
    parser = create_parser()
    args = parser.parse_args()
    
    # Handle setup
    if args.setup:
        return run_setup()
    
    # Setup logging
    log_level = "DEBUG" if args.verbose else "INFO"
    setup_logging(level=log_level)
    logger = get_logger("main")
    
    # Load configuration
    config = load_config()
    
    # Update config with command line arguments
    if hasattr(config.models, 'whisper_model_size'):
        config.models.whisper_model_size = args.model_size
    
    logger.info("🎤 Starting Audio Conversation Summarizer")
    
    try:
        # Initialize pipeline
        pipeline = AudioProcessingPipeline(config)
        
        if args.audio:
            # Process single audio file
            logger.info(f"Processing audio file: {args.audio}")
            
            # Generate output path if not provided
            output_path = args.output
            if not output_path:
                input_file = Path(args.audio)
                output_dir = Path("data/output")
                output_dir.mkdir(exist_ok=True)
                
                if args.format == "json":
                    output_path = output_dir / f"{input_file.stem}_results.json"
                else:
                    output_path = output_dir / f"{input_file.stem}_results.txt"
            
            results = pipeline.process_audio_file(args.audio, str(output_path))
            
            # Display results
            print("\n" + "="*50)
            print("🎵 PROCESSING RESULTS")
            print("="*50)
            print(f"📁 File: {results['audio_file']}")
            print(f"⏱️  Time: {results['processing_time']:.2f}s")
            print(f"🏷️  Topic: {results['topic'].get('label', 'unknown')} "
                  f"({results['topic'].get('confidence', 0):.2f})")
            print(f"\n📝 Transcript:\n{results['transcript']}")
            print(f"\n📋 Summary:\n{results['summary']}")
            
        elif args.record:
            # Record from microphone
            logger.info(f"Recording from microphone for {args.duration} seconds")
            results = pipeline.process_microphone_input(args.duration)
            
            # Display results
            print("\n" + "="*50)
            print("🎙️  MICROPHONE RECORDING RESULTS")
            print("="*50)
            print(f"⏱️  Duration: {args.duration}s")
            print(f"🏷️  Topic: {results['topic']['label']} ({results['topic']['confidence']:.2f})")
            print(f"\n📝 Transcript:\n{results['transcript']}")
            print(f"\n📋 Summary:\n{results['summary']}")
            
        elif args.batch:
            # Batch process directory
            input_dir, output_dir = args.batch
            logger.info(f"Batch processing: {input_dir} -> {output_dir}")
            
            results = pipeline.batch_process(input_dir, output_dir)
            
            print("\n" + "="*50)
            print("📁 BATCH PROCESSING RESULTS")
            print("="*50)
            print(f"✅ Processed: {results['processed']} files")
            print(f"❌ Failed: {results['failed']} files") 
            print(f"⏱️  Total time: {results['total_duration']:.2f}s")
            
        else:
            # No input specified, show help
            parser.print_help()
            print("\n💡 Quick start:")
            print("  python main.py --setup              # Run setup first")
            print("  python main.py --audio sample.wav   # Process audio file")
            print("  python main.py --record --duration 15  # Record for 15 seconds")
            
    except KeyboardInterrupt:
        logger.info("❌ Operation cancelled by user")
        return 1
    except Exception as e:
        logger.error(f"❌ Error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1
    
    logger.info("✅ Operation completed successfully")
    return 0


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)