import whisper
import openai
import sounddevice as sd
import soundfile as sf


def record_audio(save: bool = True, duration: int = 5, filename: str = "recording.wav"):
    """Records audio from the default microphone.
    
    Args:
        save: Whether to save the recording to a file
        duration: Length of recording in seconds
        filename: Name of file to save recording to
        
    Returns:
        numpy.ndarray: The recorded audio data
    """
    freq = 44100  # Standard sampling rate
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)
    sd.wait()  # Wait for recording to complete
    
    if save:
        sf.write(filename, recording, samplerate=freq)

    return recording


def inference(
    audio: str,
    modelname: str = "base",
    task: str = "transcribe",
    language: str = "en",
    device: str | None = None
):
    """Transcribes audio using OpenAI's Whisper model.
    
    Args:
        audio: Path to audio file to transcribe
        modelname: Name of Whisper model to use (e.g., 'tiny', 'base', 'small', 'medium', 'large')
        task: Task to perform - 'transcribe' or 'translate'
        language: Language of the audio (ISO 639-1 code)
        device: Device to use for inference (e.g., 'cpu' or 'cuda')
    """
    model = whisper.load_model(modelname, device=device)

    options = dict(language=language, best_of=1, fp16=False)
    transcribe_options = {**options, "task": "transcribe"}
    translate_options = {**options, "task": "translate"}

    if task == "transcribe":
        return model.transcribe(audio, **transcribe_options)["text"]
    elif task == "translate":
        return model.transcribe(audio, **translate_options)["text"]
    else:
        raise ValueError(f"Invalid task: {task}")
    



