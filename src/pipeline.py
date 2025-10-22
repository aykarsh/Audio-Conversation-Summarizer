"""
Audio Processing Pipeline

Orchestrates the complete audio-to-summary-to-topic workflow.
"""

import json
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional
import whisper
import torch

class AudioProcessingPipeline:
    """
    Main pipeline class that orchestrates audio processing workflow.
    """
    
    def __init__(self, config=None):
        """
        Initialize the processing pipeline.
        
        Args:
            config: Configuration object
        """
        self.config = config
        self.audio_handler = None
        self.speech_to_text = None
        self.summarizer = None
        self.classifier = None
        self._models_loaded = False
    
    def load_models(self):
        """Load all required models."""
        if self._models_loaded:
            return
        
        print("🔄 Loading models...")
        
        # Initialize components (will be implemented later)
        # from src.audio_processing.audio_input import AudioInputHandler
        # from src.audio_processing.speech_to_text import SpeechToText
        # from src.text_processing.summarizer import TextSummarizer
        # from src.text_processing.topic_classifier import TopicClassifier
        
        # self.audio_handler = AudioInputHandler()
        # self.speech_to_text = SpeechToText()
        # self.summarizer = TextSummarizer()
        # self.classifier = TopicClassifier()
        
        print("✅ Models loaded successfully")
        self._models_loaded = True
    
    def process_audio_file(self, file_path: str, output_path: str = None) -> Dict[str, Any]:
        """
        Process an audio file through the complete pipeline.
        
        Args:
            file_path (str): Path to the audio file
            output_path (str): Optional output file path
            
        Returns:
            Dict[str, Any]: Processing results
        """
        start_time = time.time()
        
        print(f"🎵 Processing audio file: {file_path}")
        
        # Validate input
        if not Path(file_path).exists():
            raise FileNotFoundError(f"Audio file not found: {file_path}")
        
        # Load models if not already loaded
        self.load_models()
        
        results = {
            "audio_file": file_path,
            "timestamp": datetime.now().isoformat(),
            "transcript": "",
            "summary": "",
            "topic": {},
            "processing_time": 0,
            "status": "processing"
        }
        
        try:
            # Step 1: Speech-to-Text
            print("🎤 Converting speech to text...")
            
            # Import and use Whisper for actual transcription
            
            
            # Load Whisper model
            model_size = getattr(self.config.models, 'whisper_model_size', 'base') if self.config else 'base'
            print(f"Loading Whisper {model_size} model...")
            model = whisper.load_model(model_size)
            
            # Transcribe the audio file
            print("Transcribing audio...")
            result = model.transcribe(file_path)
            transcript = result["text"].strip()
            
            results["transcript"] = transcript
            print(f"📝 Transcript: {transcript[:100]}...")
            
            # Step 2: Summarization
            print("📋 Generating summary...")
            
            if len(transcript) > 50:  # Only summarize if there's enough content
                from transformers import pipeline
                
                print("Loading summarization model...")
                summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
                
                # Split long text if needed
                max_chunk_length = 1000
                if len(transcript) > max_chunk_length:
                    # Split into chunks and summarize each
                    chunks = [transcript[i:i+max_chunk_length] for i in range(0, len(transcript), max_chunk_length)]
                    summaries = []
                    for chunk in chunks:
                        if len(chunk.strip()) > 50:
                            chunk_summary = summarizer(chunk, max_length=100, min_length=20, do_sample=False)
                            summaries.append(chunk_summary[0]['summary_text'])
                    
                    if summaries:
                        # If multiple chunks, summarize the summaries
                        if len(summaries) > 1:
                            combined_summary = " ".join(summaries)
                            if len(combined_summary) > 200:
                                final_summary = summarizer(combined_summary, max_length=150, min_length=30, do_sample=False)
                                summary = final_summary[0]['summary_text']
                            else:
                                summary = combined_summary
                        else:
                            summary = summaries[0]
                    else:
                        summary = "Content too short for summarization"
                else:
                    # Single chunk summarization
                    summary_result = summarizer(transcript, max_length=30, min_length=10, do_sample=False)
                    summary = summary_result[0]['summary_text']
            else:
                summary = "Audio content too short for meaningful summarization"
                
            results["summary"] = summary
            print(f"📄 Summary: {summary}")
            
            # Step 3: Topic Classification
            print("🏷️  Classifying topic...")
            
            if len(transcript) > 10:  # Only classify if there's content
                from transformers import pipeline
                
                print("Loading classification model...")
                classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
                
                # Predefined topics
                candidate_labels = [
                    "technology", "business", "education", "entertainment", 
                    "health", "sports", "politics", "casual conversation",
                    "news", "science", "finance", "travel"
                ]
                
                classification_result = classifier(transcript, candidate_labels)
                
                topic_result = {
                    "label": classification_result['labels'][0],
                    "confidence": classification_result['scores'][0],
                    "all_scores": dict(zip(classification_result['labels'][:5], classification_result['scores'][:5]))
                }
            else:
                topic_result = {
                    "label": "unknown",
                    "confidence": 0.0,
                    "all_scores": {"unknown": 1.0}
                }
                
            results["topic"] = topic_result
            print(f"📊 Topic: {topic_result['label']} (confidence: {topic_result['confidence']:.2f})")
            
            # Calculate processing time
            processing_time = time.time() - start_time
            results["processing_time"] = processing_time
            results["status"] = "completed"
            
            # Save results
            if output_path:
                self._save_results(results, output_path)
            
            print(f"✅ Processing completed in {processing_time:.2f} seconds")
            
        except Exception as e:
            results["status"] = "error"
            results["error"] = str(e)
            print(f"❌ Processing failed: {e}")
            raise
        
        return results
    
    def process_microphone_input(self, duration: int = 10) -> Dict[str, Any]:
        """
        Process live microphone input.
        
        Args:
            duration (int): Recording duration in seconds
            
        Returns:
            Dict[str, Any]: Processing results
        """
        print(f"🎙️  Recording from microphone for {duration} seconds...")
        
        # Load models if not already loaded
        self.load_models()
        
        # Record audio (will be implemented later)
        # audio_data = self.audio_handler.record_from_microphone(duration)
        
        # Process the recorded audio similar to file processing
        # For now, return placeholder results
        return {
            "audio_source": "microphone",
            "duration": duration,
            "transcript": "Live recording transcript placeholder",
            "summary": "Live recording summary placeholder", 
            "topic": {"label": "casual", "confidence": 0.75},
            "timestamp": datetime.now().isoformat(),
            "status": "completed"
        }
    
    def _save_results(self, results: Dict[str, Any], output_path: str):
        """
        Save processing results to file.
        
        Args:
            results (Dict[str, Any]): Results to save
            output_path (str): Output file path
        """
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Save as JSON
        if output_file.suffix.lower() == '.json':
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
        else:
            # Save as formatted text
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"Audio Conversation Analysis Results\n")
                f.write(f"{'=' * 40}\n\n")
                f.write(f"File: {results['audio_file']}\n")
                f.write(f"Processed: {results['timestamp']}\n")
                f.write(f"Duration: {results.get('processing_time', 0):.2f}s\n\n")
                
                f.write(f"TRANSCRIPT:\n")
                f.write(f"{'-' * 20}\n")
                f.write(f"{results['transcript']}\n\n")
                
                f.write(f"SUMMARY:\n")
                f.write(f"{'-' * 20}\n")
                f.write(f"{results['summary']}\n\n")
                
                f.write(f"TOPIC CLASSIFICATION:\n")
                f.write(f"{'-' * 20}\n")
                topic = results['topic']
                f.write(f"Primary Topic: {topic.get('label', 'unknown')}\n")
                f.write(f"Confidence: {topic.get('confidence', 0):.2f}\n")
        
        print(f"💾 Results saved to: {output_path}")
    
    def batch_process(self, input_directory: str, output_directory: str) -> Dict[str, Any]:
        """
        Process multiple audio files in a directory.
        
        Args:
            input_directory (str): Directory containing audio files
            output_directory (str): Directory to save results
            
        Returns:
            Dict[str, Any]: Batch processing summary
        """
        from src.utils.file_utils import FileUtils
        
        input_dir = Path(input_directory)
        output_dir = Path(output_directory)
        
        if not input_dir.exists():
            raise FileNotFoundError(f"Input directory not found: {input_directory}")
        
        # Find all audio files
        audio_files = FileUtils.list_audio_files(str(input_dir))
        
        if not audio_files:
            print("⚠️  No audio files found in input directory")
            return {"processed": 0, "failed": 0, "files": []}
        
        print(f"📁 Found {len(audio_files)} audio files to process")
        
        results = {
            "processed": 0,
            "failed": 0,
            "files": [],
            "start_time": datetime.now().isoformat(),
            "end_time": "",
            "total_duration": 0
        }
        
        start_time = time.time()
        
        for audio_file in audio_files:
            try:
                file_name = Path(audio_file).stem
                output_file = output_dir / f"{file_name}_results.json"
                
                print(f"\n🔄 Processing {file_name}...")
                file_results = self.process_audio_file(audio_file, str(output_file))
                
                results["files"].append({
                    "file": audio_file,
                    "status": "success",
                    "results": file_results
                })
                results["processed"] += 1
                
            except Exception as e:
                print(f"❌ Failed to process {audio_file}: {e}")
                results["files"].append({
                    "file": audio_file,
                    "status": "failed", 
                    "error": str(e)
                })
                results["failed"] += 1
        
        total_time = time.time() - start_time
        results["end_time"] = datetime.now().isoformat()
        results["total_duration"] = total_time
        
        print(f"\n📊 Batch processing completed:")
        print(f"   ✅ Processed: {results['processed']} files")
        print(f"   ❌ Failed: {results['failed']} files")
        print(f"   ⏱️  Total time: {total_time:.2f} seconds")
        
        return results