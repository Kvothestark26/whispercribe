from faster_whisper import WhisperModel

class Transcriber:
    def __init__(self, model_size="small"):
        """
        Inicializa el transcriptor.

        model_size puede ser:
           tiny
           base
           small
           medium
           large-v3
        """
        print(f"Cargando modelo {model_size}...")
        self.model = WhisperModel(model_size, device="cpu", compute_type="int8")
        print("Modelo cargado correctamente.")
    
    def transcribe(self, audio_path):
        segments, info = self.model.transcribe(audio_path)
        text = ""
        for segment in segments:
            segments_text = []

            for segment in segments:
                segments_text.append(segment.text)

            return "".join(segments_text).strip()
        return text.strip()