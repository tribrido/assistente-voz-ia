// Variáveis globais
let mediaRecorder;
let audioChunks = [];
let isRecording = false;

// Elementos do DOM
const recordBtn = document.getElementById('record-btn');
const stopBtn = document.getElementById('stop-btn');
const languageSelect = document.getElementById('language-select');
const recordingStatus = document.getElementById('recording-status');
const transcriptionOutput = document.getElementById('transcription-output');
const responseOutput = document.getElementById('response-output');
const responseAudio = document.getElementById('response-audio');
const historyOutput = document.getElementById('history-output');
const clearHistoryBtn = document.getElementById('clear-history-btn');

// Inicializa a aplicação
document.addEventListener('DOMContentLoaded', () => {
    initializeRecorder();
    setupEventListeners();
    loadHistory();
});

/**
 * Inicializa o gravador de áudio do navegador.
 */
async function initializeRecorder() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream);

        mediaRecorder.ondataavailable = (event) => {
            audioChunks.push(event.data);
        };

        mediaRecorder.onstop = async () => {
            const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
            await sendAudioForTranscription(audioBlob);
            audioChunks = [];
        };
    } catch (error) {
        showError('Erro ao acessar o microfone. Verifique as permissões do navegador.');
        console.error('Erro ao inicializar gravador:', error);
    }
}

/**
 * Configura os listeners de eventos dos botões.
 */
function setupEventListeners() {
    recordBtn.addEventListener('click', startRecording);
    stopBtn.addEventListener('click', stopRecording);
    clearHistoryBtn.addEventListener('click', clearHistory);
}

/**
 * Inicia a gravação de áudio.
 */
function startRecording() {
    if (!mediaRecorder) {
        showError('Gravador não inicializado. Recarregue a página.');
        return;
    }

    audioChunks = [];
    mediaRecorder.start();
    isRecording = true;

    recordBtn.disabled = true;
    stopBtn.disabled = false;

    showStatus('🎤 Gravando...', 'recording');
}

/**
 * Para a gravação de áudio.
 */
function stopRecording() {
    if (!mediaRecorder || !isRecording) return;

    mediaRecorder.stop();
    isRecording = false;

    recordBtn.disabled = false;
    stopBtn.disabled = true;

    showStatus('⏹️ Gravação parada. Processando...', 'success');
}

/**
 * Envia o áudio para transcrição.
 */
async function sendAudioForTranscription(audioBlob) {
    try {
        const formData = new FormData();
        formData.append('audio', audioBlob, 'audio.wav');
        formData.append('language', languageSelect.value);

        const response = await fetch('/api/transcribe', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (response.ok) {
            displayTranscription(data.transcription);
            await sendMessageToChat(data.transcription);
        } else {
            showError(data.error || 'Erro ao transcrever áudio');
        }
    } catch (error) {
        showError('Erro ao enviar áudio para transcrição');
        console.error('Erro:', error);
    }
}

/**
 * Envia a mensagem para o ChatGPT.
 */
async function sendMessageToChat(message) {
    try {
        showStatus('💬 Obtendo resposta do assistente...', 'success');

        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message })
        });

        const data = await response.json();

        if (response.ok) {
            displayResponse(data.response);
            await synthesizeResponse(data.response);
            loadHistory();
        } else {
            showError(data.error || 'Erro ao obter resposta do ChatGPT');
        }
    } catch (error) {
        showError('Erro ao enviar mensagem para o chat');
        console.error('Erro:', error);
    }
}

/**
 * Sintetiza a resposta em voz.
 */
async function synthesizeResponse(text) {
    try {
        showStatus('🔊 Sintetizando resposta em voz...', 'success');

        const response = await fetch('/api/synthesize', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                text,
                language: languageSelect.value
            })
        });

        const data = await response.json();

        if (response.ok) {
            playAudio(data.audio_file);
            showStatus('✅ Resposta pronta!', 'success');
        } else {
            showError(data.error || 'Erro ao sintetizar voz');
        }
    } catch (error) {
        showError('Erro ao sintetizar resposta');
        console.error('Erro:', error);
    }
}

/**
 * Reproduz o áudio da resposta.
 */
function playAudio(audioFile) {
    responseAudio.src = audioFile;
    responseAudio.play().catch(error => {
        console.error('Erro ao reproduzir áudio:', error);
    });
}

/**
 * Exibe a transcrição na tela.
 */
function displayTranscription(text) {
    transcriptionOutput.innerHTML = `<p><strong>Você:</strong> ${escapeHtml(text)}</p>`;
}

/**
 * Exibe a resposta do assistente na tela.
 */
function displayResponse(text) {
    responseOutput.innerHTML = `<p><strong>Assistente:</strong> ${escapeHtml(text)}</p>`;
}

/**
 * Carrega e exibe o histórico de conversas.
 */
async function loadHistory() {
    try {
        const response = await fetch('/api/history');
        const data = await response.json();

        if (response.ok && data.history.length > 0) {
            let historyHtml = '';
            data.history.forEach(item => {
                const roleLabel = item.role === 'user' ? '👤 Você' : '🤖 Assistente';
                historyHtml += `
                    <div class="history-item">
                        <div class="role">${roleLabel}</div>
                        <div class="content">${escapeHtml(item.content)}</div>
                    </div>
                `;
            });
            historyOutput.innerHTML = historyHtml;
        } else {
            historyOutput.innerHTML = '<p class="placeholder">Nenhuma conversa ainda...</p>';
        }
    } catch (error) {
        console.error('Erro ao carregar histórico:', error);
    }
}

/**
 * Limpa o histórico de conversas.
 */
async function clearHistory() {
    if (!confirm('Tem certeza que deseja limpar o histórico de conversas?')) {
        return;
    }

    try {
        const response = await fetch('/api/clear-history', {
            method: 'POST'
        });

        if (response.ok) {
            historyOutput.innerHTML = '<p class="placeholder">Histórico limpo...</p>';
            showStatus('✅ Histórico limpo com sucesso!', 'success');
        } else {
            showError('Erro ao limpar histórico');
        }
    } catch (error) {
        showError('Erro ao limpar histórico');
        console.error('Erro:', error);
    }
}

/**
 * Exibe uma mensagem de status.
 */
function showStatus(message, type = 'info') {
    recordingStatus.textContent = message;
    recordingStatus.className = `status-message ${type}`;
    
    if (type !== 'recording') {
        setTimeout(() => {
            recordingStatus.className = 'status-message';
            recordingStatus.textContent = '';
        }, 5000);
    }
}

/**
 * Exibe uma mensagem de erro.
 */
function showError(message) {
    showStatus(`❌ ${message}`, 'error');
}

/**
 * Escapa caracteres HTML para evitar XSS.
 */
function escapeHtml(text) {
    const map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
    };
    return text.replace(/[&<>"']/g, m => map[m]);
}
