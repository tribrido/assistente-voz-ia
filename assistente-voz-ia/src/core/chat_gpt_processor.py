import openai
import os

def get_chat_gpt_response(prompt, model="gpt-4", conversation_history=None):
    """
    Obtém uma resposta do ChatGPT para um dado prompt.

    Args:
        prompt (str): O prompt ou pergunta do usuário.
        model (str): O modelo do ChatGPT a ser usado (e.g., "gpt-4", "gpt-3.5-turbo").
        conversation_history (list): Lista de mensagens anteriores para manter o contexto.
                                     Cada item é um dicionário {"role": "user"/"assistant", "content": "mensagem"}.

    Returns:
        str: A resposta gerada pelo ChatGPT.
    """
    if not os.environ.get("OPENAI_API_KEY"):
        raise ValueError("A variável de ambiente OPENAI_API_KEY não está configurada.")

    messages = []
    if conversation_history:
        messages.extend(conversation_history)
    messages.append({"role": "user", "content": prompt})

    try:
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model=model,
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Erro ao obter resposta do ChatGPT: {e}")
        return None

if __name__ == '__main__':
    # Exemplo de uso (requer OPENAI_API_KEY configurada):
    # from dotenv import load_dotenv
    # load_dotenv()

    # Exemplo de conversa sem histórico
    response1 = get_chat_gpt_response("Qual é a capital do Brasil?")
    if response1:
        print(f"ChatGPT (1): {response1}")

    # Exemplo de conversa com histórico
    history = [
        {"role": "user", "content": "Olá, tudo bem?"},
        {"role": "assistant", "content": "Olá! Tudo ótimo, e com você?"}
    ]
    response2 = get_chat_gpt_response("Poderia me contar uma piada?", conversation_history=history)
    if response2:
        print(f"ChatGPT (2): {response2}")

    response3 = get_chat_gpt_response("E sobre o que conversamos antes?", conversation_history=history + [{"role": "user", "content": "Poderia me contar uma piada?"}, {"role": "assistant", "content": response2}])
    if response3:
        print(f"ChatGPT (3): {response3}")
