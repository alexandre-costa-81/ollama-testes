from ollama import chat
from ollama import ChatResponse

def enviar_mensagem(mensagem, lista_mensagens=[]):
    lista_mensagens.append({'role': 'user', 'content': mensagem})

    response: ChatResponse = chat(
        model='llama3.2',
        messages=lista_mensagens,
    )
    lista_mensagens.append({'role': response.message.role, 'content': response.message.content})
    return response.message

def enviar_mensagem_por_stream(mensagem, lista_mensagens=[]):
    lista_mensagens.append({'role': 'user', 'content': mensagem})

    return chat(
        model='llama3.2',
        messages=lista_mensagens,
        stream=True,
    )

def obter_resposta(mensagem, lista_mensagens=[]):
    print('Chatbot: ', end='', flush=True)
    for response in enviar_mensagem_por_stream(mensagem, lista_mensagens):
        print(response['message']['content'], end='', flush=True)
    print('')

lista_mensagens = [{'role': 'system', 'content': 'Responda com respostas diretas.'}]

while True:
    texto = input('Usuário: ')

    if texto == 'sair':
        break
    else:
        obter_resposta(texto, lista_mensagens)
        # resposta = enviar_mensagem(texto, lista_mensagens)
        # print("Chatbot: ", resposta['content'])

# Em que ano Einstein publicou a teoria geral da relatividade?