# Voice Assistant Application

A Python-based voice assistant that processes spoken commands and responds using text-to-speech synthesis. The assistant can perform real-time speech recognition, provide current time information, and search Wikipedia.

## Course Concepts Addressed

This project demonstrates key programming concepts essential for systems and software development:

### 1. **API Integration & Library Management**
- Integrates multiple third-party libraries: `speech_recognition`, `pyttsx3`, and `wikipedia`
- Demonstrates practical use of external APIs (Google Speech Recognition API)
- Shows dependency management for cross-platform compatibility

### 2. **Exception Handling**
- Implements try-except blocks for robust error management
- Handles specific exceptions: `DisambiguationError`, `PageError`, `UnknownValueError`, `RequestError`
- Gracefully manages API failures and user input errors

### 3. **Modular Design & Functions**
- Separates concerns into well-defined functions (`speak()`, `recognize_speech()`, `process_command()`, etc.)
- Improves code reusability and maintainability
- Enables easier testing and debugging

### 4. **String Processing & User Input**
- Implements text normalization (lowercase conversion)
- Demonstrates command parsing and conditional logic
- Shows practical voice-to-text workflow

## Solution Design

### Architecture Overview
The application follows a sequential, event-driven architecture:

1. **Initialization Phase**: Engine setup and voice configuration
2. **Recognition Loop**: Continuous listening for user commands
3. **Processing Phase**: Command parsing and action execution
4. **Response Phase**: Text-to-speech feedback

### Core Functions

| Function | Purpose |
|----------|---------|
| `speak(text)` | Converts text to speech using Windows SAPI5 engine |
| `recognize_speech()` | Captures microphone input and converts to text using Google API |
| `get_time()` | Retrieves and announces current time in 12-hour format |
| `search_wikipedia(query)` | Fetches Wikipedia summaries and announces results |
| `process_command(command)` | Routes user commands to appropriate handlers |
| `start_voice_assistant()` | Main loop managing continuous assistant operation |

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- Windows OS (application uses SAPI5 text-to-speech)
- Microphone connected and working
- Internet connection (for Google Speech Recognition and Wikipedia)

### Step 1: Install Required Libraries
```bash
pip install SpeechRecognition pyttsx3 wikipedia
```

**Library Details:**
- `SpeechRecognition`: Speech-to-text conversion using Google API
- `pyttsx3`: Offline text-to-speech synthesis
- `wikipedia`: Wikipedia content retrieval API

### Step 2: Verify Microphone
Test your microphone in Windows Settings > Sound > Input devices

### Step 3: Run the Application
```bash
python voice_assistant.py
```

## Usage Guide

### Getting Started
1. Run the script - the assistant will greet you
2. Speak your command clearly after "Listening..." prompt
3. The assistant will process and respond to your command

### Supported Commands

#### Time Query
```
You: "What's the time?"
Assistant: "The current time is 03:45 PM"
```

#### Wikipedia Search
```
You: "Search wikipedia"
Assistant: "What do you want to search on wikipedia?"
You: "Python programming"
Assistant: [Reads Wikipedia summary about Python]
```

#### Exit Commands
```
"exit" OR "stop" OR "quit"
```

## Code Organization

### File Structure
```
voice_assistant.py
├── Imports & Engine Setup (Lines 1-12)
├── Core Functions (Lines 14-66)
│   ├── speak()
│   ├── get_time()
│   ├── search_wikipedia()
│   ├── recognize_speech()
│   └── process_command()
├── Main Loop (Lines 71-76)
└── Execution (Line 80)
```

### Code Quality Practices Implemented
- **Clear variable names**: `recognizer`, `engine`, `command`, `query`
- **Error handling**: Specific exception catching for different failure modes
- **Ambient noise adjustment**: Improves recognition accuracy
- **Status messages**: User feedback during processing ("Listening...", "Searching Wikipedia for...")

## Documentation

### Function Documentation Example
Each function includes:
- **Purpose**: What the function does
- **Input/Output**: Parameters and return values
- **Error handling**: Exception management
- **User feedback**: Print statements and voice responses

### Example Function Analysis

**`recognize_speech()` - Lines 33-52**
- Initializes microphone source
- Adjusts for ambient noise (improves accuracy in noisy environments)
- Captures audio input
- Converts to text via Google Speech Recognition
- Handles three exception types for robustness

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "Could not understand" repeated | Speak more clearly, reduce background noise |
| Microphone not detected | Check Windows Sound Settings, verify microphone connection |
| "API error" message | Verify internet connection, check Google API availability |
| No sound output | Check Windows volume, verify speakers are connected in Settings |
| Wikipedia returns no results | Try more specific search terms, check internet connection |

## Design Decisions

### Why Windows SAPI5?
- Built into Windows OS (no additional TTS engine installation required)
- Reliable and consistent performance
- Supports multiple voices and speech rates

### Why Google Speech Recognition?
- High accuracy for natural language
- Handles accents and speaking styles
- Robust among various microphone qualities

### Why Wikipedia?
- Educational relevance (appropriate for course context)
- Demonstrates API integration with error handling
- Provides meaningful, verifiable responses

## Performance Characteristics

- **Recognition latency**: 2-5 seconds (depends on audio length)
- **API response time**: 1-3 seconds (network dependent)
- **Text-to-speech speed**: Real-time based on text length

## Future Enhancement Opportunities

1. Add more commands (weather, news, calculations)
2. Implement local speech recognition (privacy enhancement)
3. Add command history logging
4. Create configuration file for customizable settings
5. Support for multiple languages

## Dependencies & Versions

- `SpeechRecognition` >= 3.8.1
- `pyttsx3` >= 2.90
- `wikipedia` >= 1.4.0
- `Python` >= 3.7

## Running the Application

```bash
# Navigate to the directory
cd OneDrive/Desktop/

# Execute the script
python voice_assistant.py
```

The assistant will start immediately with a greeting.

## Conclusion

This voice assistant demonstrates practical application of course concepts including exception handling, API integration, modular design, and event-driven programming. The implementation prioritizes robustness through comprehensive error handling while maintaining clear, readable code structure suitable for educational purposes.
