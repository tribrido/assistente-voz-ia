from gtts import gTTS
import os

def synthesize_speech(text, lang="pt", output_filename="response_audio.mp3"):
    """
    Sintetiza texto em fala usando Google Text-to-Speech (gTTS).

    Args:
        text (str): O texto a ser convertido em fala.
        lang (str): O idioma da fala (e.g., "pt" para português, "en" para inglês).
        output_filename (str): O nome do arquivo para salvar o áudio.

    Returns:
        str: O nome do arquivo de áudio gerado.
    """
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save(output_filename)
        print(f"Áudio de resposta salvo em {output_filename}")
        return output_filename
    except Exception as e:
        print(f"Erro ao sintetizar fala: {e}")
        return None

if __name__ == '__main__':
    # Exemplo de uso:
    synthesize_speech("Olá, eu sou um assistente de voz multi-idiomas.", lang="pt")
    synthesize_speech("Hello, I am a multi-language voice assistant.", lang="en", output_filename="hello_en.mp3")
