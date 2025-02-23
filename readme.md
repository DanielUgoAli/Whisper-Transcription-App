# Whisper Transcription App

A simple GUI application for audio transcription and translation using OpenAI's Whisper model using Tkinter.

## Table of Contents

## Features

- Record audio directly from your microphone
- Transcribe audio to text
- Translate audio to English
- Simple and intuitive interface

## Requirements

- Python 3.7+
- Whisper
- Sounddevice
- Soundfile
- Tkinter
- CustomTkinter

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/DanielUgoAli/Whisper-Transcription-App.git
   cd Whisper-Transcription-App
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python app.py
   ```

## Usage

1. Click "Record" to record audio (5 seconds max)
2. Click "Transcribe" to convert audio to text
3. Click "Translate" to translate audio to English

## Notes

- The app uses the 'base' Whisper model by default
- Translation functionality is currently limited and i mean very limited
- The app is not optimized for long audio recordings
- The app is not optimized for real-time transcription
- Recordings are saved as `recording.wav` in the project directory
- There will be another version of this app that will be optimized for real-time transcription using streamlit and websockets with api usage.
