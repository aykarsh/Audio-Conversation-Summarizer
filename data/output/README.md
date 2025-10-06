# Output Directory

This directory stores the processed results from the Audio Conversation Summarizer.

## Output File Types

### JSON Results
Complete processing results in structured format:
```json
{
  "audio_file": "sample_meeting.wav",
  "transcript": "Full transcribed text...",
  "summary": "Concise summary of the conversation...",
  "topic": {
    "label": "business",
    "confidence": 0.95,
    "all_scores": {
      "business": 0.95,
      "technology": 0.75,
      "casual": 0.12
    }
  },
  "processing_time": 45.2,
  "timestamp": "2024-01-15T14:30:00Z"
}
```

### Text Files
Individual text files for each component:
- `filename_transcript.txt` - Full transcript
- `filename_summary.txt` - Generated summary
- `filename_topic.txt` - Topic classification result

## File Naming Convention

Results are saved with timestamps and source file references:
- `results_YYYYMMDD_HHMMSS.json`
- `meeting_20240115_transcript.txt`
- `interview_20240115_summary.txt`

## Cleanup

Old results can be safely deleted. The application does not depend on previously generated output files.