import os
import sys
from dotenv import load_dotenv

# Adiciona o diretório 'src' ao PATH para permitir importações relativas
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 
                                                os.pardir)))

from src.core.audio_recorder import record_audio
from src.core.speech_to_text import transcribe_audio
from src.core.chat_gpt_processor import get_chat_gpt_response
from src.core.text_to_speech import synthesize_speech

def main():
    load_dotenv() # Carrega variáveis de ambiente do arquivo .env

    print("\nBem-vindo ao Assistente de Voz Multi-Idiomas!")
    print("Pressione Ctrl+C a qualquer momento para sair.")

    conversation_history = []

    while True:
        try:
            # 1. Gravar áudio do usuário
            audio_file = "user_input.wav"
            record_audio(filename=audio_file, duration=5) # Grava por 5 segundos

            # 2. Transcrever áudio para texto
            print("Transcrevendo áudio...")
            user_text = transcribe_audio(audio_file, language="pt") # Assumindo português como idioma padrão

            if user_text:
                print(f"Você disse: {user_text}")

                # 3. Obter resposta do ChatGPT
                print("Obtendo resposta do ChatGPT...")
                chat_response = get_chat_gpt_response(user_text, conversation_history=conversation_history)

                if chat_response:
                    print(f"Assistente: {chat_response}")
                    conversation_history.append({"role": "user", "content": user_text})
                    conversation_history.append({"role": "assistant", "content": chat_response})

                    # 4. Sintetizar resposta em voz
                    response_audio_file = "assistant_response.mp3"
                    synthesize_speech(chat_response, lang="pt", output_filename=response_audio_file)

                    # Opcional: Reproduzir o áudio (requer player de áudio configurado)
                    # from playsound import playsound
                    # playsound(response_audio_file)
                else:
                    print("Não foi possível obter uma resposta do ChatGPT.")
            else:
                print("Não foi possível transcrever o áudio. Tente novamente.")

        except KeyboardInterrupt:
            print("\nEncerrando o assistente. Até logo!")
            break
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            print("Reiniciando o processo...")

if __name__ == "__main__":
    main()
