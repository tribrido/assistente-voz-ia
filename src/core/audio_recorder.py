import sounddevice as sd
import soundfile as sf
import numpy as np

def record_audio(filename='recorded_audio.wav', duration=5, samplerate=44100):
    """
    Grava áudio do microfone por uma duração especificada.

    Args:
        filename (str): Nome do arquivo para salvar o áudio.
        duration (int): Duração da gravação em segundos.
        samplerate (int): Taxa de amostragem do áudio.

    Returns:
        str: O nome do arquivo de áudio gravado.
    """
    print(f"Gravando áudio por {duration} segundos...")
    # Grava o áudio
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='float64')
    sd.wait()  # Espera a gravação terminar

    # Salva o áudio em um arquivo WAV
    sf.write(filename, recording, samplerate)
    print(f"Áudio salvo em {filename}")
    return filename

if __name__ == '__main__':
    # Exemplo de uso:
    # Certifique-se de ter um microfone conectado e configurado.
    # Pode ser necessário instalar 'portaudio' para 'sounddevice' funcionar.
    # sudo apt-get install portaudio19-dev python3-pyaudio
    # pip install sounddevice soundfile numpy
    record_audio(duration=5)
