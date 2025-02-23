import os
import warnings
import tkinter as tk
import customtkinter as ctk
from utils import record_audio, inference

warnings.filterwarnings("ignore")

class WhisperApp:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.geometry("640x480")
        self.app.title("Whisper GUI")
        self.recording_path = "recording.wav"
        self.setup_ui()
        
    def setup_ui(self):
        # Create title
        title_label = ctk.CTkLabel(self.app, text="Whisper Transcription App", font=("Arial", 24))
        title_label.pack(pady=20)

        # Create button frame
        button_frame = ctk.CTkFrame(self.app)
        button_frame.pack(pady=20)

        # Create buttons
        record_button = ctk.CTkButton(button_frame, text="Record", width=120, command=self.safe_record)
        record_button.pack(pady=(0, 10))


        transcribe_button = ctk.CTkButton(button_frame, text="Transcribe", width=120, command=self.safe_transcribe)
        transcribe_button.pack(side="left", padx=10)

        translate_button = ctk.CTkButton(button_frame, text="Translate", width=120, command=self.safe_translate)
        translate_button.pack(side="left", padx=10)

        # Create output box
        self.output_label = tk.Label(self.app, text="Recording is only for 5secs\nTranslate is not working properly 😅", width=80, height=10, wraplength=580, justify="left", bg="white")
        self.output_label.pack(side="bottom", pady=20)

    def update_output(self, text):
        self.output_label.config(text=text)

    def safe_record(self):
        try:
            record_audio()
            self.update_output("Recording completed successfully!")
        except Exception as e:
            self.update_output(f"Recording error: {str(e)}")

    def safe_transcribe(self):
        if not os.path.exists(self.recording_path):
            self.update_output("Error: No recording found. Please record first.")
            return
        
        try:
            result = inference(self.recording_path, modelname='tiny', task="transcribe")
            self.update_output(result)
        except Exception as e:
            self.update_output(f"Transcription error: {str(e)}")

    def safe_translate(self):
        if not os.path.exists(self.recording_path):
            self.update_output("Error: No recording found. Please record first.")
            return
            
        try:
            result = inference(self.recording_path, modelname='tiny', task="translate", language="zh")
            self.update_output(result)
        except Exception as e:
            self.update_output(f"Translation error: {str(e)}")

    def run(self):
        self.app.mainloop()

if __name__ == "__main__":
    app = WhisperApp()
    app.run()
