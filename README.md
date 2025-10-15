# Projeto DIO: Simulação de Malware para Estudos em Cibersegurança

Este projeto foi desenvolvido como parte do desafio "Simulando Malwares para Fins Educacionais", da trilha de cibersegurança da DIO, em parceria com o Santander. O objetivo é demonstrar o funcionamento de malwares de forma controlada e segura, aprofundando o conhecimento sobre ameaças digitais e, mais importante, sobre as **medidas de prevenção e defesa**.

## Conteúdo do Projeto

O repositório contém dois scripts principais:

1.  **Ransomware Simulado (`ransomware.py`):**
    * Um script que simula a criptografia e a descriptografia de arquivos de teste.
    * Utiliza a biblioteca **`cryptography`** com o algoritmo Fernet para criptografia simétrica.
    * O código demonstra como uma chave é gerada e usada para tornar dados inacessíveis, além do processo reverso para recuperar os arquivos.

2.  **Keylogger Simulado (`keylogger_mail.py`):**
    * Um script que captura as teclas digitadas em um ambiente de teste.
    * Utiliza a biblioteca **`pynput`** para monitoramento do teclado.
    * integração com a biblioteca **`smtplib`** para enviar o log de teclas capturadas para um endereço de e-mail pré-configurado, simulando o envio de dados para um atacante.

## Como Rodar o Projeto

**⚠️ Aviso de Segurança:** Este projeto é estritamente educacional. Execute-o apenas em ambientes controlados e em máquinas virtuais. Nunca use esses scripts em arquivos importantes ou em sistemas que não são de sua propriedade.

1.  **Instale as bibliotecas necessárias:**
    ```bash
    pip install cryptography
    pip install pynput
    ```
2.  **Configure o Keylogger:**
    * Abra o arquivo `keylogger_mail.py`.
    * Substitua as variáveis de e-mail e senha de aplicativo (`REMETENTE`, `SENHA_APP`, `DESTINATARIO`) pelas suas credenciais. **Lembre-se de usar uma senha de aplicativo do seu provedor de e-mail (ex: Gmail) e não a senha principal da sua conta.**
3.  **Execute os scripts:**
    ```bash
    # Para o Ransomware
    python ransomware.py
    
    # Para o Keylogger
    python keylogger_mail.py
    ```

## Reflexão sobre Defesa Cibernética

A principal lição deste desafio é que a melhor defesa é o conhecimento. Ao entender como essas ferramentas funcionam, podemos nos proteger de forma mais eficaz. As principais medidas de prevenção e defesa incluem:

* **Antivírus e Firewall:** Usar um bom antivírus e manter o firewall ativo são a primeira linha de defesa contra softwares maliciosos.
* **Conscientização:** A maioria dos ataques se baseia em engenharia social. Evitar clicar em links suspeitos, não abrir anexos desconhecidos e ser cético com solicitações urgentes por e-mail são atitudes essenciais.
* **Ambientes de Teste:** Utilizar ambientes isolados (como máquinas virtuais) para testar softwares desconhecidos impede que eles afetem seu sistema principal.
* **Senhas de Aplicativo:** O uso de senhas de aplicativo para ferramentas externas, como visto neste projeto, é uma prática de segurança fundamental para proteger sua conta principal, mesmo que um script seja comprometido.


---
