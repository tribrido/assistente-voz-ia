import openai
import os

def transcribe_audio(audio_file_path, language="pt"):
    """
    Transcreve um arquivo de áudio para texto usando a API Whisper da OpenAI.

    Args:
        audio_file_path (str): Caminho para o arquivo de áudio.
        language (str): Idioma do áudio (e.g., "pt" para português, "en" para inglês).

    Returns:
        str: O texto transcrito do áudio.
    """
    if not os.environ.get("OPENAI_API_KEY"):
        raise ValueError("A variável de ambiente OPENAI_API_KEY não está configurada.")

    try:
        with open(audio_file_path, "rb") as audio_file:
            transcript = openai.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                language=language
            )
        return transcript.text
    except Exception as e:
        print(f"Erro ao transcrever áudio: {e}")
        return None

if __name__ == '__main__':
    # Exemplo de uso (requer um arquivo de áudio e OPENAI_API_KEY configurada):
    # Crie um arquivo de áudio de teste, por exemplo, 'test_audio.wav'
    # e defina a variável de ambiente OPENAI_API_KEY.
    # Ex: export OPENAI_API_KEY='sua_chave_aqui'
    # Ou adicione ao seu .env e carregue com python-dotenv
    
    # from dotenv import load_dotenv
    # load_dotenv()

    # Exemplo de arquivo de áudio (substitua pelo seu)
    test_audio_path = "recorded_audio.wav"
    if os.path.exists(test_audio_path):
        transcription = transcribe_audio(test_audio_path, language="pt")
        if transcription:
            print(f"Transcrição: {transcription}")
    else:
        print(f"Arquivo de áudio de teste '{test_audio_path}' não encontrado. Crie um para testar.")
