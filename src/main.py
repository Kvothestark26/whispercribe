from transcriber import Transcriber
from config import MODEL_SIZE

def main():
    transcriber = Transcriber(MODEL_SIZE)

    text = transcriber.transcribe("audio/audioprueba.mp3")

    with open("output/prueba.txt", "w", encoding="utf-8") as file:
        file.write(text)

    print()
    print("===== TRANSCRIPCIÓN =====")
    print(text)


if __name__ == "__main__":
    main()