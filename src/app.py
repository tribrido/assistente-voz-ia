from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
import sys
from dotenv import load_dotenv

# Adiciona o diretório 'src' ao PATH para permitir importações relativas
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from core.speech_to_text import transcribe_audio
from core.chat_gpt_processor import get_chat_gpt_response
from core.text_to_speech import synthesize_speech

# Carrega variáveis de ambiente
load_dotenv()

# Inicializa a aplicação Flask
app = Flask(__name__, template_folder='../templates', static_folder='../static')
CORS(app)

# Armazena o histórico de conversas em memória (para produção, use um banco de dados)
conversation_history = []

@app.route('/')
def index():
    """Renderiza a página principal da aplicação."""
    return render_template('index.html')

@app.route('/api/transcribe', methods=['POST'])
def transcribe():
    """
    Endpoint para transcrever áudio.
    Recebe um arquivo de áudio e retorna a transcrição.
    """
    try:
        if 'audio' not in request.files:
            return jsonify({'error': 'Nenhum arquivo de áudio foi enviado'}), 400
        
        audio_file = request.files['audio']
        if audio_file.filename == '':
            return jsonify({'error': 'Nenhum arquivo foi selecionado'}), 400
        
        # Salva o arquivo temporariamente
        temp_audio_path = 'temp_audio.wav'
        audio_file.save(temp_audio_path)
        
        # Transcreve o áudio
        language = request.form.get('language', 'pt')
        transcription = transcribe_audio(temp_audio_path, language=language)
        
        # Remove o arquivo temporário
        if os.path.exists(temp_audio_path):
            os.remove(temp_audio_path)
        
        if transcription:
            return jsonify({'transcription': transcription}), 200
        else:
            return jsonify({'error': 'Erro ao transcrever o áudio'}), 500
    
    except Exception as e:
        return jsonify({'error': f'Erro no servidor: {str(e)}'}), 500

@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Endpoint para obter resposta do ChatGPT.
    Recebe um texto e retorna a resposta.
    """
    try:
        data = request.get_json()
        user_message = data.get('message')
        
        if not user_message:
            return jsonify({'error': 'Mensagem não fornecida'}), 400
        
        # Obtém resposta do ChatGPT
        response = get_chat_gpt_response(user_message, conversation_history=conversation_history)
        
        if response:
            # Atualiza o histórico de conversas
            conversation_history.append({"role": "user", "content": user_message})
            conversation_history.append({"role": "assistant", "content": response})
            
            return jsonify({'response': response}), 200
        else:
            return jsonify({'error': 'Erro ao obter resposta do ChatGPT'}), 500
    
    except Exception as e:
        return jsonify({'error': f'Erro no servidor: {str(e)}'}), 500

@app.route('/api/synthesize', methods=['POST'])
def synthesize():
    """
    Endpoint para sintetizar texto em voz.
    Recebe um texto e retorna um arquivo de áudio.
    """
    try:
        data = request.get_json()
        text = data.get('text')
        language = data.get('language', 'pt')
        
        if not text:
            return jsonify({'error': 'Texto não fornecido'}), 400
        
        # Sintetiza o texto em voz
        output_filename = 'response_audio.mp3'
        synthesize_speech(text, lang=language, output_filename=output_filename)
        
        # Retorna o caminho do arquivo de áudio
        return jsonify({'audio_file': output_filename}), 200
    
    except Exception as e:
        return jsonify({'error': f'Erro no servidor: {str(e)}'}), 500

@app.route('/api/history', methods=['GET'])
def get_history():
    """
    Endpoint para obter o histórico de conversas.
    """
    return jsonify({'history': conversation_history}), 200

@app.route('/api/clear-history', methods=['POST'])
def clear_history():
    """
    Endpoint para limpar o histórico de conversas.
    """
    global conversation_history
    conversation_history = []
    return jsonify({'message': 'Histórico limpo com sucesso'}), 200

if __name__ == '__main__':
    # Verifica se a chave de API da OpenAI está configurada
    if not os.environ.get('OPENAI_API_KEY'):
        print("ERRO: A variável de ambiente OPENAI_API_KEY não está configurada.")
        print("Por favor, configure-a no arquivo .env ou como variável de ambiente.")
        sys.exit(1)
    
    # Inicia o servidor Flask em modo debug
    app.run(debug=True, host='0.0.0.0', port=5000)
