# Diretrizes para Contribuição

Ficamos felizes com o seu interesse em contribuir para o projeto **Assistente de Voz Multi-Idiomas com IA**! Para garantir um processo de colaboração eficiente e harmonioso, por favor, siga as diretrizes abaixo.

## Como Contribuir

1.  **Faça um Fork do Repositório**: Comece fazendo um fork do nosso repositório para a sua conta GitHub.

2.  **Clone o Repositório**: Clone o seu fork para a sua máquina local:
    ```bash
    git clone https://github.com/SEU_USUARIO/assistente-voz-ia.git
    cd assistente-voz-ia
    ```

3.  **Crie uma Nova Branch**: Crie uma branch para a sua feature ou correção. Use nomes descritivos, como `feature/nova-funcionalidade` ou `bugfix/correcao-erro-x`.
    ```bash
    git checkout -b feature/sua-nova-feature
    ```

4.  **Instale as Dependências**: Certifique-se de ter todas as dependências instaladas:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Desenvolva sua Feature/Correção**: Implemente suas mudanças. Lembre-se de seguir as boas práticas de Clean Code e modularização.

6.  **Escreva Testes**: Se aplicável, adicione testes unitários e/ou de integração para suas mudanças. Isso ajuda a garantir que seu código funcione como esperado e não introduza regressões.

7.  **Execute os Testes**: Antes de submeter, execute todos os testes para garantir que tudo está funcionando:
    ```bash
    pytest
    ```

8.  **Formate o Código**: Utilize um formatador de código (como `Black` para Python) para manter a consistência do estilo:
    ```bash
    black ./
    ```

9.  **Faça Commit das Suas Mudanças**: Escreva mensagens de commit claras e descritivas. Recomenda-se o uso de [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) para padronizar as mensagens.
    ```bash
    git commit -m 
"`feat: Adiciona nova funcionalidade X`"
    ```

10. **Envie suas Mudanças**: Faça o push da sua branch para o seu fork no GitHub:
    ```bash
    git push origin feature/sua-nova-feature
    ```

11. **Abra um Pull Request (PR)**: Vá para o repositório original no GitHub e abra um Pull Request da sua branch para a branch `main` (ou a branch de desenvolvimento apropriada). Descreva suas mudanças em detalhes e referencie quaisquer issues relacionadas.

## Padrões de Código

*   Siga o estilo de código [PEP 8](https://www.python.org/dev/peps/pep-0008/) para Python.
*   Mantenha as funções pequenas e com uma única responsabilidade.
*   Adicione comentários onde o código não for autoexplicativo.
*   Use nomes de variáveis e funções descritivos.

## Reportando Bugs

Se você encontrar um bug, por favor, abra uma issue no GitHub. Inclua o máximo de detalhes possível:

*   Uma descrição clara e concisa do bug.
*   Passos para reproduzir o comportamento.
*   O comportamento esperado.
*   O comportamento atual.
*   Capturas de tela ou logs, se relevantes.

## Sugerindo Novas Funcionalidades

Novas ideias são sempre bem-vindas! Se você tem uma sugestão para uma nova funcionalidade, por favor, abra uma issue no GitHub para discutirmos. Descreva a funcionalidade, o problema que ela resolve e como você imagina que ela funcionaria.

Obrigado por contribuir!
