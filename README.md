# 🗣️ Assistente de Voz Multi-Idiomas com IA

![Assistente de Voz Conceito](docs/assistente_voz_conceito.png)

## 🚀 Visão Geral do Projeto

Este projeto desenvolve um **Assistente de Voz Multi-Idiomas** inovador, combinando as mais recentes tecnologias de Inteligência Artificial para permitir uma comunicação fluida e natural. Utilizando o **Whisper** da OpenAI para transcrição de fala (Speech-to-Text), o **ChatGPT** para processamento de linguagem natural e geração de respostas inteligentes, e o **Google Text-to-Speech (gTTS)** para sintetizar as respostas em voz, o assistente oferece uma experiência de usuário rica e interativa.

O objetivo principal é demonstrar a integração dessas poderosas ferramentas para criar soluções de comunicação ágeis e adaptativas, com foco em conversas multi-idiomas por voz.

## ✨ Funcionalidades

*   **Gravação de Áudio**: Captura de entrada de voz do usuário.
*   **Speech-to-Text (Whisper)**: Transcrição precisa de áudio para texto em diversos idiomas.
*   **Processamento de Linguagem Natural (ChatGPT)**: Geração de respostas inteligentes e contextualmente relevantes.
*   **Text-to-Speech (gTTS)**: Conversão de texto para fala, permitindo que o assistente responda por voz.
*   **Suporte Multi-Idiomas**: Capacidade de processar e responder em diferentes idiomas.

## 💡 Diferenciais e Melhorias (Exemplos)

Este projeto foi aprimorado com as seguintes funcionalidades e práticas de desenvolvimento para se destacar:

*   **Interface Web Interativa**: Uma interface de usuário moderna e responsiva desenvolvida com Flask para uma experiência de usuário intuitiva.
*   **Gerenciamento de Contexto de Conversa**: Implementação de um histórico de conversas para que o ChatGPT mantenha o contexto em interações mais longas, proporcionando diálogos mais coerentes.
*   **Detecção Automática de Idioma**: Integração de um mecanismo para detectar automaticamente o idioma da entrada de voz, tornando o assistente mais adaptável.
*   **Testes Automatizados**: Cobertura abrangente de testes unitários e de integração (`pytest`) para garantir a robustez e a confiabilidade do código.
*   **Integração Contínua (CI/CD)**: Configuração de `GitHub Actions` para automatizar a execução de testes e a verificação de qualidade do código a cada `push`.
*   **Segurança de Credenciais**: Utilização de variáveis de ambiente (`.env`) para o gerenciamento seguro de chaves de API, evitando a exposição de informações sensíveis.

## 🛠️ Tecnologias Utilizadas

*   **Python**: Linguagem de programação principal.
*   **OpenAI Whisper**: Modelo de Speech-to-Text.
*   **OpenAI ChatGPT API**: Para processamento de linguagem natural.
*   **Google Text-to-Speech (gTTS)**: Para conversão de texto em fala.
*   **Flask**: Microframework web para a interface de usuário.
*   **Flask-CORS**: Extensão para habilitar CORS.
*   **HTML/CSS/JavaScript**: Para o frontend da aplicação web.

## ⚙️ Como Instalar e Rodar

Siga os passos abaixo para configurar e executar o projeto localmente:

### Pré-requisitos

*   Python 3.x
*   Chave de API da OpenAI (para Whisper e ChatGPT)

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/tribrido/assistente-voz-ia.git
    cd assistente-voz-ia
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows: `venv\\Scripts\\activate`
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure suas chaves de API:**
    Crie um arquivo `.env` na raiz do projeto e adicione sua chave da OpenAI:
    ```
    OPENAI_API_KEY="sua_chave_aqui"
    ```
    *Nunca compartilhe seu arquivo `.env` ou suas chaves de API publicamente.*

### Execução

Para iniciar o assistente de voz com a interface web:

```bash
python src/app.py
```

Após iniciar o servidor Flask, abra seu navegador e acesse `http://127.0.0.1:5000` (ou o endereço indicado no terminal).

## 📖 Como Usar

1.  **Acesse a Interface Web**: Abra `http://127.0.0.1:5000` no seu navegador.
2.  **Selecione o Idioma**: Escolha o idioma desejado no seletor.
3.  **Inicie a Gravação**: Clique no botão "🎤 Iniciar Gravação" e fale sua pergunta.
4.  **Pare a Gravação**: Clique no botão "⏹️ Parar Gravação" quando terminar de falar.
5.  **Visualize a Interação**: A transcrição da sua fala, a resposta do assistente e o áudio da resposta serão exibidos na interface.
6.  **Histórico de Conversas**: O histórico das interações será mantido e exibido na parte inferior da página. Você pode limpá-lo a qualquer momento.

## 🤝 Contribuição

Contribuições são bem-vindas! Se você tiver sugestões de melhoria, encontrou um bug ou deseja adicionar novas funcionalidades, por favor, siga as diretrizes em CONTRIBUTING.md.

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.

📧 Contato

Marcelo Costa - tribrido

Projeto Link: [https://github.com/tribrido/assistente-voz-ia](https://github.com/tribrido/assistente-voz-ia)

